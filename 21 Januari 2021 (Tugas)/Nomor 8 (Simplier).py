from statistics import mode
def mencari_modus(x):
    mencari_modus = mode(x)
    print("Modusnya adalah: ", mencari_modus)

while True:
    a = input("Masukkan list angka: ")
    listangka = a.split()
    mencari_modus(listangka)

# Muhammad Grandiv Lava Putra
# XI MIPA 5
# 22