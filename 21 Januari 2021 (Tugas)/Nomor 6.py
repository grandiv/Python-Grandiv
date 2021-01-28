N = int(input("Masukkan jumlah bebek: "))
M = int(input("Masukkan jumlah teman: "))

def bebek_temen(x,y):
    masing2 = int(x/y)
    sisa = x % y
    print("masing-masing", masing2)
    print("bersisa", sisa)

bebek_temen(N,M)

# Muhammad Grandiv Lava Putra
# XI MIPA 5
# 22