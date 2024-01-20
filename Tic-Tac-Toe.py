import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def player_turn(board):
    while True:
        try:
            row = int(input("Masukkan nomor baris (0-2): "))
            col = int(input("Masukkan nomor kolom (0-2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                return row, col
            else:
                print("Posisi tidak valid. Coba lagi.")
        except ValueError:
            print("Masukan tidak valid. Harap masukkan angka.")

def computer_turn(board):
    available_positions = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    return random.choice(available_positions)

def main():
    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        player_symbol = 'X'
        computer_symbol = 'O'

        print("Selamat datang di permainan Tic-Tac-Toe melawan komputer!")
        print_board(board)

        for turn in range(9):
            if turn % 2 == 0:
                row, col = player_turn(board)
                board[row][col] = player_symbol
            else:
                print("Giliran Komputer:")
                row, col = computer_turn(board)
                board[row][col] = computer_symbol

            print_board(board)

            if check_winner(board, player_symbol):
                print("Selamat! Anda menang!")
                break
            elif check_winner(board, computer_symbol):
                print("Sayang sekali, Komputer menang.")
                break
            elif is_board_full(board):
                print("Permainan berakhir dengan hasil seri.")
                break

        play_again = input("Ingin bermain lagi? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()