# baby-shower-website

A one-page site for Sylvia & Andrew's baby shower — Sunday, November 8, 2026 at the
Beresford Recreation Center in San Mateo. Guests enter the password `sylvia-andrew`
to see the invitation, an embedded map, calendar links, the registry, and how to RSVP.

The password gate is client-side only. It keeps the page from being casually stumbled
upon, but it isn't real security — anyone who views the page source can read the
password, so don't put anything private behind it.

## Files

| Path | What it is |
| --- | --- |
| `index.html` | The whole site — markup, styles, and the gate script |
| `assets/dumpling.png` | The dumpling, cut out of the printed invitation |
| `assets/invite.jpg` | The original printed invitation |
| `assets/baby-shower.ics` | Calendar file for Apple Calendar and Outlook |
| `assets/fonts/` | Great Vibes and Jost, self-hosted so the type sets the same on any host |
| `build_preview.py` | Bundles `index.html` into one self-contained file for sharing |

## View locally

```
python3 -m http.server 8000
```

Then open http://localhost:8000. Open `index.html` directly from disk and the map
and fonts still work, but the `.ics` download may not.

## Publish on GitHub Pages

Merge this branch into `main`, then go to **Settings → Pages**, choose
**Deploy from a branch**, pick `main` and `/ (root)`, and save. The site appears at
`https://awhlam.github.io/baby-shower-website/` within a minute or two.

## Changing the details

Everything a guest reads lives in the `<body>` of `index.html`. The date appears in
four places that must stay in sync: the invitation block, the Google Calendar link,
`assets/baby-shower.ics`, and the map/directions links.
