#!/usr/bin/env python3
from pathlib import Path
import json, sys, re

if len(sys.argv) != 2:
    raise SystemExit("Usage: python scripts/set_doi.py 10.xxxx/zenodo.xxxxx")
doi = sys.argv[1].strip()
if not doi.startswith("10."):
    raise SystemExit("DOI must start with 10.")

root = Path(__file__).resolve().parents[1]
meta_path = root / "metadata/publication.json"
meta = json.loads(meta_path.read_text(encoding="utf-8"))
meta["doi"] = doi
meta["doi_status"] = "Reserved/assigned"
meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

cff = root / "CITATION.cff"
t = cff.read_text(encoding="utf-8")
if re.search(r"(?m)^doi:\s*", t):
    t = re.sub(r"(?m)^doi:\s*.*$", f"doi: '{doi}'", t)
else:
    t = t.replace("version: 1.0.0\n", f"version: 1.0.0\ndoi: '{doi}'\n")
cff.write_text(t, encoding="utf-8")

html = root / "site/index.html"
t = html.read_text(encoding="utf-8")
t = t.replace("DOI: pending Zenodo reservation.", f"DOI: {doi}.")
t = t.replace("DOI: pending Zenodo reservation", f"DOI: {doi}")
if 'name="citation_doi"' not in t:
    t = t.replace('<meta name="citation_pdf_url"', f'<meta name="citation_doi" content="{doi}">\n<meta name="citation_pdf_url"')
# add DOI to JSON-LD if missing
needle = '"version": "1.0.0"'
if '"identifier":' not in t and needle in t:
    t = t.replace(needle, needle + f',\n  "identifier": "https://doi.org/{doi}"')
html.write_text(t, encoding="utf-8")

llms = root / "site/llms.txt"
t = llms.read_text(encoding="utf-8")
t = t.replace("DOI: pending Zenodo reservation", f"DOI: {doi}")
llms.write_text(t, encoding="utf-8")

for p in [root/'posts/victron-community.md', root/'posts/diy-solar-forum.md']:
    s = p.read_text(encoding='utf-8')
    s = s.replace('[INSERT ZENODO DOI AFTER PUBLICATION]', doi)
    s = s.replace('[INSERT AFTER ZENODO PUBLICATION]', doi)
    p.write_text(s, encoding='utf-8')

print(f"Updated text metadata with DOI {doi}.")
print("Still required: insert the DOI visibly into the DOCX/PDF title page, regenerate PDF, copy it to site/assets, and visually verify before publication.")
