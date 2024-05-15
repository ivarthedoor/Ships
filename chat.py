import random

# Funkcja do tworzenia planszy
def create_board(size):
    board = []
    for _ in range(size):
        row = ["O"] * size
        board.append(row)
    return board

# Funkcja do wyświetlania planszy
def display_board(board):
    size = len(board)
    print("  " + " ".join([str(i) for i in range(size)]))
    for i in range(size):
        print(str(i) + " " + " ".join(board[i]))

# Funkcja do losowania pozycji statku
def generate_ship_location(board, ship_size):
    size = len(board)
    horizontal = random.choice([True, False])
    if horizontal:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - ship_size)
    else:
        x = random.randint(0, size - ship_size)
        y = random.randint(0, size - 1)
    return (x, y, horizontal)

# Funkcja do umieszczania statku na planszy
def place_ship(board, ship_size):
    x, y, horizontal = generate_ship_location(board, ship_size)
    size = len(board)
    if horizontal:
        for i in range(ship_size):
            board[x][y + i] = "S"
    else:
        for i in range(ship_size):
            board[x + i][y] = "S"

# Funkcja do sprawdzania trafienia
def check_hit(board, x, y):
    if board[x][y] == "S":
        board[x][y] = "X"
        return True
    else:
        return False

# Funkcja główna gry
def main():
    board_size = 5
    num_ships = 3
    ship_size = 3

    board = create_board(board_size)

    # Umieszczanie statków
    for _ in range(num_ships):
        place_ship(board, ship_size)

    # Gra
    while True:
        display_board(board)
        guess_x = int(input("Podaj wiersz (0-{}): ".format(board_size - 1)))
        guess_y = int(input("Podaj kolumnę (0-{}): ".format(board_size - 1)))

        if guess_x < 0 or guess_x >= board_size or guess_y < 0 or guess_y >= board_size:
            print("Niepoprawne współrzędne!")
            continue

        if check_hit(board, guess_x, guess_y):
            print("Trafiony!")
        else:
            print("Pudło!")

        # Sprawdzenie, czy wszystkie statki zostały zatopione
        if all(all(cell != "S" for cell in row) for row in board):
            print("Gratulacje! Wszystkie statki zatopione!")
            break

if __name__ == "__main__":
    main()