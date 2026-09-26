# Praktikum 2.9: Memanggil Entity dari Paket

# Langkah 2: Import modul alfa dari my_package dan panggil FunctionA()
import my_package.alfa

print(my_package.alfa.FunctionA())

# Langkah 4: Import modul beta dari my_package dan panggil FunctionB()
import my_package.beta

print(my_package.beta.FunctionB())

# Langkah 5: Import modul gama dengan alias gama dan panggil FunctionC()
import my_package.subpackage1.subpackageA.gama as gama

print(gama.FunctionC())

# Langkah 6: Import modul delta dengan alias delta dan panggil FunctionD()
import my_package.subpackage1.subpackageA.delta as delta

print(delta.FunctionD())

# Langkah 7: Import modul epsilon dari subpackage2 dan panggil FunctionE()
from my_package.subpackage2 import epsilon

print(epsilon.FunctionE())

# Langkah 8: Import modul zeta dari subpackage2 dan panggil FunctionF()
from my_package.subpackage2 import zeta

print(zeta.FunctionF())
