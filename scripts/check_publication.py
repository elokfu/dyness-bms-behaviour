#!/usr/bin/env python3
from pathlib import Path
import json, sys
root = Path(__file__).resolve().parents[1]
errors=[]
meta=json.loads((root/'metadata/publication.json').read_text(encoding='utf-8'))
required=[root/'README.md',root/'CITATION.cff',root/'site/index.html',root/'site/robots.txt',root/'site/sitemap.xml',root/'report/Dyness_BMS_Balancing_Algorithm_Charge_Control_Firmware_2.50-71.10.11.pdf',root/'report/dyness_balancing_cycle_projection_report_with_bleeder_hours.pdf',root/'site/assets/dyness_balancing_cycle_projection_report_with_bleeder_hours.pdf']
for p in required:
    if not p.exists(): errors.append(f"missing: {p.relative_to(root)}")
html=(root/'site/index.html').read_text(encoding='utf-8')
for term in ['2.50-71.10.11','1.5 A','1.4 A','30 mV','3.5 V','3.6 V','3.45 V','150 mV','effective discharge','16-cell','cell 16','Observed practical imbalance']:
    if term not in html: errors.append(f"site missing required term: {term}")
robots=(root/'site/robots.txt').read_text(encoding='utf-8')
if 'OAI-SearchBot' not in robots: errors.append('robots.txt does not explicitly mention OAI-SearchBot')
if 'Disallow: /' in robots: errors.append('robots.txt contains a global Disallow: /')
for f in ['dyness-balancer-2026-08-09T06-26-03(4).csv','dyness-balancer-2026-08-09T06-26-03(5).csv','dyness-balancer-2026-08-09T10-21-53.csv']:
    if not (root/'site/assets/data'/f).exists(): errors.append(f"site data missing: {f}")
if errors:
    print('PUBLICATION CHECK FAILED')
    for e in errors: print('-',e)
    sys.exit(1)
print('PUBLICATION CHECK PASSED')
print('DOI:', meta.get('doi') or 'not yet reserved')
print('License status:', meta.get('license_status'))
