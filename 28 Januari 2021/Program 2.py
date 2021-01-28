# mencari nilai faktorial dari suatu bilangan

def faktor(n):
    if n == 1:
        return n
    else: 
        return n*faktor(n-1)

bil = int(input("input bilangan: "))

if bil < 0:
    print("faktorial hanya untuk nilai positif")
elif bil == 0:
    print("faktorial 0 adalah 1")
else:
    print("faktorial dari", bil,'adalah ',faktor(bil))