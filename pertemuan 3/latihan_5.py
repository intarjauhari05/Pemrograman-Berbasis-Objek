# ==========================================================
# Latihan Bab 3: Soal 5
# Program sederhana ATM dengan fitur tarik tunai (Interaktif)
# ==========================================================

class SaldoTidakCukupError(Exception):
    pass

class NominalTidakValidError(Exception):
    pass

def tarik_tunai(saldo_saat_ini, input_nominal):
    try:
        # a. Nominal yang dimasukkan bukan angka
        try:
            nominal = float(input_nominal)
        except ValueError:
            raise ValueError("Nominal yang dimasukkan harus berupa angka!")

        # c. Nominal kurang dari atau sama dengan 0
        if nominal <= 0:
            raise NominalTidakValidError("Nominal penarikan harus lebih besar dari 0!")

        # b. Saldo tidak mencukupi
        if nominal > saldo_saat_ini:
            raise SaldoTidakCukupError(f"Saldo tidak mencukupi! Saldo saat ini: Rp {saldo_saat_ini:,.2f}")

        saldo_saat_ini -= nominal
        print(f"\n[Sukses] Penarikan sebesar Rp {nominal:,.2f} berhasil!")
        print(f"[Info] Sisa saldo Anda: Rp {saldo_saat_ini:,.2f}\n")
        return saldo_saat_ini

    except ValueError as e:
        print(f"\n[Error Input] {e}\n")
    except NominalTidakValidError as e:
        print(f"\n[Error Nominal] {e}\n")
    except SaldoTidakCukupError as e:
        print(f"\n[Error Saldo] {e}\n")
    except Exception as e:
        print(f"\n[Error Umum] Terjadi kesalahan: {e}\n")
    return saldo_saat_ini

# Program Utama ATM Interaktif
if __name__ == "__main__":
    saldo = 500000.0
    print("=== Selamat Datang di ATM Sederhana ===")
    print(f"Saldo awal Anda: Rp {saldo:,.2f}")

    while True:
        print("-" * 40)
        print("Menu:")
        print("1. Tarik Tunai")
        print("2. Cek Saldo")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ").strip()

        if pilihan == "1":
            nominal_input = input("Masukkan nominal tarik tunai: ")
            saldo = tarik_tunai(saldo, nominal_input)
        elif pilihan == "2":
            print(f"\n[Info] Saldo Anda saat ini: Rp {saldo:,.2f}\n")
        elif pilihan == "3":
            print("\nTerima kasih telah menggunakan layanan ATM!")
            break
        else:
            print("\n[Peringatan] Pilihan menu tidak valid. Silakan pilih 1, 2, atau 3.\n")
