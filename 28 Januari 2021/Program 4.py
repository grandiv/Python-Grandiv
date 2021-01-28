# menampilkan deret fibonancy (menjumlahkan suatu bilangan dari 2 bilangan sebelumnya)
# 1 2 3 5 8 13 21

def deret_fibo(n):
    if n <=1 :
        return n
    else: 
        return(deret_fibo(n-1) + deret_fibo(n-2))

jumlah_deret = int(input("Jumlah deret: "))

if jumlah_deret <= 0:
    print("Masukkan bilangan bulat positif")
else: 
    print("deret fibonanci: ")
    for i in range(jumlah_deret):
        print(deret_fibo(i))

#output
# 0 1 1 2 3 5 8 13 21 34 dst