# Data film
movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {
        "title": "Spider-Man: No Way Home",
        "year": 2021,
        "rating": 7.6,
        "genre": "Action",
    },
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]


# Fungsi untuk menghitung jumlah film berdasarkan genre
def count_movies_by_genre(movies):
    genre_count = {}
    for movie in movies:
        genre = movie["genre"]
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1
    return genre_count


# Fungsi untuk menghitung rata-rata rating film berdasarkan tahun rilis
def calculate_average_rating_by_year(movies):
    year_rating = {}
    count_rating = {}
    for movie in movies:
        year = movie["year"]
        rating = movie["rating"]
        if year in year_rating:
            year_rating[year] += rating
            count_rating[year] += 1
        else:
            year_rating[year] = rating
            count_rating[year] = 1
    average_rating = {
        year: year_rating[year] / count_rating[year] for year in year_rating
    }
    return average_rating


# Fungsi untuk menemukan film dengan rating tertinggi
def find_highest_rated_movie(movies):
    highest_rated_movie = max(movies, key=lambda x: x["rating"])
    return highest_rated_movie


# Fungsi untuk mencari judul film berdasarkan judul
def find_movie_by_title(movies, title):
    for movie in movies:
        if movie["title"].lower() == title.lower():
            return movie
    return None


# Tampilan menu
def display_menu():
    print("Pilih tugas yang ingin dilakukan:")
    print("1. Menghitung jumlah film berdasarkan genre")
    print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
    print("3. Menemukan film dengan rating tertinggi")
    print(
        "4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre"
    )
    print("5. Selesai")


# Fungsi utama
def main():
    while True:
        display_menu()
        choice = input("Masukkan nomor tugas (1/2/3/4/5): ")

        if choice == "1":
            genre_count = count_movies_by_genre(movies)
            print("\nJumlah Film Berdasarkan Genre:")
            print(genre_count)
        elif choice == "2":
            average_rating = calculate_average_rating_by_year(movies)
            print("\nRata-rata Rating Film Berdasarkan Tahun Rilis:")
            print(average_rating)
        elif choice == "3":
            highest_rated_movie = find_highest_rated_movie(movies)
            print("\nFilm dengan Rating Tertinggi:")
            print(f"Judul: {highest_rated_movie['title']}")
            print(f"Rating: {highest_rated_movie['rating']}")
            print(f"Tahun Rilis: {highest_rated_movie['year']}")
            print(f"Genre: {highest_rated_movie['genre']}")
        elif choice == "4":
            title = input("Masukkan judul film yang ingin dicari: ")
            movie = find_movie_by_title(movies, title)
            if movie:
                print(f"\nInformasi Film: {movie['title']}")
                print(f"Rating: {movie['rating']}")
                print(f"Tahun Rilis: {movie['year']}")
                print(f"Genre: {movie['genre']}")
            else:
                print("\nFilm dengan judul tersebut tidak ditemukan.")
        elif choice == "5":
            print("Terima kasih telah menggunakan aplikasi kami.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih nomor tugas yang benar.")


if __name__ == "__main__":
    main()
