class Hitung:
    def jumlah(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b

hitung1 = Hitung()
print("Penjumlahan 2 angka:", hitung1.jumlah(5, 10))
print("Penjumlahan 3 angka:", hitung1.jumlah(5, 10, 15))