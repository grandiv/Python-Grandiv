from math import radians, sin, cos, tan
print ("Menentukan nilai sin dan cos dari 0,30,60 - 360 derajat")
print("sudut","\t","sin","\t","cos","\t","tan")
for i in range (0,361,30):
    a=radians (i)
    b=sin (a)
    b=format(b,'.2f')
    c=cos (a)
    c=format(c,'.2f')
    d=tan (a)
    d=format(d,'.2f')
    print (i,"\t",b,"\t",c,"\t",d)
input("selesai")