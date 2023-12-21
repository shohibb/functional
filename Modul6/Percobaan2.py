# TODO 0 : Import beberapa library lain yang dibutuhkan
from PIL import Image

# TODO 1 : Buka gambar latar belakang (background) dan gambar yang ingin disisipkan (overlay)
background_image = Image.open(r"Modul6\view-umm.jpg")
overlay_image = Image.open(r"Modul6\UMM.png")


# TODO 2 : Konversi overlay image ke mode RGB (menghilangkan alpha channel)
overlay_image = overlay_image.convert("RGB")


# TODO 3 : (optional) Perkecil ukuran gambar overlay menggunakan method resize()
resize = overlay_image.resize((400, 150))

# Tentukan/Hitung koordinat tengah untuk menempatkan overlay
background_width, background_height = background_image.size
overlay_width, overlay_height = resize.size

# Hitung koordinat tengah
x_center = (background_width - overlay_width) // 2
y_center = (background_height - overlay_height) // 2

# TODO 4 : Sisipkan gambar overlay ke dalam gambar background menggunakan method paste()
background_image.paste(resize, (x_center, y_center))


# TODO 5 : Simpan gambar hasil edit
background_image.save(r"Modul6\overlay.jpg")

# TODO 6 : Tampilkan
background_image.show()
