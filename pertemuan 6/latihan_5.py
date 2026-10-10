from abc import ABC, abstractmethod

class Kendaraan(ABC):
    jumlah_kendaraan = 0

    def __init__(self, nama, kecepatan):
        self.nama = nama
        self.kecepatan = kecepatan
        Kendaraan.jumlah_kendaraan += 1

    @abstractmethod
    def bergerak(self):
        pass

class Mobil(Kendaraan):
    def __init__(self, nama, kecepatan):
        super().__init__(nama, kecepatan)

    def bergerak(self):
        return f"Mobil {self.nama} melaju di jalan raya dengan kecepatan {self.kecepatan} km/jam."

class Motor(Kendaraan):
    def __init__(self, nama, kecepatan):
        super().__init__(nama, kecepatan)

    def bergerak(self):
        return f"Motor {self.nama} melaju di jalan raya dengan kecepatan {self.kecepatan} km/jam."

mobil1 = Mobil("Toyota Avanza", 100)
mobil2 = Mobil("Honda Civic", 140)
mobil3 = Mobil("Mitsubishi Pajero", 120)

motor1 = Motor("Yamaha NMAX", 90)
motor2 = Motor("Honda Beat", 70)
motor3 = Motor("Kawasaki Ninja", 150)

print(mobil1.bergerak())
print(mobil2.bergerak())
print(mobil3.bergerak())

print(motor1.bergerak())
print(motor2.bergerak())
print(motor3.bergerak())

print(f"Total kendaraan: {Kendaraan.jumlah_kendaraan}")
