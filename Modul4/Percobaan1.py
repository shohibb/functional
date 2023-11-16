def perkalian(a):
    def dengan(b):
        return a * b

    return dengan


def HoF():
    fungsi_perkalian = perkalian(5)
    hasil = fungsi_perkalian(4)
    print("Hasil perkalian dengan HoF:", hasil)


HoF()


def currying():
    hasil = perkalian(5)(4)
    print("Hasil perkalian dengan Currying:", hasil)


currying()
