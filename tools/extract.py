#!/usr/bin/env python3
"""Extract every prompt + animated example from the Motion Library site.

Source : https://kittenjam-motion-library.vercel.app
  index.html  page shell
  data.js     COMPS / WHENS / USES taxonomies + ITEMS[] — one object per
              effect, carrying zh/en names, description, and the AI prompt
  fx.js       FX[id] — the animated example implementation for each id
  fx.css      per-effect (.fx<id>) and shared category CSS
  app.js      page logic; defines how a prompt is copied:
              「<zh>（<en>）」動態效果：<prompt> + PALETTE line

Outputs (repo root, relative to this script's parent folder):
  site/            verbatim copy of the runnable site (the live examples)
  prompts.json     all prompts + metadata + example code, structured
  prompts.md       the whole catalog as one readable document
  prompts.csv      flat table of all prompts
  examples/<comp>/<NNN>-<slug>.md   one file per effect: prompt + example
                   preview settings + its FX[id] JavaScript + its direct
                   .fx<id> CSS rules (with the @keyframes they reference)

Usage:  python3 tools/extract.py            # fetch live and rebuild
        python3 tools/extract.py --local DIR  # rebuild from a saved copy
"""
import ast
import csv
import io
import json
import re
import sys
import urllib.request
from collections import Counter
from pathlib import Path

BASE = "https://kittenjam-motion-library.vercel.app"
ROOT = Path(__file__).resolve().parent.parent
SITE_FILES = ["index.html", "data.js", "fx.js", "fx.css", "app.js", "tracking.js"]
PALETTE = "\n配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。"


def fetch(name: str) -> bytes:
    with urllib.request.urlopen(f"{BASE}/{name}", timeout=60) as r:
        return r.read()


def brace_block(text: str, start: int) -> int:
    """Index just past the } matching the { at/after start, string-aware."""
    brace = text.find("{", start)
    i, depth = brace, 0
    in_str = None
    esc = lc = bc = False
    while i < len(text):
        c = text[i]
        nxt = text[i + 1] if i + 1 < len(text) else ""
        if lc:
            if c == "\n":
                lc = False
        elif bc:
            if c == "*" and nxt == "/":
                bc = False
                i += 1
        elif in_str:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == in_str:
                in_str = None
        else:
            if c == "/" and nxt == "/":
                lc = True
                i += 1
            elif c == "/" and nxt == "*":
                bc = True
                i += 1
            elif c in ("\"", "'", "`"):
                in_str = c
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    return i + 1
        i += 1
    raise ValueError("unbalanced braces")


def parse_data(data_js: str):
    def const(name):
        m = re.search(rf"const {name}=", data_js)
        return data_js[m.end():]

    comps = ast.literal_eval(const("COMPS").split("];")[0] + "]")
    whens = ast.literal_eval(const("WHENS").split("];")[0] + "]")
    uses_raw = const("USES").split("};")[0] + "}"
    uses = dict(re.findall(r"(\w+):'([^']*)'", uses_raw))
    items_txt = const("ITEMS")
    items = json.loads(items_txt[items_txt.find("["): items_txt.rfind("];") + 1])
    return comps, whens, uses, items


def parse_fx(fx_js: str) -> dict:
    out = {}
    for m in re.finditer(r"(?m)^\s*(\d+)\s*\(\s*s\b", fx_js):
        end = brace_block(fx_js, m.start())
        out[int(m.group(1))] = fx_js[m.start():end].strip()
    return out


def parse_css(fx_css: str) -> tuple:
    """Split top-level CSS into statements; map .fx<id> rules + @keyframes."""
    stmts, i, n = [], 0, len(fx_css)
    while i < n:
        while i < n and fx_css[i].isspace():
            i += 1
        if i >= n:
            break
        if fx_css.startswith("/*", i):  # comment — keep with next rule context only
            j = fx_css.find("*/", i) + 2
            i = j
            continue
        j = fx_css.find("{", i)
        if j == -1:
            break
        prelude = fx_css[i:j].strip()
        end = brace_block(fx_css, i)
        stmts.append((prelude, fx_css[i:end]))
        i = end
    keyframes, per_id = {}, {}
    for prelude, body in stmts:
        km = re.match(r"@keyframes\s+([\w-]+)", prelude)
        if km:
            keyframes[km.group(1)] = body
            continue
        for fid in {int(x) for x in re.findall(r"\.fx(\d+)(?!\d)", prelude)}:
            per_id.setdefault(fid, []).append(body)
    # attach @keyframes referenced (animation: <name> ...) by an id's rules
    result = {}
    for fid, rules in per_id.items():
        joined = "\n".join(rules)
        names = set(re.findall(r"animation(?:-name)?\s*:\s*([a-zA-Z_][\w-]*)", joined))
        result[fid] = joined + "".join(
            f"\n{k}" for name in sorted(names) if (k := keyframes.get(name)) and k not in joined
        )
    return result


