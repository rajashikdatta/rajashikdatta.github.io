from PIL import Image, ImageFilter
import sys

IN = 'images/favicon.jpg'
OUT = 'images/favicon-silhouette.png'
SIZES = [16,32,48,96,144,180]

# Load image
im = Image.open(IN).convert('RGBA')
# Create alpha mask by simple luminance threshold after slight blur
gray = im.convert('L')
blur = gray.filter(ImageFilter.GaussianBlur(radius=1))
# compute Otsu threshold
hist = blur.histogram()
total = sum(hist)
sumB = 0
wB = 0
maximum = 0.0
sum1 = sum(i * hist[i] for i in range(256))
for i in range(256):
    wB += hist[i]
    if wB == 0:
        continue
    wF = total - wB
    if wF == 0:
        break
    sumB += i * hist[i]
    mB = sumB / wB
    mF = (sum1 - sumB) / wF
    between = wB * wF * (mB - mF) * (mB - mF)
    if between > maximum:
        level = i
        maximum = between

# apply threshold
mask = blur.point(lambda p: 255 if p > level else 0)
# optional invert if background detected as dark vs light
# attach mask as alpha
r,g,b,a = im.split()
im.putalpha(mask)
# save silhouette PNG (full size)
im.save(OUT)

# also save resized PNGs for favicons
for s in SIZES:
    out = f'images/favicon-{s}.png'
    thumb = im.resize((s,s), Image.LANCZOS)
    thumb.save(out)

print('WROTE', OUT, 'and sizes', SIZES)
