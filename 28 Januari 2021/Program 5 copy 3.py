def konversi(x, posisi = 0):
    return int(x[-1]) * (2**posisi) + konversi(x[:-1], posisi + 1) if x != "" else 0

biner = input('input biner : ')
print(konversi(biner))