def ceknilai(nilai):
    if nilai % 2 == 0:
        nilai += 2
    else:
        nilai *= 2
    
    return nilai

angka = input("masukkan nilai = ")
hasil = ceknilai(int(angka))
print("hasilnya adalah {} ".format(hasil))
