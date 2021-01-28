# mencari nilai penjumlahan dari nilai asli suatu bilangan

def penjumlahan(n):
    if n<= 1:
        return n
    else:
        return n + penjumlahan(n-1)

bil = int(input("input bilangan: "))

if bil < 0:
    print("Masukkan bilangan positif: ")
else: 
    print("Penjumlahan dari nilai asli", bil,"adalah", penjumlahan(bil))