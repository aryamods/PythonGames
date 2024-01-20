def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Pembagian oleh nol."

def calculator():
    print("Selamat datang di Kalkulator Sederhana!")

    while True:
        try:
            num1 = float(input("Masukkan angka pertama: "))
            operator = input("Pilih operator (+, -, *, /): ")
            num2 = float(input("Masukkan angka kedua: "))

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Operator tidak valid. Silakan coba lagi.")
                continue

            print(f"Hasil: {result}")

            play_again = input("Ingin menggunakan kalkulator lagi? (y/n): ").lower()
            if play_again != 'y':
                break

        except ValueError:
            print("Masukan tidak valid. Harap masukkan angka.")

if __name__ == "__main__":
    calculator()