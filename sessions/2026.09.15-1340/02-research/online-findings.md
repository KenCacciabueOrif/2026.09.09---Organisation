# Online findings — Cycle 22

Focus: dashboard perf item 20 (split data / fetch) + item 22 (index map); file:// constraints; debounce already local.

---

## Citations

### 1. HTTP caching — MDN
- **URL:** https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching
- **Takeaway:** Separate cacheable subresources from the main HTML document so the shell can stay cacheable while data updates independently (cache-busting / distinct URLs for changing payloads). Matches refinement item 20’s “HTML cacheable, data fetched” intent.

### 2. Request.cache — MDN
- **URL:** https://developer.mozilla.org/en-US/docs/Web/API/Request/cache
- **Takeaway:** `fetch(url, { cache: … })` controls freshness vs reuse. For regenerating local dashboard data, prefer default or `no-cache` when serving over HTTP so regenerates are visible without hard-refresh theater.

### 3. Map — MDN
- **URL:** https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map
- **Takeaway:** Spec requires sublinear average access; build once `new Map(repos.map((r,i)=>[r,i]))` (or by stable key) then `.get` — replaces repeated `Array.prototype.indexOf` scans (item 22).

### 4. Array.prototype.indexOf — MDN
- **URL:** https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf
- **Takeaway:** Linear scan; fine for tiny n, but the refinement correctly flags loop-time `indexOf` as avoidable O(n²) when mapping filtered rows back to original indices.

### 5. CORS / file:// + local JSON fetch
- **URL:** https://cors-handbook.com/posts/cors-for-file-protocol/
- **Also:** https://stackoverflow.com/questions/58717906/getting-a-syntaxerror-when-trying-to-fetch-json-data-from-local-files
- **Takeaway:** Chrome (and peers) generally **block `fetch` of sibling `.json` from a `file://` page** (opaque/`null` origin). Practical mitigations: serve catalogue via localhost (`python -m http.server` / Live Preview), **or** load data via a same-directory `<script src="…">` JS data module (often works under `file://` where `fetch` does not). Plan AC must pick one and not assume silent `file://` + `fetch('.json')` success.

### 6. Debounce (context only — already implemented)
- Pattern is standard `setTimeout` clear/rearm on `input`; local HTML already uses **150 ms** on `#c-q`. No online gap to close for item 21.

---

## Implication for Cycle 22

Item **20** is the only large structural win left in 20–22, but implementers must treat **`file://` fetch failure** as a first-class risk and document verification via **HTTP serve** and/or a **script-src data module** fallback — not browser-harness-only (prior session: CDP unavailable).