def slug(en: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", en.lower()).strip("-") or "item"


def main() -> None:
    local = None
    if "--local" in sys.argv:
        local = Path(sys.argv[sys.argv.index("--local") + 1])
    blobs = {}
    for name in SITE_FILES:
        blobs[name] = (local / name).read_bytes() if local else fetch(name)
    try:
        blobs["og.png"] = (local / "og.png").read_bytes() if local else fetch("og.png")
    except Exception:
        pass

    site_dir = ROOT / "site"
    site_dir.mkdir(exist_ok=True)
    for name, blob in blobs.items():
        (site_dir / name).write_bytes(blob)

    data_js = blobs["data.js"].decode("utf-8")
    fx = parse_fx(blobs["fx.js"].decode("utf-8"))
    css = parse_css(blobs["fx.css"].decode("utf-8"))
    comps, whens, uses, items = parse_data(data_js)

    comp_label = {k: v for k, v, _ in comps}
    comp_color = {k: c for k, _, c in comps}
    when_label = dict(whens)

    for it in items:
        it["prompt_full"] = f"「{it['zh']}（{it['en']}）」動態效果：{it['prompt']}{PALETTE}"
        it["example"] = {
            "preview_text": it.get("txt", ""),
            "stage_background": it.get("bg", ""),
            "stage_class": f"fx{it['id']}",
            "fixed_preview_text": bool(it.get("fixed", False)),
            "live_demo": "site/index.html",
            "javascript_fx": fx.get(it["id"], ""),
            "css_fx": css.get(it["id"], ""),
            "file": f"examples/{it['comp']}/{it['id']:03d}-{slug(it['en'])}.md",
        }

    dataset = {
        "source": BASE + "/",
        "title": "Motion Library 動態收藏",
        "author_credit": "Hannah (UI/UX Designer) — see README.md",
        "count": len(items),
        "components": [{"key": k, "label": v, "color": comp_color[k]} for k, v, _ in comps],
        "timings": [{"key": k, "label": v} for k, v in whens],
        "uses": uses,
        "palette_suffix_appended_when_copying": PALETTE.strip(),
        "items": items,
    }
    (ROOT / "prompts.json").write_text(
        json.dumps(dataset, ensure_ascii=False, indent=2), encoding="utf-8")

    # ---- prompts.csv -------------------------------------------------
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["id", "zh", "en", "desc", "comp", "comp_label", "when", "when_labels",
                "tech", "style", "uses", "uses_labels", "tag", "preview_text",
                "fixed", "bg", "added", "prompt", "prompt_full", "example_file"])
    for it in items:
        w.writerow([it["id"], it["zh"], it["en"], it["desc"], it["comp"],
                    comp_label[it["comp"]], "|".join(it["when"]),
                    "|".join(when_label[x] for x in it["when"]), it["tech"],
                    it.get("style", ""), "|".join(it["uses"]),
                    "|".join(uses[x] for x in it["uses"]), it.get("tag", ""),
                    it.get("txt", ""), it.get("fixed", False), it.get("bg", ""),
                    it.get("added", ""), it["prompt"], it["prompt_full"],
                    it["example"]["file"]])
    (ROOT / "prompts.csv").write_text(buf.getvalue(), encoding="utf-8")

    # ---- prompts.md + examples/ --------------------------------------
    def entry_md(it, level=2, example_link=None):
        h = "#" * level
        lines = [
            f"{h} {it['id']:03d} · {it['zh']} — {it['en']}",
            "",
            f"{it['desc']}",
            "",
            f"- 元件 Component: {comp_label[it['comp']]} (`{it['comp']}`)",
            f"- 時機 Timing: {'、'.join(when_label[x] for x in it['when'])}",
            f"- 技術 Tech: {it['tech']}",
            f"- 情境 Uses: {'、'.join(uses[x] for x in it['uses'])}",
            f"- 風格／關鍵字 Style: {it.get('style', '')}",
            f"- 標籤 Tag: {it.get('tag', '')}",
            f"- 範例文字 Example text: 「{it.get('txt', '')}」"
            f"（預覽底色：{it.get('bg', '')}{'，固定文字' if it.get('fixed') else ''}）",
            f"- 收錄日期 Added: {it.get('added', '')}",
        ]
        if example_link:
            lines.append(f"- 完整範例 Example: [{example_link}]({example_link})")
        lines += ["", "**AI 提示詞（網站複製格式）:**", "", "```text", it["prompt_full"], "```", ""]
        return "\n".join(lines)

    md = [f"# Motion Library 動態收藏 — All {len(items)} Prompts", "",
          f"Source: {BASE}/ · Extracted with `tools/extract.py`. "
          "Prompts are shown exactly as the site's 「複製 AI 提示詞」 button copies them "
          "(raw prompt + the site's palette line). Animated examples: see `examples/` "
          "and the runnable copy in `site/`.", ""]
    for key, label, _ in comps:
        group = [it for it in items if it["comp"] == key]
        md += [f"## {label} ({key}) — {len(group)}", ""]
        for it in group:
            md.append(entry_md(it, level=3, example_link=it["example"]["file"]))
    (ROOT / "prompts.md").write_text("\n".join(md), encoding="utf-8")

    ex_root = ROOT / "examples"
    for it in items:
        path = ROOT / it["example"]["file"]
        path.parent.mkdir(parents=True, exist_ok=True)
        body = [entry_md(it, level=1), "## 範例實作 Example implementation", "",
                f"Preview stage: `<div class=\"stage {it.get('bg', '')} fx{it['id']}\">`, "
                f"preview text 「{it.get('txt', '')}」. Run it live by opening "
                "`site/index.html` (serve the folder, e.g. `python3 -m http.server`) "
                f"and searching 「{it['zh']}」.", "",
                f"### JavaScript — `FX[{it['id']}]` from `site/fx.js`", "",
                "```js", it["example"]["javascript_fx"] or "// (no FX entry found)", "```", "",
                "Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, "
                "`ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.", "",
                f"### CSS — direct `.fx{it['id']}` rules from `site/fx.css`", ""]
        if it["example"]["css_fx"]:
            body += ["```css", it["example"]["css_fx"], "```", ""]
        else:
            body += ["_No dedicated `.fx" + str(it["id"]) + "` rules — this effect is "
                     "driven by its JavaScript above and/or the shared category CSS "
                     "(class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, "
                     "`cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in "
                     "`site/fx.css`._", ""]
        body += [f"Source: {BASE}/ — item #{it['id']}", ""]
        path.write_text("\n".join(body), encoding="utf-8")

    idx = ["# Examples — animated example for every prompt", "",
           f"{len(items)} effects. Each file holds the full AI prompt, the preview "
           "settings, and the effect's own `FX[id]` JavaScript (+ its direct CSS) "
           "extracted from the site. The complete runnable demo stays in `../site/`.", ""]
    for key, label, _ in comps:
        group = [it for it in items if it["comp"] == key]
        idx += [f"## {label} ({key}) — {len(group)}", "",
                "| # | 名稱 | Name | 時機 | 技術 | 範例 |",
                "|---|------|------|------|------|------|"]
        for it in group:
            rel = it["example"]["file"].split("/", 1)[1]
            idx.append(f"| {it['id']:03d} | {it['zh']} | {it['en']} | "
                       f"{'、'.join(when_label[x] for x in it['when'])} | {it['tech']} | "
                       f"[md]({rel}) |")
        idx.append("")
    (ex_root / "README.md").write_text("\n".join(idx), encoding="utf-8")

    missing_ids = [i for i in range(1, max(it["id"] for it in items) + 1)
                   if i not in {it["id"] for it in items}]
    print(f"items={len(items)} fx={len(fx)} css_direct={len(css)}")
    print(f"missing ids on source: {missing_ids}")
    print("by comp:", dict(Counter(it["comp"] for it in items)))
    print("by tech:", dict(Counter(it["tech"] for it in items)))


if __name__ == "__main__":
    main()
