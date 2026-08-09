# AI and search discovery intent

The author's goal is for concrete Dyness BMS questions to find this report and for AI search/retrieval systems to be able to cite it.

Implementation choices in this package:

- The canonical publication is a normal static HTML page, not PDF-only.
- Important facts are repeated as self-contained question/answer sections.
- `robots.txt` permits general crawling and explicitly allows `OAI-SearchBot`.
- GPTBot is not blocked because the author also wants the report eligible for possible future AI training use.
- The page includes `TechArticle` JSON-LD, scholarly `citation_*` meta tags, canonical URL, sitemap, visible author, firmware version and downloadable evidence.
- `llms.txt` is included as an optional machine-readable convenience, but the HTML page is the primary discovery surface.
- Raw CSV evidence is public alongside the report.
