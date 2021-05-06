# Inheritance / Pewarisan
# Super class / Parent class
class Manusia:
    # Konstruktor
    def __init__(self, nama, jk, usia):
        self.nama = nama
        self.jk = jk
        self.usia = usia

    def info(self):
        print("Nama: {}\nJenis Kelamin: {}\nUsia: {}".format(self.nama,self.jk, self.usia))
        print("------------------------")

    def makan(self):
        print("Sedang makan nasi")
        print("------------------------")

# Sub class / Child class
class Pelajar(Manusia):
    # Konstruktor anak
    def __init__(self, nama, jk, usia, nis, nilai):
        Manusia.__init__(self, nama, jk, usia)
        self.nis = nis
        self.nilai = nilai

    def belajar(self):
        print("{} sedang belajar".format(self.nama))
        print("------------------------")

    # Metode Overriding
    def makan(self):
        print("{} sedang sarapan pagi dengan nasi".format(self.nama))
        print("------------------------")

# Sub class / Child class
class Pekerja(Manusia):
    # Konstruktor anak
    def __init__(self, nama, jk, usia, nip, gaji):
        Manusia.__init__(self, nama, jk, usia)
        self.nip = nip
        self.gaji = gaji

    def bekerja(self):
        print("{} sedang bekerja".format(self.nama))
        print("------------------------")

# Instansiasi objek
David = Pelajar("Davidian", "Laki-laki", 17, "1337", 90)
Grandiv = Pekerja("Muh Grandiv", "Laki-laki", 18, "666", 50000000)

# Pemanggilan
David.info()
David.belajar()
David.makan() # Memanggil metode anak
Grandiv.info()
Grandiv.bekerja()
Grandiv.makan() # Memanggil metode induk