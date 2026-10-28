# site/ — runnable copy of the original Motion Library

Verbatim snapshot of <https://kittenjam-motion-library.vercel.app/>
(fetched 2026-10-28 by `../tools/extract.py`). This is where every prompt's
animated example actually runs.

| File | Role |
|---|---|
| `index.html` | Page shell, filters, submission dialog |
| `data.js` | Taxonomies (`COMPS` / `WHENS` / `USES`) + `ITEMS` — all 327 prompts and metadata |
| `fx.js` | `FX[id]` — the animated example implementation for each effect, plus shared helpers |
| `fx.css` | Per-effect `.fx<id>` styles and shared category CSS |
| `app.js` | Card rendering, filtering, and the 「複製 AI 提示詞」 copy logic |
| `tracking.js` | Original author's Vercel Analytics opt-out helper (inert locally) |
| `og.png` | The site's social-preview image |

Run it:

```bash
cd site
python3 -m http.server 8000
# open http://localhost:8000
```

Notes:

- GSAP 3.13 and Google Fonts load from CDNs — the demo needs internet.
- The `/_vercel/insights/script.js` tag 404s outside Vercel; harmless.
- The 「我要投稿」 submission dialog still posts to the **original author's**
  FormSubmit endpoint (see the end of `app.js`). It is kept for fidelity —
  remove that section before publishing this copy anywhere of your own.
- Credit on the page itself: curated by Hannah (UI/UX Designer);
  names/descriptions are the original author's curation, previews are
  recreations for personal reference and learning.
