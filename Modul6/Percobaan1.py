from PIL import Image, ImageDraw, ImageFont

# TODO 1: Lakukan load image pada variabel berikut
gambarku = Image.open(r"Modul6\UMM.jpg")

# TODO 2: Ubah gambar menjadi hitam-putih
gambarBW = gambarku.convert("L")

# # TODO 3: Tambahkan text sesuai kriteria.
direktoriFont = r"Modul6/Arial.ttf"
size = 24
draw = ImageDraw.Draw(gambarBW)
font = ImageFont.truetype(direktoriFont, size)
text = "Akmal shahib maulana 2021-135"
text_width = draw.textlength(text, font)
text_y = gambarku.height - font.size  # Update untuk pemosisian tengah vertikal
text_x = (gambarku.width - text_width) // 2  # Update untuk pemosisian tengah horizontal
draw.text((text_x, text_y), text, -1, font)

# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save("Modul6\percobaan_satu.jpg")

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()
