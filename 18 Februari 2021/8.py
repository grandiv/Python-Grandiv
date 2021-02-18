# Python program to find the L.C.M. of two input number

# This function computes GCD
def compute_gcd(x, y):

    while(y):
        x, y = y, x % y
    return x

# This function computes LCM
def compute_lcm(x, y):
    lcm = (x*y)//compute_gcd(x,y)
    return lcm

num1 = 12
num2 = 20

print("The L.C.M. is", compute_lcm(num1, num2))