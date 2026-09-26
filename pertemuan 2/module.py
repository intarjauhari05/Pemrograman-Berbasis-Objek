# Praktikum 2.7: Modul Buatan Sendiri (module.py)

if __name__ == "__main__":
    print("Anda menjalankan module.py")
else:
    print("Anda mengimport modul")

counter = 0

def jumlahkan(list):
    hasiljml = 0
    for element in list:
        hasiljml += element
    return hasiljml
