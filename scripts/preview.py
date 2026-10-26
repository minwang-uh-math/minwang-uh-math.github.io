"""Render the personal pages for local design preview without a Jekyll installation.

Install python-liquid, markdown and PyYAML first. This does not replace a Jekyll
production build; it previews the academic layout and its current page content.
"""
from pathlib import Path
import datetime
import functools
import http.server
import json
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
for deps in (ROOT / 'local/preview-deps', Path('/tmp/minwang-preview-libs')):
    if deps.exists():
        sys.path.insert(0, str(deps))
try:
    import liquid
    import markdown
    import yaml
except ImportError:
    sys.exit('Install preview dependencies: python3 -m pip install --target local/preview-deps python-liquid markdown PyYAML')

OUT = ROOT / 'local/preview'
OUT.mkdir(parents=True, exist_ok=True)

def include_syntax(source):
    return re.sub(r'{%\s*include\s+([\w./-]+)\s*%}', r"{% include '\1' %}", source)

includes = {p.name: include_syntax(p.read_text()) for p in (ROOT / '_includes').glob('*.html')}
env = liquid.Environment(loader=liquid.DictLoader(includes))
site = yaml.safe_load((ROOT / '_config.yml').read_text())
site['time'] = datetime.datetime.now(datetime.timezone.utc)
site['static_files'] = [{'path': '/' + str(p.relative_to(ROOT))} for p in (ROOT / 'images').iterdir() if p.is_file()]
site['data'] = {}
for p in (ROOT / '_data').iterdir():
    if p.suffix == '.json':
        site['data'][p.stem] = json.loads(p.read_text())
    elif p.suffix in ('.yml', '.yaml'):
        site['data'][p.stem] = yaml.safe_load(p.read_text())
env.add_filter('relative_url', lambda path: site.get('baseurl', '') + str(path))
env.add_filter('absolute_url', lambda path: site['url'] + site.get('baseurl', '') + str(path))
layout = env.from_string(include_syntax((ROOT / '_layouts/academic.html').read_text()))
for p in (ROOT / '_pages').iterdir():
    source = p.read_text()
    parts = re.split(r'^---\s*$', source, maxsplit=2, flags=re.MULTILINE)
    if len(parts) != 3:
        continue
    page = yaml.safe_load(parts[1])
    if page.get('published') is False or page.get('layout') != 'academic':
        continue
    page['url'] = page['permalink']
    body = env.from_string(include_syntax(parts[2])).render(site=site, page=page)
    if p.suffix == '.md':
        body = markdown.markdown(body, extensions=['extra'])
    html = layout.render(site=site, page=page, content=body)
    route = page['url'].lstrip('/')
    target = OUT / route if route.endswith('.html') else OUT / route / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html)
for folder in ('assets/css', 'images'):
    shutil.copytree(ROOT / folder, OUT / folder, dirs_exist_ok=True)
# Remove previously generated private content from the local preview as well.
(OUT / 'files/min_cv.pdf').unlink(missing_ok=True)
(OUT / 'cv/index.html').unlink(missing_ok=True)
print('Preview rendered to', OUT, flush=True)
if '--build-only' not in sys.argv:
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(OUT))
    with http.server.ThreadingHTTPServer(('127.0.0.1', 4000), handler) as server:
        print('Open http://127.0.0.1:4000 — Ctrl+C to stop', flush=True)
        server.serve_forever()
