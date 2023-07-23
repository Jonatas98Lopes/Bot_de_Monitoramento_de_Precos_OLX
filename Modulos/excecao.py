import PySimpleGUI as sg


class Erro:

    def __init__(self):
        
        sg.theme('DarkPurple')

        layout = [
            [sg.Text('Ops! Parece que a OLX não possui este produto.', font=('Helvetica', 14), text_color=('white'))],
            [sg.Text('Tente pesquisar outro produto.', font=('Helvetica', 14), text_color=('white'))],
            [sg.Button('Ok?', button_color=('white', '#28A745'), size=(5), pad=((220, 100), 20))]
        ]

        janela = sg.Window('Produto não existente na OLX:', font='_ 14', size=(500,140)).layout(layout)

	
        self.button, self.values = janela.Read() 
        janela.close()



