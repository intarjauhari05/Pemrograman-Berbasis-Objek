# Langkah 2
try:
    bill=9
    bil2=0
    x=bill/bil2
except ZeroDivisionError as e:
    print(e)
print("<< End Program >>")

# Langkah 3
import math

try:
    print(math.a)
except AttributeError as e:
    print(e)
print("<< End Program >>")

# Langkah 4
try:
    from time import datetime
except ImportError as e:
    print(e)
print("<< End Program >>")

# Langkah 5
try:
    import mymodul
except ModuleNotFoundError as e:
    print(e)
print("<< End Program >>")

# Langkah 6
try:
    list = [1, 2, 3]
    print(list[3])
except IndexError as e:
    print(e)
print("<< End Program >>")

# Langkah 7
try:
    harga = {"apel": 25000, "jeruk": 20000, "mangga": 15000}
    harga["anggur"]
except KeyError as e:
    print(e)
print("<< End Program >>")

# Langkah 8
try:
    list=[]
    x=max(list)
except ValueError as e:
    print(e)
print("<< End Program >>")

# Langkah 9
try:
    text='Hallo, mari belajar eksepsi'
    print(teks)
except NameError as e:
    print(e)
print("<< End Program >>")

# Langkah 10
try:
    varString = "Hello"
    varInt = 100
    print(varString + varInt)
except TypeError as e:
    print(e)
print("<< End Program >>")

# Langkah 11
try:
    with open("sample.txt", mode="r") as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
print("<< End Program >>")
