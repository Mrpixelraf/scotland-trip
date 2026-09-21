"""Build the full London–Skye driving report and conversation map."""
import json
import re
from pathlib import Path
import markdown

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / 'artifacts/driver-plan'
geo = json.loads((APP / 'geography.json').read_text())
fragment = (APP / 'map.html').read_text().replace('__DRIVER_GEO__', json.dumps(geo, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/'))
assert len(fragment.encode()) < 1_000_000
(APP / 'full-drive-map.html').write_text(fragment)
report = (ROOT / 'planning/personal-driving-plan.md').read_text()
body = markdown.markdown(report, extensions=['tables'])
body = body.replace('../artifacts/driver-plan/geography.json', 'https://github.com/Mrpixelraf/scotland-trip/blob/main/artifacts/driver-plan/geography.json')
body = body.replace('<table>', '<div class="table-responsive"><table class="table">').replace('</table>', '</table></div>')
shell = (ROOT / 'docs/index.html').read_text().split('<body>')[0].replace('苏格兰 · 东线、西线与天空岛', '天空岛 · 完整自驾、住宿与费用')
body = re.sub(r'(<h2>全程路线与每日作息</h2>)', fragment + r'\1', body, count=1)
document = shell + '<body><div><nav><a href="./?route=skye">← 东线 / 西线 / 天空岛对比</a> · <a href="#daily">每日作息与住宿预算</a></nav><main id="daily">' + body + '</main></div></body></html>'
(ROOT / 'docs/driver.html').write_text(document)
print('Built docs/driver.html and inline map:', len(fragment.encode()), 'bytes')
