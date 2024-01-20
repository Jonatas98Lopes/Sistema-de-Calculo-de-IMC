altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso / (altura ** 2)



if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso normal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 35:
    print('Obesidade Grau I')
elif imc < 40:
    print('Obesidade Grau II')
else:
    print('Obesidade Grau III')


print(f'IMC: {imc:.2f}')