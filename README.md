# CDRomance provider for ROM Hub / ROMarr

**Status: no standalone RPP provider. Use the signed-in ROMarr Capture browser
extension for pages you can open in Brave/Chromium.** This repository remains
the ROM Hub catalogue record and documents why anonymous plugin HTTP cannot
serve as the transport.

| Capability | Status |
|---|---|
| ROM Hub `search` | Unavailable to anonymous `ctx.http` |
| ROMarr Capture | Implemented for detail pages; runs only on a page the operator opened |
| Browser download | Uses the site's own rendered controls and browser session |

## The finding

Every path on `cdromance.org` — including `/robots.txt`, which is normally the
one file a site keeps readable — returns:

```
HTTP/1.1 403 Forbidden
Content-Type: text/html; charset=UTF-8

<title>Just a moment...</title>
... cType: 'managed' ...
<noscript>Enable JavaScript and cookies to continue</noscript>
```

That is Cloudflare's **managed challenge**, not a rate limit and not a soft
bot score. The site serves no readable content at all to a plain HTTPS client.

Two consequences worth stating separately:

* **Its `robots.txt` could not be read**, so this survey does not even know
  what CDRomance's crawl policy *is*. That matters: a provider cannot honour a
  policy it has never seen.
* **There is no structure to report** — no listing shape, no id scheme, no
  detail-page format, and no answer to whether the site still hosts files.
  None of it was observable.

## Why this is a browser-assisted source

An automated client must not defeat Cloudflare's challenge. A person opening
the page in their normal signed-in browser is different: the browser has
already rendered the page through the site's ordinary flow. ROMarr Capture
reads that rendered page and sends the extracted catalogue row to the
operator's own ROMarr; it does not solve challenges, crawl links, or send a
request to CDRomance itself.

It remains unavailable inside the standalone RPP runtime: a plugin has no JavaScript engine,
`ctx.http` cannot execute a challenge, and the cookie jar is cleared before
every request (`rom_hub/broker/fetcher.py`), so a clearance cookie could not
be carried to a second request even if one were somehow obtained.

The Capture adapter is deliberately preview-first because its selectors have
not yet been verified against a live detail page. Open a game page, click the
ROMarr Capture icon, and check that title, platform, and size are present before
sending. A missing field is an adapter bug to fix, not a reason to discard the
source.

## Terms

The standalone provider fetches and redistributes nothing. Browser capture
indexes only metadata from a page the operator opened; it grants no rights to
download or redistribute the site's files.

## License

MIT — see `LICENSE`.
