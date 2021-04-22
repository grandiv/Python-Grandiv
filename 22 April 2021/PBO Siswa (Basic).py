class siswa: 
    #class variable
    jumlah_siswa = 0
    #konstruktor
    def __init__(self, inputnama, inputkelas, inputalamat, inputnilai): 
        self.nama = inputnama
        self.kelas = inputkelas
        self.alamat = inputalamat
        self.nilai = inputnilai
        siswa.jumlah_siswa =+ 1

    #methode
    def viewSiswa (self):
        print("----------------------")
        print("Data Siswa")
        print("Nama : ", self.nama)
        print("Kelas : ", self.kelas)
        print("Alamat : ", self.alamat)
        print("----------------------")

    def viewNilai(self):
        print("Data Nilai")
        print("Nama : ", self.nama)
        for nilai in self.nilai:
            print("Nilai : ", nilai)
        print("----------------------")

    def viewKeterangan(self):
        print("Keterangan")
        print("Nama : ", self.nama)
        print("Kelas : ", self.kelas)
        rata = sum(self.nilai)/len(self.nilai)
        print("Rata-rata : ", rata)
        if rata >= 75:
            keterangan = "Lulus"
        else:
            keterangan = "Tidak lulus"
        print("Keterangan : ", keterangan)
        print("----------------------")

#instansiasi objek
siswa1 = siswa("Ali", "XI MIPA 1", "Jakarta", [89,67,85,47])
siswa2 = siswa("Dedi", "XII MIPA 2", "Solo", [89,97,85,87])

#pemanggilan objek siswa 1
siswa1.viewSiswa()
siswa1.viewNilai()
siswa1.viewKeterangan()
print("Jumlah siswa: ", siswa.jumlah_siswa)
#pemanggilan objek siswa 2
siswa2.viewSiswa()
siswa2.viewNilai()
siswa2.viewKeterangan()
print("Jumlah siswa: ", siswa.jumlah_siswa)