import random
print('｡.｡･.｡*ﾟ+｡｡.｡･.｡*ﾟ+｡｡.｡･.｡*ﾟ+｡｡.｡･.｡*ﾟ+｡｡.｡･.｡*ﾟ+｡｡.｡･.｡*ﾟ+｡｡.｡･.')
print(f'Welcome to Guess the number game!\n')
print(f'If you can guess the number within 5 attempts, you win!\n')
print(f'First you can choose the number range.\n')

min_number = int(input('Minimum number? '))
max_number = int(input('Max number? '))

while min_number >= max_number:
    print(f'Max number should be bigger than minimum number.\n')
    print(f'Please try again.\n')
    min_number = int(input('Minimum number? '))
    max_number = int(input('Max number? '))

random_number = random.randint(min_number, max_number)

input_number = int(input(f'please guess the number (minimum is {min_number} max is {max_number}).\n'))

count = 0

while random_number != input_number:
    if input_number < random_number:
        print('Your number is too small.')
    else:
        print('Your number is too big.')
    
    count += 1

    if count >= 5:
        print('Game over. Please try again.')
        break

    input_number = int(input(f'please guess the number again (minimum is {min_number} max is {max_number}).\n'))

else:
    if count == 0:
        print(f' ')
        print(f'You won! You guessed the number on the first try!!')
        print('ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧Congratulations ✺◟( ᐛ )◞✺ᕙ(  •̀ ᗜ •́  )ᕗ')
        print(f' ')
    else:
        print(f' ')
        print(f'You won! You only missed {count} times :D')
        print(f' ')

    print('｡.｡･.｡*ﾟ+｡｡.｡･.｡*ﾟ+｡｡.｡･.｡*ﾟ+｡｡.｡･.｡*ﾟ+｡｡.｡･.｡*ﾟ+｡｡.｡･.｡*ﾟ+｡｡.｡･.')