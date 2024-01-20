import PySimpleGUI as sg 

# Interface gráfica

def interface():

    sg.theme('Reddit')
    
    layout = [
        [
            sg.Text('Altura(em centímetros)', size=(20,1)),
            sg.Input(key='height', size=(3,1))
        ],

        [
            sg.Text('Peso(em kilos)', size=(20,1)),
            sg.Input(key='weight',  size=(3,1))
            
        ],

        [sg.Text(key='imc_category',
                 font=('', 18, 'bold'), 
                 text_color='#fba900',
                 justification='center')
        ],

        [sg.Text(key='imc',
                 font=('', 14, 'bold'), 
                 justification='center')],
                 
        [sg.Button('Calcular')]
    ]

    return sg.Window('IMC', layout=layout)


window = interface()
window.read()






""" altura = float(input("Digite sua altura: "))
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


print(f'IMC: {imc:.2f}') """