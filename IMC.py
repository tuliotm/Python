peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso/(altura**2)

if imc > 30:
  condicao = "obeso"
elif imc >= 25 and imc < 30:
  condicao = "acima do peso"
elif imc >= 18.5 and imc < 25:
  condicao = "com peso normal"
else:
  condicao = "abaixo do peso"

print(f"O seu Índice de Massa Corporal é de {imc:0.2f} kg/m² e você está {condicao}.")