from inicializar import Inicializar
from selenium.webdriver.common.by import By
from time import sleep



# Nota:
# Vamos considerar que o produto seja sempre o mesmo por enquanto. Vamos comprar um monitor.

# Passos:

# 1. Receber o produto a pesquisar.
produto = 'Monitor'
with open(f'{produto}.csv', 'a', encoding='UTF-8',) as arquivo:
        arquivo.write(f'Título;Preço;Link\n')
# 2. Abrir o navegador.
start = Inicializar()
driver = start.get_driver()
# 3. Acessa o site: https://www.olx.com.br/estado-sp?q=NOMEDOPRODUTO -> SUBSTITUA POR MONITOR
driver.get(f'https://www.olx.com.br/estado-sp?q={produto}')
# FAÇA, ENQUANTO HOUVER PRÓXIMAS PÁGINAS PARA ACESSAR

# 4. Esperar a página carregar.
sleep(120)
# 5. Rolar a página até o fim,
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
sleep(10)
# 6. Localizar todos os nomes dos itens na página.
nomes_itens = driver.find_elements(By.XPATH, '//div[@class="sc-12rk7z2-7 kDVQFY"]//h2')
sleep(1)
# 7. Localizar todos os preços dos itens na página.
precos_itens = driver.find_elements(By.CLASS_NAME, 'm7nrfa-0.eJCbzj.sc-ifAKCX.jViSDP')
sleep(1)
# 8. Localizar todos os links dos itens na página.
links_itens = driver.find_elements(By.CLASS_NAME, 'sc-12rk7z2-1.huFwya.sc-gzVnrw.fZJfxo')
sleep(1)
# 9. Abrir a planilha
with open(f'{produto}.csv', 'a', encoding='UTF-8',) as arquivo:
# 10. Salvar os dados de nomes, preços e links.
    for nome, preco, link in zip(nomes_itens, precos_itens, links_itens):
        arquivo.write(f'{nome.text};{preco.text};{link.get_attribute("href")}\n')
# 11. Localizar o botão "Próxima página"
# proxima_pagina = driver.find_element(By.XPATH, '//span[text()="Mais anúncios"]')
# # 11. Clicar no botão "Próxima página"
# proxima_pagina.click()
