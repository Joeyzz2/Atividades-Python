num = int(input('digite um numero: '))
for c in range(1,num ):
    if num % c == 0:
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
