kelime = input('myword: ')
kelimeLen = len(kelime)

is_palindrome = True

for i in range(kelimeLen // 2):
    if kelime[i] != kelime[kelimeLen - i - 1]:
        is_palindrome = False 
        break 

if is_palindrome:
    print("bir palindromdur.")
else:
    print("bir palindrom değildir.")
