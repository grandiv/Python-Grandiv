def bunga(G): 
    bg = B * P
    ang = A - bg
    sisa = P - ang
    print ("----------------------------------------")
    print ("Besarnya bunga adalah ", bg)
    print ("Besarnya angsuran adalah ", ang)
    print ("Besarnya sisa pinjaman adalah ", sisa)
    print ("----------------------------------------")
    print ("Program ini belum dapat menghitung angsuran/bunga/sisa ke n secara otomatis. Sehingga user perlu input manual satu persatu sebanyak G")
    print ("----------------------------------------")
        
# B = %Bunga (input bukan 70% namun 0.7)
# P = Pinjaman
# A = Anuitas
# bg = Banyaknya bunga
# ang = Banyaknya angsuran
# sisa = Banyaknya sisa pinjaman

G = int(input("Akan dilunasi dalam: "))
if G < 0:
    print("Error")
elif G == 0: 
    print("Error")

i = 1
while i <= G: 
    
    B = float(input("Masukkan bunga (bentuk desimal): "))
    P = float(input("Masukkan pinjaman: "))
    A = float(input("Masukkan besar anuitas: "))
    print(bunga(G))
    i += 1