import random

def main():
    print("Selamat datang di permainan Batu-Gunting-Kertas!")
    while True:
        user_choice = input("Pilih batu, gunting, atau kertas: ").lower()
        if user_choice in ['batu', 'gunting', 'kertas']:
            computer_choice = random.choice(['batu', 'gunting', 'kertas'])
            print(f"Komputer memilih: {computer_choice}")
            determine_winner(user_choice, computer_choice)
        else:
            print("Masukan tidak valid. Mohon pilih antara batu, gunting, atau kertas.")

        play_again = input("Ingin bermain lagi? (y/n): ").lower()
        if play_again != 'y':
            break

def determine_winner(player, computer):
    if player == computer:
        print("Hasil: Seri!")
    elif (player == 'batu' and computer == 'gunting') or \
         (player == 'gunting' and computer == 'kertas') or \
         (player == 'kertas' and computer == 'batu'):
        print("Anda menang!")
    else:
        print("Anda kalah!")

if __name__ == "__main__":
    main()