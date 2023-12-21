from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont

background = Image.open(r"Modul6\bg.jpg")
overlay = Image.open(r"Modul6\Tugas.jpg")

# background
grayscale = background.convert("L")
rotate = grayscale.rotate(30)
blur = rotate.filter(ImageFilter.BLUR)

# overlay
curr_bright = ImageEnhance.Brightness(overlay)
new_bright = 1.3
brightness = curr_bright.enhance(new_bright)

curr_contrast = ImageEnhance.Contrast(brightness)
new_contrast = 1.5
contrast = curr_contrast.enhance(new_contrast)

resize = contrast.resize((400, 400))

# coordinates
background_width, background_height = background.size
overlay_width, overlay_height = resize.size

x_coord = (background_width - overlay_width) // 2
y_coord = (background_height - overlay_height) // 2

blur.paste(resize, (x_coord, y_coord))

direktoriFont = r"Modul6/Arial.ttf"
size = 24
draw = ImageDraw.Draw(blur)
font = ImageFont.truetype(direktoriFont, size)
text = "Informatika JOSS"
text_width = draw.textlength(text, font)
text_y = (blur.height - font.size) // 1.1
text_x = (blur.width - text_width) // 2
draw.text((text_x, text_y), text, 225, font)

blur.save(r"Modul6\tugas_praktikum_enam.jpg")

blur.show()
