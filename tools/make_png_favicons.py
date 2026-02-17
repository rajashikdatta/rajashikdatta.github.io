from PIL import Image, ImageDraw

IN = 'images/favicon.jpg'
SIZES = [16,32,180]

im = Image.open(IN).convert('RGBA')
W,H = im.size

# create square crop centered
size = min(W,H)
left = (W - size)//2
top = (H - size)//2
box = (left, top, left+size, top+size)
sq = im.crop(box)

for s in SIZES:
    out = f'images/favicon-{s}.png'
    thumb = sq.resize((s,s), Image.LANCZOS)
    # create circular mask
    mask = Image.new('L', (s,s), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0,0,s-1,s-1), fill=255)
    thumb.putalpha(mask)
    thumb.save(out)
    print('WROTE', out)
print('DONE')
