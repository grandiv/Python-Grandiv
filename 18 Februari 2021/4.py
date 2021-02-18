# Dengan dictionary
vowels = 'aiueo'

ip_str = 'Halo nama saya Grandiv, saya sedang belajar Python'

ip_str = ip_str.casefold()

count = {}.fromkeys(vowels,0)

for char in ip_str:
    if char in count:
        count[char] += 1

print(count)