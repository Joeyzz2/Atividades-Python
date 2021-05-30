def fatora(n):
   fatorial = n
   next = n
   while next > 1:
       fatorial = fatorial * (next - 1)
       next -= 1
   print('O fatorial de {} é {}.'.format(n, fatorial))
def conta(n):
   soma = 0
   for numero in range(1, n + 1):
       soma += numero
   print('A soma de todos os números entre 1 e {} é {}.'.format(n, soma))
while True:
   n = int(input('Insira um número: '))
   if n <= 0:
       print('Número menor ou igual a zero inserido. Fim do programa')
       break
   else:
       if n < 7:
           fatora(n)
       if n >= 7:

           conta(n)
   print()