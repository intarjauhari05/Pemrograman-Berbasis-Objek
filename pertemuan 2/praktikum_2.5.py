# Praktikum 2.5: Mengenal Fungsi pada Modul Math

# 2) Menampilkan semua entity pada modul math dengan dir()
import math

print("--- Langkah 2: dir(math) ---")
print(dir(math))

# 3) Import konstanta e, pow(), log(), exp()
from math import e, exp, log

print("\n--- Langkah 3: Operasi pemangkatan dan logaritma ---")
print(pow(e, 1))
print(pow(2, 2))
print(log(e, e))
print(exp(log(e)))
print(exp(2 * log(2)))
print(exp(0))

# 4) Relasi kesamaan (Boolean)
print("\n--- Langkah 4: Relasi kesamaan ---")
print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

# 5) Fungsi ceil(), floor(), trunc()
from math import ceil, floor, trunc

x = 1.4
y = 2.6

print("\n--- Langkah 5: Pembulatan (floor, ceil, trunc) ---")
print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))
