# ESTE ARQUIVO DEVE SER USADO PARA GERAR O EXECUTÁVEL DO PROGRAMA.


from cx_Freeze import setup, Executable


settings = Executable(
    script='app.py',
    icon='assets\\icone.ico',
)

setup(
    name='Bot de Monitoramento de Preços OLX',
    version='1.0',
    description='Com este software, você pode baixar as principais informações de todos os itens de um produto que está procurando na OLX e colocá-las numa planilha.',
    author='Jonatas Lopes de Sousa',
    options= {'build_exe': {
        'include_msvcr': True
    }},
    executables=[settings]
    )