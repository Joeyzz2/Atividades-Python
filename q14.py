MassaInicial = int(input("Digite o Valor da massa: "))
MassaFinal = MassaInicial
temp = 0
while(MassaFinal >= 0.5):
    MassaFinal = MassaFinal / 2
    temp = temp + 50
print("Massa inicial: {MassaInicial}")
print("Massa final: {MassaFinal:.2f}")
print("Tempo total: {temp} segundos")
tempHr = (temp/3600)
tempMm = (temp % 3600)/60
tempSg = (temp % 3600)%60
print(" O Tempo Dividido e : {tempHr:.0f} horas, {tempMm:.1f} minutos, {tempSg:.0f} segundos")