class Siswa: 

    def __init__(self, nis, nama, kelas):
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas
    
    # Getter
    def getnis(self):
        return self.__nis

    # Setter
    def setnis(self, newnis):
        self.__nis = newnis

grandiv = Siswa(1337, "Muhammad Grandiv", "XI MIPA 5")


print(grandiv.getnis())
grandiv.setnis(666)
print(grandiv.getnis())