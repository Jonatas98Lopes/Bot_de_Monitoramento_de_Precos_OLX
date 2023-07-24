import os

def obter_pasta_usuario():
    return os.path.expanduser("C:\\Users\\jonat\\OneDrive\\Área de Trabalho")

def salvar_arquivo_csv(produto, conteudo):
    pasta_usuario = obter_pasta_usuario()
    caminho_arquivo_csv = os.path.join(pasta_usuario, f'{produto}.csv')

    if not os.path.exists(caminho_arquivo_csv):
        with open(caminho_arquivo_csv, 'w', encoding='UTF-8') as arquivo:
            arquivo.write(conteudo)
    else:
        with open(caminho_arquivo_csv, 'a', encoding='UTF-8') as arquivo:
            arquivo.write(conteudo)


