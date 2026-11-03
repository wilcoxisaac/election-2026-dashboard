# 2026 Election Live: Path to Democratic Control

A one-page, mobile-first dashboard for the November 3, 2026 U.S. midterms. It shows forecast gauges, live seat counts, a battlefield map, the Senate path to 51, and a short feed of updates. Key governor, judicial and ballot-measure races are included.

**Live site:** https://wilcoxisaac.github.io/election-2026-dashboard/

## Install on iPhone
1. Open the live site in **Safari**.
2. Tap **Share**, then **Add to Home Screen**, then **Add**.
3. It opens full-screen from its own icon, like an app.

## How updates work
- `index.html` re-reads `data.json` every 60 seconds and whenever the app comes back to the foreground. Each new item in `alerts` shows up as an on-screen alert, with an optional chime.
- A scheduled Claude task updates `data.json` about once an hour on election night, using race calls from AP and the major networks.

## Files
| File | Purpose |
|---|---|
| `index.html` | The built page (self-contained; map paths are embedded) |
| `data.json` | Live data: phase, race calls, tallies, alerts, momentum |
| `manifest.webmanifest`, `sw.js`, `*.png` | Home-screen install and offline support |
| `tools/index.src.html` | Page source with `__STATES__` / `__DATA__` placeholders |
| `tools/build.mjs` | `node tools/build.mjs` rebuilds `index.html` from the source |
| `tools/gen-map.mjs` | Generates `tools/states.json` from `us-atlas` (`npm i d3-geo topojson-client us-atlas`) |

## data.json schema (abridged)
```json
{
  "updated": "ISO time", "phase": "pre|live|final", "phaseNote": "…",
  "liveRead": {"senate": "…", "house": "…", "governors": "…"},
  "tally": {"senate": {"D":0,"R":0,"I":0}, "house": {"D":0,"R":0}, "governors": {"D":0,"R":0,"I":0}},
  "races": {"SEN-NC": {"status":"uncalled|D|R|I|runoff","reporting":0,"d":null,"r":null,"calledBy":""}},
  "alerts": [{"t":"ISO time","dir":"D|R|neutral","text":"…"}],
  "momentum": [{"date":"YYYY-MM-DD","dir":"D|R|neutral","text":"…","source":"…","url":"…"}]
}
```

This is a nonpartisan summary of published forecasts and race calls. It is not affiliated with any campaign or news organization.
