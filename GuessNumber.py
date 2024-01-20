import random

def main():
    print("Selamat datang di permainan Tebak Angka!")

    while True:
        target_number = random.randint(1, 100)

        while True:
            try:
                user_guess = int(input("Tebak angka (antara 1 dan 100) atau ketik 'exit' untuk keluar: "))

                if 1 <= user_guess <= 100:
                    if user_guess == target_number:
                        print(f"Selamat! Anda menebak dengan benar. Angka yang dicari adalah {target_number}.")
                        break
                    elif user_guess < target_number:
                        print("Tebakan terlalu rendah. Coba lagi.")
                    else:
                        print("Tebakan terlalu tinggi. Coba lagi.")
                else:
                    print("Masukan tidak valid. Harap masukkan angka antara 1 dan 100.")
            except ValueError:
                user_input = input("Masukan tidak valid. Ketik 'exit' untuk keluar atau tebak angka lagi: ")
                if user_input.lower() == 'exit':
                    break
                else:
                    continue

        play_again = input("Ingin bermain lagi? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()