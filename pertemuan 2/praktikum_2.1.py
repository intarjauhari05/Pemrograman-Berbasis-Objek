# Praktikum 2.1: Mengenal Cara Import Modul

# 2) Import modul math
import math

# 3) Import modul sys
import sys

# 4) Import math dan sys secara bersamaan
import math, sys

# 5) Memanggil konstanta pi dari modul math
print("--- Langkah 5: math.pi ---")
print(math.pi)

# 6) Memanggil konstanta lainnya (e, inf, nan, tau)
print("\n--- Langkah 6: Konstanta e, inf, nan, tau ---")
print("e   :", math.e)
print("inf :", math.inf)
print("nan :", math.nan)
print("tau :", math.tau)

# 7) Memanggil fungsi sin(pi / 2)
print("\n--- Langkah 7: math.sin(math.pi / 2) ---")
print(math.sin(math.pi / 2))

# 8) Fungsi dan variabel buatan sendiri tanpa modul
print("\n--- Langkah 8: Fungsi sin buatan sendiri ---")
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14
print(sin(pi / 2))
