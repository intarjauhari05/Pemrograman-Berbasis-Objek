class kendaraan():
    def __init__(self):
        self.__jenis = ''
        self.__merk = ''
        self.__nama = ''
        self.__warna = ''

    def get_atribut(self):
        print("Nama 	:", self.__nama,
              "\nMerk \t:", self.__merk,
              "\nWarna\t:", self.__warna,
              "\nJenis\t:", self.__jenis)

    def set_atribut(self, val1='', val2='', val3='', val4=''):
        self.__jenis = val1
        self.__merk = val2
        self.__nama = val3
        self.__warna = val4

kdr1 = kendaraan()
kdr1.set_atribut(val1='mobil', val2='toyota', val3='avanza', val4='hitam')
kdr1.get_atribut()

brio = kendaraan()
brio.set_atribut(val1='mobil', val4='merah')
brio.get_atribut()

vario = kendaraan()
vario.set_atribut(val2='honda', val4='hitam')
vario.get_atribut()