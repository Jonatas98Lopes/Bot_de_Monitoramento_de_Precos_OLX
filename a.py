produto = 'Monitor'
with open(f'{produto}.csv', 'a', encoding='UTF-8',) as arquivo:
        arquivo.write(f'Título;Preço;Link\n')

for i in range(30):
    with open(f'{produto}.csv', 'a', encoding='UTF-8',) as arquivo:
        arquivo.write(f'{i+1};{i+2};{i+3}\n')