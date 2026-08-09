# CODEX_HANDOFF.md

## Objective
Publish the Dyness BMS report for maximum technical search reach and AI retrievability while preserving the experimental evidence and avoiding unauthorized irreversible actions.

## Recommended repository
Public GitHub repository: `dyness-bms-behaviour`

## Phase A - Repository and public site (Codex may execute without further approval)
1. Read `AGENTS.md`, `README.md` and `metadata/publication.json`.
2. Run `python scripts/check_publication.py` and fix only publication/website issues; do not alter measured technical conclusions.
3. If this directory is not already a Git repository, initialize it and create a `main` branch.
4. If GitHub CLI is authenticated and no target repository exists, create a **public** repository named `dyness-bms-behaviour`, push `main`, and set the repository description to: `Experimental Dyness BMS balancing algorithm, CCL and charge-MOSFET behaviour - firmware 2.50-71.10.11`.
5. Enable GitHub Pages using the included `.github/workflows/pages.yml` workflow or the current supported equivalent.
6. Verify the deployed page contains the full Q&A text, PDF, raw CSV data and figures.
7. Report the live GitHub Pages URL to the author.

If repository creation or Pages enablement requires a permission/login step that cannot be completed safely, stop and tell the author exactly what UI action is required.

## Phase B - Canonical domain (requires author/domain context)
Preferred canonical URL: `https://tehnosys.ro/dyness-bms/`.

If the author controls `tehnosys.ro` and wants this URL:
1. Determine whether the existing site can host a static `/dyness-bms/` path.
2. Deploy the contents of `site/` there or configure a suitable redirect/custom-domain arrangement.
3. Do not change DNS records without explicit author approval.
4. Once the canonical URL is confirmed, update all canonical URLs, sitemap URLs, structured metadata and repository homepage consistently.

If the Tehnosys site cannot be modified, use the GitHub Pages URL as canonical instead.

## Phase C - License checkpoint (COMPLETED)
The author confirmed in the current session:

`Do you confirm publication of the report and data under CC BY 4.0?`

Answer: yes. CC BY 4.0 is now the selected license. Do not continue to final Zenodo publication until the separate final publish approval is received.

## Phase D - Zenodo DOI and definitive v1.0 (reserve DOI first)
Zenodo supports reserving a DOI before publication so that the DOI can be inserted into the file itself.

Preferred safe workflow:
1. Create a Zenodo draft as a **Technical report / Report** with the metadata in `metadata/zenodo-fields.md`.
2. Reserve a DOI but **do not publish the record yet**.
3. Obtain the reserved DOI from the author/session.
4. Run `python scripts/set_doi.py <DOI>`.
5. Insert the DOI visibly on the report title page in `report/Dyness_BMS_Balancing_Algorithm_Charge_Control_Firmware_2.50-71.10.11.docx` and regenerate the PDF. Preserve all technical content and layout.
6. Set PDF metadata Author = `Heiko Gerdes`, Title = `Dyness BMS Balancing Algorithm and Charge-Control Behaviour - Experimental Characterization, Firmware 2.50-71.10.11`, Keywords from `metadata/publication.json`, and DOI if supported by the PDF metadata workflow.
7. Replace the PDF in both `report/` and `site/assets/`.
8. Run the publication checker and visually verify the PDF.
9. Commit and push the DOI update and verify the public web page.

**STOP and request explicit author approval before pressing Zenodo Publish or calling a publish API endpoint.**

If the author explicitly provides a Zenodo API token and explicitly asks for API publication, use the current Zenodo API documentation, never commit the token, and still request a final publish confirmation.

## Phase E - Zenodo publication (explicit approval required)
After approval:
1. Upload the definitive PDF plus the three raw measurement CSVs and switch-event CSV.
2. Add the GitHub repository and canonical web page as related identifiers where supported.
3. Publish the record.
4. Verify the DOI resolves and record the final Zenodo URL.
5. Update any DOI/record URLs in the repository if necessary and push.

## Phase F - Search and AI discovery
1. Confirm `site/robots.txt` allows general crawling and specifically does not block `OAI-SearchBot`.
2. Keep GPTBot allowed if the author's goal remains to permit possible future model-training use.
3. Confirm sitemap is publicly reachable.
4. Confirm the page has canonical metadata, `TechArticle` JSON-LD, citation meta tags and the concrete Q&A section.
5. Prepare Google Search Console instructions for the author: verify the canonical site, submit the sitemap, and request indexing for the report URL.
6. Do not claim indexing is complete until verified later.

## Phase G - Community distribution (drafts are ready; posting requires explicit approval)
Use:
- `posts/victron-community.md`
- `posts/diy-solar-forum.md`

Before submission, replace DOI/canonical placeholders with the final live URLs.

**STOP before clicking Submit/Post unless the author explicitly asks Codex to post in the current session.**

## Phase H - Final verification
After publication, verify with public searches for combinations such as:
- `Dyness BMS balancing 1.5 A 30 mV`
- `Dyness CCL 0 3.5 V charge MOSFET`
- `Dyness firmware 2.50-71.10.11`
- `Dyness balancing resistor 30 mV`

Record which queries find the canonical page, GitHub and Zenodo. Do not use search absence immediately after publication as evidence of failure; indexing can take time.

## One prompt to start Codex
Paste this into Codex after opening the repository:

> Read `AGENTS.md` and `CODEX_HANDOFF.md`. Execute Phase A completely. Then continue through all non-destructive preparation steps you can perform. Stop at every explicit approval checkpoint, especially license selection, Zenodo publication, DNS changes and forum submission. Preserve all experimental conclusions and verify your work before reporting completion.
