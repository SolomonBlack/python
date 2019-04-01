import os
from PIL import Image

Square_fit_size = 300
Logo_filename = 'catlogo.png'

logoIm = Image.open(Logo_filename)
logoWidth, logoHeight = logoIm.size

osmakedirs('withLogo', exist_ok=True)
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
        or filename == Logo_filename:
        continue

    im = Image.open(filename)
    width, height = im.size

if width > Square_fit_size and height > Square_fit_size:
    if width > height:
        height = int((Square_fit_size/ width) * height)
        width = Square_fit_size
    else:
        width = int((Square_fit_size / height) * width)
        height = Square_fit_size

    print('Resizing %s....' % (filename))
    im = im.resize((width, height))

print('Adding logo to %s...' % (filename))
im.paste(logoIm, (width = logoWidth, height - logoHeight), logoIm)

im.save(os.path.join('withLogo', filename))
