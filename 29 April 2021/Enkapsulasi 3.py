class Siswa:

    def __init__(self, nis, nama, kelas):
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas

    # Decorator 
    @property
    def nis(self):
        pass

    # Getter
    @nis.getter
    def nis(self):
        return self.__nis

    # Setter
    @nis.setter
    def nis(self, newnis):
        self.__nis = newnis
    
grandiv = Siswa(1337, "Muhammad Grandiv", "XI MIPA 5")

print(grandiv.nis)
grandiv.nis = 666
print(grandiv.nis)