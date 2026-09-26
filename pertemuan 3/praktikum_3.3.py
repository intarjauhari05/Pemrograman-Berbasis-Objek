# Langkah 2
# bill=9
# bil2=0
# x=bill/bil2
# print("<< End Program >>")

# Langkah 3
try:
    bill=9
    bil2=0
    x=bill/bil2
except Exception as e:
    print(e)
print("<< End Program >>")

# Langkah 4
# import math

# print(math.a)
# print("<< End Program >>")

# Langkah 5
import math

try:
    print(math.a)
except Exception as e:
    print(e)
print("<< End Program >>")

# Langkah 6
# from time import datetime
# print("<< End Program >>")

# Langkah 7
try:
    from time import datetime
except Exception as e:
    print(e)
print("<< End Program >>")

# Langkah 8
# import mymodul
# print("<< End Program >>")

# Langkah 9
try:
    import mymodul
except Exception as e:
    print(e)
print("<< End Program >>")

# Langkah 10
# list = [1, 2, 3]
# print(list[3])
# print("<< End Program >>")

# Langkah 11
try:
    list = [1, 2, 3]
    print(list[3])
except Exception as e:
    print(e)
print("<< End Program >>")

# Langkah 12
# harga = {"apel": 25000, "jeruk": 20000, "mangga": 15000}
# harga["anggur"]
# print("<< End Program >>")

# Langkah 13
try:
    harga = {"apel": 25000, "jeruk": 20000, "mangga": 15000}
    harga["anggur"]
except Exception as e:
    print(e)
print("<< End Program >>")

# Langkah 14
# list=[]
# x=max(list)
# print("<< End Program >>")

# Langkah 15
try:
    list=[]
    x=max(list)
except Exception as e:
    print(e)
print("<< End Program >>")

# Langkah 16
# text='Hallo, mari belajar eksepsi'
# print(teks)
# print("<< End Program >>")

# Langkah 17
try:
    text='Hallo, mari belajar eksepsi'
    print(teks)
except Exception as e:
    print(e)
print("<< End Program >>")

# Langkah 18
# varString = "Hello"
# varInt = 100
# print(varString + varInt)
# print("<< End Program >>")

# Langkah 19
try:
    varString = "Hello"
    varInt = 100
    print(varString + varInt)
except Exception as e:
    print(e)
print("<< End Program >>")

# Langkah 20
# with open("sample.txt", mode="r") as file:
#     print(file.read())
# print("<< End Program >>")

# Langkah 21
try:
    with open("sample.txt", mode="r") as file:
        print(file.read())
except Exception as e:
    print(e)
print("<< End Program >>")
