my_str = 'kasur ini rusak'

my_str = my_str.casefold()

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
    print('kalimat ini adalah palindrome')
else: 
    print('kalimat ini bukan palindrome')