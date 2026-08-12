# CDRomance provider for ROM Hub / ROMarr

**Status: not installable. This repository is documentation and a catalogue
entry, not a working provider.**

| Capability | Status |
|---|---|
| `search` | **Unavailable** — the whole site is behind a Cloudflare managed challenge |
| `importer` | **Unavailable** — same reason |
| `stream` | **Unavailable** — same reason |

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

## Why this is a full stop rather than a hard problem

Getting past a managed challenge means executing Cloudflare's JavaScript
challenge and carrying its clearance cookie — i.e. defeating a bot check that
the site operator deliberately turned on. That is circumvention, and this
project does not do it. The rule is the same one that made the Vimm.net work
decline to forge a `Referer` header.

It is also independently impossible inside the runtime, which is worth knowing
so nobody spends a weekend on it: an RPP v1 plugin has no JavaScript engine,
`ctx.http` cannot execute a challenge, and the cookie jar is cleared before
every request (`rom_hub/broker/fetcher.py`), so a clearance cookie could not
be carried to a second request even if one were somehow obtained.

**Recommendation: drop CDRomance from the target list.** Nothing about this is
likely to change unless the site turns the challenge off.

## Terms

Nothing here fetches, indexes or redistributes anything. This repository
records a finding.

## License

MIT — see `LICENSE`.
