"""Build the self-contained route comparison from its editable data and view."""
import argparse
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
APP=ROOT/'artifacts/scotland-routes'
parser=argparse.ArgumentParser()
parser.add_argument('--inline-output',type=Path)
args=parser.parse_args()
payload={key:json.loads((APP/(name+'.json')).read_text()) for key,name in [('trip','trip'),('places','places'),('basemap','basemap'),('lakes','lakes'),('roads','roads')]}
fragment=(APP/'view.html').read_text().replace('__TRIP_DATA__',json.dumps(payload,ensure_ascii=False,separators=(',',':')).replace('</','<\\/'))
assert len(fragment.encode())<1_000_000
if args.inline_output:
    args.inline_output.parent.mkdir(parents=True,exist_ok=True)
    args.inline_output.write_text(fragment)
# A small independent shell for the same view; no host APIs, tokens or backend.
shell='''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="referrer" content="no-referrer"><title>苏格兰 · 东线、西线与天空岛</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23153d58'/%3E%3Cpath d='M6 25 14 8 22 23 26 14' fill='none' stroke='%23fff' stroke-width='3'/%3E%3C/svg%3E">
<style>
:root {color-scheme:light dark;--background:light-dark(#fff,#141a20);--foreground:light-dark(#152b39,#edf3f6);--muted:light-dark(#edf1f2,#273039);--muted-foreground:light-dark(#526572,#adbac3);--border:light-dark(#cad4db,#45515c);--primary:light-dark(#153d58,#dcecf4);--primary-foreground:light-dark(#fff,#153042);--card:light-dark(#f2f6f8,#25313b);--card-foreground:var(--foreground);--viz-series-1:light-dark(#176c8c,#70cde7);--viz-series-2:light-dark(#99701a,#e6bd6c);--viz-series-3:light-dark(#6f4eab,#c2a3ed);font:16px/1.6 system-ui,-apple-system,'PingFang SC',sans-serif;}
*{box-sizing:border-box}body{margin:0;background:var(--background);color:var(--foreground);padding:1.5rem}body>div{max-width:1120px;margin:auto}h2{font-size:1.6rem}h3{font-size:1.1rem}h2,h3,strong{font-weight:500}a{color:var(--viz-series-1);overflow-wrap:anywhere}button,input,select{font:inherit}button{cursor:pointer}.btn{border:1px solid var(--border);border-radius:7px;padding:.5rem .85rem;background:var(--background);color:var(--foreground)}.btn[aria-pressed=true]{background:var(--primary);color:var(--primary-foreground);border-color:var(--primary)}.btn:hover{filter:brightness(.96)}.btn-ghost{border-color:transparent}.viz-controls{display:flex;gap:.5rem;flex-wrap:wrap;margin:.75rem 0}.viz-controls>.form-label{flex:1;min-width:180px}.form-label{display:block;margin:.75rem 0 .3rem}.form-control,.form-select{display:block;width:100%;padding:.5rem .7rem;border:1px solid var(--border);border-radius:6px;color:var(--foreground);background:var(--background)}.form-check{display:flex;gap:.7rem;align-items:flex-start}.form-check input{margin-top:.45rem;width:18px;height:18px;flex-shrink:0}.text-small{font-size:.85rem}.text-muted{color:var(--muted-foreground)}hr{border:0;border-top:1px solid var(--border);margin:1.1rem 0}.card{padding:1rem;border:1px solid var(--border);border-radius:8px;background:var(--card);color:var(--card-foreground)}.viz-stat-value{font-size:2rem;font-weight:500}.tabular-nums{font-variant-numeric:tabular-nums}.table-responsive{overflow-x:auto}.table{width:100%;border-collapse:collapse}.table th,.table td{text-align:left;border-bottom:1px solid var(--border);padding:.7rem;vertical-align:top}.table th{font-weight:500}.sr-only{position:absolute;width:1px;height:1px;padding:0;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}summary{cursor:pointer}ol{padding-left:1.4rem}@media(max-width:500px){body{padding:.8rem}.table td,.table th{padding:.4rem}.btn{min-height:44px}}
</style></head><body>'''
document=shell+fragment+'</body></html>'
(APP/'index.html').write_text(document)
(ROOT/'docs/index.html').write_text(document)
(ROOT/'docs/.nojekyll').write_text('')
print('Built',APP/'index.html','fragment bytes',len(fragment.encode()))
