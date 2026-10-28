#!/usr/bin/env python3
"""Build the English version from translations/en.json.

Inputs : prompts.json (Chinese catalog built by tools/extract.py)
         translations/en.json (one entry per effect: desc_en, prompt_en,
         tag_en, style_en, txt_en — same id order as prompts.json)
Outputs:
  prompts_en.json / prompts_en.md / prompts_en.csv
  examples_en/<comp>/<NNN>-<slug>.md  (+ examples_en/README.md)
  site/data_en.js        ITEMS_EN for the site language toggle
  site/index.html        i18n hooks injected (toggle button, styles,
                         data_en.js + i18n.js script tags) — idempotent

The English copy format mirrors the site's Chinese one:
  "<en> (<zh>)" motion effect: <prompt_en>
  Colors: please match the website's existing theme colors and style
  yourself; do not specify any additional colors.

Run tools/extract.py first when refreshing from the source site, then this.
"""
import csv
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PALETTE_EN = ("\nColors: please match the website's existing theme colors "
              "and style yourself; do not specify any additional colors.")

COMP_EN = {"text": "Text", "button": "Button", "control": "Form · Controls",
           "card": "Cards · Groups", "media": "Images · Media",
           "shape": "Shapes · SVG", "bg": "Background · Ambience",
           "layout": "Layout · Pages", "cursor": "Cursor"}
WHEN_EN = {"enter": "Entrance", "exit": "Exit", "switch": "Switch",
           "loop": "Loop · Idle", "hover": "Hover · Click",
           "scroll": "Scroll-triggered", "drag": "Drag Gesture"}
USE_EN = {"hero": "Headline · Hero", "emph": "Emphasis",
          "data": "Numbers & Data", "bg": "Background Decoration",
          "trans": "Transitions", "logo": "Logo · Brand",
          "ui": "UI Interaction", "scroll": "Scroll Effects",
          "app": "App Interface"}


