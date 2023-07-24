import PySimpleGUI as sg


class Fim:

    def __init__(self):
        
        sg.theme('DarkPurple')

        layout = [
            [sg.Text('O programa foi finalizado.. Uma planilha foi gerada para você.', font=('Helvetica', 14), text_color=('white'))],
            [sg.Button('Ok', button_color=('white', '#28A745'), size=(10, 10), pad=((220, 100), 20))]
        ]

        janela = sg.Window('Programa finalizado.', font='_ 14', size=(550,105)).layout(layout)

	
        self.button, self.values = janela.Read() 
        janela.close()



