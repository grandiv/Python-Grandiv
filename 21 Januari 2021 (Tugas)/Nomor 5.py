def add(x, y): #fungsi penjumlahan
    return x + y
def subtract(x, y): #fungsi pengurangan
    return x - y
def multiply(x, y): #fungsi perkalian
    return x * y
def divide(x, y): #fungsi pembagian
    return x / y

print("Pilih Operasi.") # menu operasi
print("1.Jumlah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")
choice = input("Masukkan pilihan (1/2/3/4): ") #meminta input dari user
num1 = int(input("Masukkan bilangan pertama: "))
num2 = int(input("Masukkan bilangan kedua: "))
if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
    print(num1, "-",num2,"=", subtract(num1,num2))
elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Input salah")

# Muhammad Grandiv Lava Putra
# XI MIPA 5
# 22