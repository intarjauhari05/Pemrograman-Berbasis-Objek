from hitungbangun.luas import lingkaran
from hitungbangun.luas import persegi
from hitungbangun.volume import kubus
from hitungbangun.volume import tabung

while True:
    print("\n1. luas lingkaran")
    print("2. luas persegi")
    print("3. volume kubus")
    print("4. volume tabung")
    print("0. keluar")
    menu = input("masukkan pilihan: ")
    if menu == "1":
        print("luas lingkaran", lingkaran.luas())
    elif menu == "2":
        print("luas persegi", persegi.luas())
    elif menu == "3":
        print("volume kubus", kubus.volume())
    elif menu == "4":
        print("volume tabung", tabung.volume())
    elif menu == "0":
        break
    else:
        print("pilihan tidak ada")