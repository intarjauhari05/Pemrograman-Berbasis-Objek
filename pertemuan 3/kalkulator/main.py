from kalkulator import tambah, kurang, kali, bagi

def lanjut():
    if input("\nHitung lagi? (y/n): ") == "n":
        exit()

while True:
    print("=== KALKULATOR ===")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Error: Input harus berupa angka!")
        continue
    try:
        pilihan = input("pilih operasi: ")
        if pilihan == "1":
            print("Hasil: ", tambah(a, b))
            lanjut()
        elif pilihan == "2":
            print("Hasil: ", kurang(a, b))
            lanjut()
        elif pilihan == "3":
            print("Hasil: ", kali(a, b))
            lanjut()
        elif pilihan == "4":
            try:
                print("Hasil: ", bagi(a, b))
                lanjut()
            except ZeroDivisionError:
                print("Error: Tidak dapat membagi dengan nol!")
                lanjut()
        # else:
        #     print("Error: Pilihan operasi tidak tersedia")
        #     lanjut()
    except KeyError:
        raise print("Error: Pilihan operasi tidak tersedia")
    except ValueError:
        raise print("Error: Input harus berupa angka")
        lanjut()