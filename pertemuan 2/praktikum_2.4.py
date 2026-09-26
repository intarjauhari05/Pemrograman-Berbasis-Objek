# Praktikum 2.4: Mengenal Aliasing pada Modul

# 2) Import modul dengan alias (as m)
import math as m

print("--- Langkah 2: Memanggil melalui alias modul 'm' ---")
print(m.sin(m.pi / 2))

# 3) Import entity dengan alias masing-masing
from math import sin as sine, pi as PI

print("\n--- Langkah 3: Memanggil entity dengan alias sine dan PI ---")
print(sine(PI / 2))
