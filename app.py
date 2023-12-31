from Settings.inicializar import Inicializar
from Interfaces_Graficas.produto import Produto
from Interfaces_Graficas.encerramento import Fim
from Interfaces_Graficas.excecao import Erro
from selenium.webdriver.common.by import By
from Settings.caminho import salvar_arquivo_csv
from time import sleep


def verifica_variavel_vazia(nome, preco, link):
    """ Verifica se as variáveis estão sem texto ou nulas. Caso uma delas esteja nessa condição, devolve 'True'

        Recebe 3 variáveis do tipo string como argumento.
    """
    variaveis = [nome, preco, link]
    for variavel in variaveis:
        if variavel == '' or variavel == None:
            return True
    return False


def filtra_caractere_nao_numericos(valor):
    """
        Separa o cifrão '$' do valor finaceiro. Caso exista um ponto '.' entre os caracteres da variável, será removido.

        Recebe uma variável do tipo String como argumento.
    """
    valor = valor.split('$')[1].strip()
    caracateres = list(valor)
    for caracatere in caracateres:
        if caracatere == '.':
            caracateres.remove(caracatere)
    valor = "".join(caracateres)
    return valor


interface_produto = Produto()
produto = interface_produto.values["produto"]

start = Inicializar()
driver = start.get_driver()
try:
    driver.get(f'https://www.olx.com.br/estado-sp?q={produto}')
    sleep(30)
    sem_anuncios = driver.find_element(By.XPATH, '//h3[text()="Ops! Nenhum anúncio foi encontrado."]')
except:
    salvar_arquivo_csv(produto, 'Título;Preço;Link\n')
    habilitar_cookies = driver.find_element(By.ID, 'cookie-notice-ok-button')
    sleep(1)
    habilitar_cookies.click()
    sleep(1)
    while True:
        sleep(30)
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(30)
        driver.execute_script("window.scrollBy(0, -1100);")
        
        nomes_itens = driver.find_elements(By.XPATH, '//div[@class="sc-12rk7z2-7 kDVQFY"]//h2')
        sleep(1)
        
        precos_itens = driver.find_elements(By.CLASS_NAME, 'm7nrfa-0.eJCbzj.sc-ifAKCX.jViSDP')
        sleep(1)
        
        links_itens = driver.find_elements(By.CLASS_NAME, 'sc-12rk7z2-1.huFwya.sc-gzVnrw.fZJfxo')
        sleep(1)
        
        # with open(f'{produto}.csv', 'a', encoding='UTF-8',) as arquivo:
        
        for nome, preco, link in zip(nomes_itens, precos_itens, links_itens):
            nome = nome.text.strip()
            preco = preco.text.strip()
            link = link.get_attribute("href").strip()
            variaveis_vazias = verifica_variavel_vazia(nome, preco, link)
            if variaveis_vazias:
                continue
            preco = filtra_caractere_nao_numericos(preco)
            salvar_arquivo_csv(produto, f'{nome};{preco};{link}\n')
            
        sleep(1)
        driver.execute_script("window.scrollBy(0, -1300);")
        sleep(1)
        try:
            proxima_pagina = driver.find_element(By.CLASS_NAME, 'sc-248j9g-1.QtOQI.sc-gzVnrw.fZJfxo')
            proxima_pagina.click()
        except:
            break
    fim = Fim()

else:
    erro = Erro()