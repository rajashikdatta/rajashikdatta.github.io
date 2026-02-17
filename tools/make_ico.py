from PIL import Image
from pathlib import Path

IN = Path('images/favicon.jpg')
OUT = Path('images/favicon.ico')
if not IN.exists():
    print('input not found:', IN)
    raise SystemExit(1)

im = Image.open(IN).convert('RGBA')
# center-crop to square
w,h = im.size
s = min(w,h)
left = (w-s)//2
top = (h-s)//2
sq = im.crop((left, top, left+s, top+s))
# required sizes
sizes = [(16,16),(32,32),(48,48),(64,64),(128,128),(256,256)]
imgs = [sq.resize(sz, Image.LANCZOS) for sz in sizes]
# save as ico (Pillow handles multiple sizes when passed as list)
imgs[0].save(OUT, format='ICO', sizes=[(x,y) for x,y in sizes])
print('WROTE', OUT)
