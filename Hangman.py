import random

def choose_word():
    words = ["python", "html", "php", "java", "javascript", "ruby", "Swift", "bash", "perl"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    while True:
        secret_word = choose_word().lower()
        guessed_letters = set()
        attempts_left = 6

        print("Selamat datang di permainan Hangman!")

        while True:
            display = display_word(secret_word, guessed_letters)
            print(f"Kata: {display}")
            print(f"Sisa kesempatan: {attempts_left}")

            if display == secret_word:
                print("Selamat! Anda berhasil menebak kata.")
                break

            if attempts_left == 0:
                print(f"Maaf, Anda kehabisan kesempatan. Kata yang benar adalah: {secret_word}")
                break

            guess = input("Tebak huruf: ").lower()

            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("Anda sudah menebak huruf ini sebelumnya. Coba lagi.")
                elif guess in secret_word:
                    print("Hore! Tebakan Anda benar.")
                    guessed_letters.add(guess)
                else:
                    print("Tebakan salah. Coba lagi.")
                    attempts_left -= 1
            else:
                print("Masukan tidak valid. Harap masukkan satu huruf.")

        play_again = input("Ingin bermain lagi? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    hangman()
