class murid: 
    '''Dasar kelas untuk semua murid'''
    jumlah_murid = 0

    def __init__(self, nama, umur, tingkatsabuk):
        self.nama = nama
        self.umur = umur
        self.tingkatsabuk = tingkatsabuk
        murid.jumlah_murid += 1

    def tampilkan_jumlah(self):
        print("Total murid: ", murid.jumlah_murid)

    def tampilkan_profil(self):
        print("Nama :",self.nama)
        print("Umur :",self.umur)
        print("Tingkat Sabuk :",self.tingkatsabuk)

#membuat objek pertama dari kelas karyawan
murid1 = murid("David", 17, "Sabuk Hitam")
#membuat objek kedua dari kelas karyawan
murid2 = murid("Kevin", 26, "Sabuk Putih")
#membuat objek ketiga dari kelas karyawan
murid3 = murid("Seto", 39, "Sabuk Cokelat")

murid1.tampilkan_profil()
murid2.tampilkan_profil()
murid3.tampilkan_profil()

print("Total murid: ", murid.jumlah_murid)