def slug(en: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", en.lower()).strip("-") or "item"


def main() -> None:
    data = json.loads((ROOT / "prompts.json").read_text(encoding="utf-8"))
    trans = {x["id"]: x for x in
             json.loads((ROOT / "translations/en.json").read_text(encoding="utf-8"))}
    items = data["items"]
    assert len(trans) == len(items), (len(trans), len(items))

    for it in items:
        e = trans[it["id"]]
        it["desc_en"] = e["desc_en"]
        it["prompt_en"] = e["prompt_en"]
        it["tag_en"] = e["tag_en"]
        it["style_en"] = e["style_en"]
        it["txt_en"] = e["txt_en"]
        it["prompt_full_en"] = (f"\"{it['en']} ({it['zh']})\" motion effect: "
                                f"{e['prompt_en']}{PALETTE_EN}")
        it["example_en_file"] = (f"examples_en/{it['comp']}/"
                                 f"{it['id']:03d}-{slug(it['en'])}.md")

    out = {"source": data["source"], "title": "Motion Library",
           "language": "en",
           "note": "English translation of prompts.json; zh fields kept for reference.",
           "count": len(items),
           "components": [{"key": c["key"], "label": COMP_EN[c["key"]],
                           "label_zh": c["label"], "color": c["color"]}
                          for c in data["components"]],
           "timings": [{"key": t["key"], "label": WHEN_EN[t["key"]],
                        "label_zh": t["label"]} for t in data["timings"]],
           "uses_en": USE_EN, "uses": data["uses"],
           "palette_suffix_appended_when_copying_en": PALETTE_EN.strip(),
           "items": items}
    (ROOT / "prompts_en.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    # ---- CSV ----------------------------------------------------------
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["id", "en", "zh", "desc_en", "desc", "comp", "comp_en",
                "when", "when_en", "tech", "style_en", "uses", "uses_en",
                "tag_en", "preview_text_en", "fixed", "bg", "added",
                "prompt_en", "prompt_full_en", "example_en_file"])
    for it in items:
        w.writerow([it["id"], it["en"], it["zh"], it["desc_en"], it["desc"],
                    it["comp"], COMP_EN[it["comp"]], "|".join(it["when"]),
                    "|".join(WHEN_EN[x] for x in it["when"]), it["tech"],
                    it["style_en"], "|".join(it["uses"]),
                    "|".join(USE_EN[x] for x in it["uses"]), it["tag_en"],
                    it["txt_en"], it.get("fixed", False), it.get("bg", ""),
                    it.get("added", ""), it["prompt_en"], it["prompt_full_en"],
                    it["example_en_file"]])
    (ROOT / "prompts_en.csv").write_text(buf.getvalue(), encoding="utf-8")

    # ---- Markdown catalog + examples ----------------------------------
    def entry_md(it, level=2, link=None):
        h = "#" * level
        lines = [
            f"{h} {it['id']:03d} · {it['en']} — {it['zh']}", "",
            it["desc_en"], "",
            f"- Component: {COMP_EN[it['comp']]} (`{it['comp']}`)",
            f"- Timing: {', '.join(WHEN_EN[x] for x in it['when'])}",
            f"- Tech: {it['tech']}",
            f"- Uses: {', '.join(USE_EN[x] for x in it['uses'])}",
            f"- Style / keywords: {it['style_en']}",
            f"- Tag: {it['tag_en']}",
            f"- Example text: \"{it['txt_en']}\""
            f" (stage background: {it.get('bg', '')}"
            f"{', fixed text' if it.get('fixed') else ''})",
            f"- Added: {it.get('added', '')}",
        ]
        if link:
            lines.append(f"- Full example: [{link}]({link})")
        lines += ["", "**AI prompt (English copy format):**", "",
                  "```text", it["prompt_full_en"], "```", ""]
        return "\n".join(lines)

    md = [f"# Motion Library — All {len(items)} Prompts (English)", "",
          "English version of `prompts.md`, translated from the Chinese "
          "original. Animated examples: see `examples_en/` and the runnable "
          "site in `site/` (use its 中文 / EN toggle).", ""]
    for c in data["components"]:
        group = [it for it in items if it["comp"] == c["key"]]
        md += [f"## {COMP_EN[c['key']]} ({c['key']}) — {len(group)}", ""]
        for it in group:
            md.append(entry_md(it, level=3, link=it["example_en_file"]))
    (ROOT / "prompts_en.md").write_text("\n".join(md), encoding="utf-8")

    for it in items:
        path = ROOT / it["example_en_file"]
        path.parent.mkdir(parents=True, exist_ok=True)
        ex = it["example"]
        body = [entry_md(it, level=1), "## Example implementation", "",
                f"Preview stage: `<div class=\"stage {it.get('bg', '')} "
                f"fx{it['id']}\">`, preview text \"{it['txt_en']}\". Run it "
                "live by opening `site/index.html` (serve the folder, e.g. "
                "`python3 -m http.server`), switching to EN, and searching "
                f"\"{it['en']}\".", "",
                f"### JavaScript — `FX[{it['id']}]` from `site/fx.js`", "",
                "```js", ex["javascript_fx"] or "// (no FX entry found)", "```", "",
                "Helpers used by these functions (`T`, `split`, `el`, `rnd`, "
                "`chars`, `ticks`, GSAP helpers, …) are defined at the top "
                "of `site/fx.js`.", "",
                f"### CSS — direct `.fx{it['id']}` rules from `site/fx.css`", ""]
        if ex["css_fx"]:
            body += ["```css", ex["css_fx"], "```", ""]
        else:
            body += [f"_No dedicated `.fx{it['id']}` rules — this effect is "
                     "driven by its JavaScript above and/or the shared "
                     "category CSS (class prefixes such as `ly-`, `kd-`, "
                     "`bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, "
                     "`tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._", ""]
        body += [f"Source: {data['source']} — item #{it['id']}", ""]
        path.write_text("\n".join(body), encoding="utf-8")

    idx = ["# Examples (English) — animated example for every prompt", "",
           f"{len(items)} effects, translated from `examples/`. Each file "
           "holds the full English AI prompt, the preview settings, and the "
           "effect's own `FX[id]` JavaScript (+ its direct CSS). The "
           "complete runnable demo stays in `../site/` — use its EN toggle "
           "to see these in English live.", ""]
    for c in data["components"]:
        group = [it for it in items if it["comp"] == c["key"]]
        idx += [f"## {COMP_EN[c['key']]} ({c['key']}) — {len(group)}", "",
                "| # | Name | 名稱 | Timing | Tech | Example |",
                "|---|------|------|--------|------|---------|"]
        for it in group:
            rel = it["example_en_file"].split("/", 1)[1]
            idx.append(f"| {it['id']:03d} | {it['en']} | {it['zh']} | "
                       f"{', '.join(WHEN_EN[x] for x in it['when'])} | "
                       f"{it['tech']} | [md]({rel}) |")
        idx.append("")
    (ROOT / "examples_en/README.md").write_text("\n".join(idx), encoding="utf-8")

    # ---- site/data_en.js ----------------------------------------------
    slim = {str(it["id"]): {"desc": it["desc_en"], "prompt": it["prompt_en"],
                            "tag": it["tag_en"], "style": it["style_en"],
                            "txt": it["txt_en"]} for it in items}
    (ROOT / "site/data_en.js").write_text(
        "// English translations for the language toggle (tools/build_en.py "
        "from translations/en.json)\nconst ITEMS_EN="
        + json.dumps(slim, ensure_ascii=False) + ";\n", encoding="utf-8")

    # ---- inject i18n hooks into site/index.html (idempotent) ----------
    p = ROOT / "site/index.html"
    html = p.read_text(encoding="utf-8")
    if "ml-i18n-style" not in html:
        style = ("<!-- ml-i18n-style --><style>"
                 ".lang-toggle{display:inline-flex;border:1px solid var(--line);"
                 "border-radius:10px;overflow:hidden;flex:none}"
                 ".lang-toggle button{background:var(--card);color:var(--mut);"
                 "border:0;padding:10px 14px;font:inherit;font-size:14px;"
                 "font-weight:700;cursor:pointer}"
                 ".lang-toggle button.on{background:var(--fg);color:#111}"
                 "</style>")
        html = html.replace("</head>", style + "\n</head>", 1)
    if 'id="langToggle"' not in html:
        toggle = ('<div class="tools">\n    <div id="langToggle" '
                  'class="lang-toggle" role="group" aria-label="Language">'
                  '<button type="button" data-lang="zh">中文</button>'
                  '<button type="button" data-lang="en">EN</button></div>')
        html = html.replace('<div class="tools">', toggle, 1)
    if 'src="i18n.js"' not in html:
        html = html.replace('<script src="app.js"></script>',
                            '<script src="app.js"></script>\n'
                            '<script src="data_en.js"></script>\n'
                            '<script src="i18n.js"></script>', 1)
    p.write_text(html, encoding="utf-8")

    print(f"english build: {len(items)} items -> prompts_en.json/.md/.csv, "
          f"examples_en/, site/data_en.js, index.html hooks")


if __name__ == "__main__":
    main()
