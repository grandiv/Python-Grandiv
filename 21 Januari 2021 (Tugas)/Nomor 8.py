def modus(angka_angka):
    count = 0
    terbanyak = angka_angka[0]

    for i in angka_angka:
        flag = angka_angka.count(i)
        if flag >= count:
            count = flag
            terbanyak = i
    return(terbanyak)

while True:
    a = input("Masukkan angka angka: ")

    angka_angka = a.split()
    print("modusnya adalah :", modus(angka_angka))
    print("")

# Muhammad Grandiv Lava Putra
# XI MIPA 5
# 22