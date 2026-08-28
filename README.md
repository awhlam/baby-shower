# baby-shower-website

A single-page site for Sylvia & Andrew's baby shower. Shows the invitation, location, date/time, and RSVP info, gated behind a simple password ("sylvia-andrew").

Note: the password gate is client-side only, meant to keep casual visitors out — it's not real security since the page source is visible to anyone who looks.

## View locally

Open `index.html` in a browser, or serve the folder:

```
python3 -m http.server 8000
```

## Deploy

Works as a static site on GitHub Pages: enable Pages for this repo (Settings → Pages → Deploy from branch → `main` / root).
