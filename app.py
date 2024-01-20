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

        [sg.Text(key='invalid_values', text_color='red')],

        [sg.Text(key='imc_category', font=('', 18, 'bold'), 
            justification='center')
        ],

        [sg.Text(key='imc',
                 font=('', 14, 'bold'), 
                 justification='center')],

        [sg.Button('Calcular')]
    ]

    return sg.Window('IMC', layout=layout)


def contem_apenas_numeros(texto: str) -> bool:
    return texto.isdigit()

def eValor_numerico(texto: str) -> bool:
    virgula = contem_apenas_numeros("".join(texto.split(",")))
    ponto = contem_apenas_numeros("".join(texto.split(".")))
    return (virgula or ponto)
        

window = interface()
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED: break

    else:
        window['invalid_values'].update('')
        window['imc_category'].update('')
        window['imc'].update('')

        altura = values['height'].strip()
        peso = values['weight'].strip()
        
        if eValor_numerico(altura) and eValor_numerico(peso):


            altura = float(altura) / 100
            peso = float(peso)
            imc = peso / (altura ** 2)


            if imc < 18.5:
                window['imc_category'].update(text_color='pink')
                window['imc_category'].update('Abaixo do peso')

            elif imc < 25:
                window['imc_category'].update(text_color='green')
                window['imc_category'].update('Peso normal')

            elif imc < 30:
                window['imc_category'].update(text_color='orange')
                window['imc_category'].update('Sobrepeso')

            elif imc < 35:
                window['imc_category'].update(text_color='red')
                window['imc_category'].update('Obesidade Grau I')

            elif imc < 40:
                window['imc_category'].update(text_color='red')
                window['imc_category'].update('Obesidade Grau II')
    
            else:
                window['imc_category'].update(text_color='red')
                window['imc_category'].update('Obesidade Grau III')
    

            window['imc'].update(f'IMC: {imc:.2f}') 

        else: 
            window['invalid_values'].update('ALTURA OU PESO INVÁLIDOS.')







