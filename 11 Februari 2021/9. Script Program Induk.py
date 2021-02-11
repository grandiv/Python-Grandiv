#import modul
import fibo

#pemanggilan fungsi pertama
print(fibo.fib(100))

#pemanggilan fungsi kedua
print(fibo.fib2(100))

#pemanggilan fungsi dengan nama lokal
fib = fibo.fib
print(fib(100))
