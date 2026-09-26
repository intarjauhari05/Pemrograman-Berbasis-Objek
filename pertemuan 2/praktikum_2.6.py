# Praktikum 2.6: Mengenal Fungsi pada Modul Random

# 2) Fungsi random()
from random import random

print("--- Langkah 2: random() ---")
for i in range(5):
    print(random())

# 3) Fungsi random() dan seed()
from random import random, seed

print("\n--- Langkah 3: random() dengan seed ---")
# seed(0)
for i in range(5):
    print(random())

# 4) Fungsi randrange()
from random import randrange

print("\n--- Langkah 4: randrange() ---")
for i in range(10):
    print(randrange(0, 6), end=',')
print()
for i in range(10):
    print(randrange(0, 6, 2), end=',')
print()

# 5) Fungsi randint()
from random import randint

print("\n--- Langkah 5: randint() ---")
for i in range(10):
    print(randint(0, 6), end=',')
print()
for i in range(10):
    print(randint(0, 6), end=',')
print()

# 6) Fungsi choice() dan sample()
from random import choice, sample

print("\n--- Langkah 6: choice() dan sample() ---")
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))