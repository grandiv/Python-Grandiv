import random as r

def diceroll(sidenumber):
    dice = round(r.uniform(1, float(sidenumber)))
    return dice
endProgram = ""

while endProgram != "quit":
    numberofdice = int(input("Masukkan berapa kali dadu mau diputar: "))
    sidenumber = int(input("Masukkan berapa sisi dadu: "))
    x = numberofdice

    while x != 0:
        try:
            print(diceroll(sidenumber))
            x -= 1
        except: 
            print("Invalid Entry: ")

        endProgram = input("Press enter to roll again: ").lower()