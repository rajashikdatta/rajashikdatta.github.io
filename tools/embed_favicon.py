import base64
from pathlib import Path

jpg = Path('images/favicon.jpg')
svg = Path('images/favicon.svg')
if not jpg.exists():
    print('favicon.jpg not found')
    raise SystemExit(1)

data = base64.b64encode(jpg.read_bytes()).decode('ascii')
svg_content = f'''<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <clipPath id="circleClip"><circle cx="32" cy="32" r="32"/></clipPath>
  </defs>
  <image href="data:image/jpeg;base64,{data}" x="0" y="0" width="64" height="64" preserveAspectRatio="xMidYMid slice" clip-path="url(#circleClip)" />
</svg>
'''
svg.write_text(svg_content)
print('WROTE', svg)
