from PIL import Image, ImageEnhance

img = Image.open(r"Modul6\view-umm.jpg")

# brightness
curr_brig = ImageEnhance.Brightness(img)
new_brig = 1.5
brightness = curr_brig.enhance(new_brig)

curr_cont = ImageEnhance.Contrast(brightness)
new_count = 1.5
contrast = curr_cont.enhance(new_count)


contrast.save(r"Modul6\brightness_contrast_image.jpg")

merged_image = Image.new("RGB", (img.width * 2, img.height))
merged_image.paste(img, (0, 0))
merged_image.paste(contrast, (img.width, 0))

merged_image.show()
