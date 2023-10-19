import random


create_board = lambda width, height: [
    ["-" for _ in range(width + 1)] for _ in range(height)
]


def display_board(board):
    for row in board:
        print(" ".join(row))


def place_player(board, max_attempts=3):
    width = len(board[0])
    height = len(board)
    attempts = 0

    while attempts < max_attempts:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if board[y][x] == "-":
            board[y][x] = "A"
            return (x, y)
        attempts += 1

    return None


def place_goals(board, max_attempts=3):
    width = len(board[0])
    height = len(board)
    attempts = 0

    while attempts < max_attempts:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if board[y][x] == "-":
            board[y][x] = "O"
            return (x, y)
        attempts += 1

    return None


def move_player(board, x, y, dx, dy):
    width = len(board[0])
    height = len(board)
    new_x, new_y = x + dx, y + dy
    if 0 <= new_x < width and 0 <= new_y < height:
        if board[new_y][new_x] == "O":
            board[y][x] = "-"
            board[new_y][new_x] = "A"
            return new_x, new_y
        elif board[new_y][new_x] == "-":
            board[y][x] = "-"
            board[new_y][new_x] = "A"
            return new_x, new_y
        else:
            print("Anda tidak dapat bergerak ke posisi tersebut.")
    else:
        print("Anda mencoba bergerak ke luar batas permainan.")
    return x, y


def play_game(board, player_position, goals_position):
    display_board(board)
    moves = input("Masukkan urutan gerakan (ASWD): ").upper()

    for move in moves:
        if move == "W":
            player_position = move_player(board, *player_position, 0, -1)
        elif move == "A":
            player_position = move_player(board, *player_position, -1, 0)
        elif move == "S":
            player_position = move_player(board, *player_position, 0, 1)
        elif move == "D":
            player_position = move_player(board, *player_position, 1, 0)

        if player_position == goals_position:
            display_board(board)
            print("Selamat, Anda menang!")
            return

    display_board(board)
    print("Anda kalah.")
    regenerate_board = input("Coba lagi? (ya/tidak): ").lower()
    if regenerate_board == "ya":
        play_game(board, player_position, goals_position)


def main():
    print("~~ Selamat datang dipermainan board game pemrograman fungsional")
    print(
        "------------------------------------------------------------------------------------------------"
    )
    print(
        "Anda (A) dapat berjalan secra horizontal dan vertikal menuju target (O)\nGunakan keyboard ASDW untuk berjalan"
    )
    print(
        "------------------------------------------------------------------------------------------------"
    )
    print("~~ Selamat bermain ~~\n")
    width = int(input("Masukkan lebar board: "))
    height = int(input("Masukkan tinggi board: "))

    regenerate_count = (
        0  # Variabel untuk menghitung berapa kali pemain membuat ulang papan
    )

    while regenerate_count < 3:  # Memastikan jumlah ulangan tidak melebihi 3
        board = create_board(width, height)
        player_position = place_player(board)
        goals_position = place_goals(board)

        display_board(board)

        regenerate_board = input("Bikin ulang pannya? (ya/tidak): ").lower()
        if regenerate_board != "ya":
            break
        regenerate_count += 1

    if regenerate_count < 3:
        play_game(board, player_position, goals_position)


if __name__ == "__main__":
    main()
