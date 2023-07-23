import PySimpleGUI as sg


class Produto:

    def __init__(self):
        
        sg.theme('DarkPurple')

        layout = [
            [sg.Text('Digite o nome do produto que deseja encontrar na OLX:', font=('Helvetica', 14), text_color=('white'))],
            [sg.Input(size=(70,5), key='produto', font='_ 12')],
            [sg.Button('Pesquisar', button_color=('white', '#28A745'))]
        ]

        janela = sg.Window('Qual o nome do produto?', font='_ 14', size=(500,110)).layout(layout)

	
        self.button, self.values = janela.Read() 
        janela.close()


