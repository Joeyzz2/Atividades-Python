n = int(input('Informe um número "n": '))
limite = 50
print('Você informou o nº {}.'.format(n))
print('')
print('Os números pares menores que n/2 são: ')
for numero in range(n//2):
   if numero % 2 == 0:
       print((numero), end=' ')
print('\n')
print('Os {} números ímpares maiores que n/2 são: '.format(limite))
for numero in range((n//2)+1,limite):
   if numero % 2 != 0:
       print((numero), end=' ')