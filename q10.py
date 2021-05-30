meses = ['nome',"Janeiro","Fevereiro","Março","Abril","Maio","Junho" ,
"Julho" , "Agosto" ,"Setembro" , "Outubro" , "Novembro" ,"Dezembro"]
valor = int(input("Digite um valor:"))
if valor > 0 and valor <= 12:
  print(f"Mês de {meses[valor]}")
else:
  print("Valor invalido: Maior que 12 ou menor que 1")