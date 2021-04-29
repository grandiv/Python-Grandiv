# Encapsulation
class Hero:
    jumlah = 0

    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    # Getter
    def getname(self):
        return self.__name
    
    def gethealth(self):
        return self.__health

    # Setter
    def diserang(self, attserang):
        self.__health -= attserang

# Instansiasi objek
lina = Hero("Lina", 10)

# Cetak privat
print(lina.getname())