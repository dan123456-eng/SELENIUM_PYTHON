import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Criar instância do navegador
browser = webdriver.Chrome(ChromeDriverManager().install())# NÃO browser = webdriver.Chrome()

# Criar instância do navegador
#browser = webdriver.Chrome() -> used browser = webdriver.Chrome(ChromeDriverManager().install())

# Abrir a página do Google
browser.get("https://blogcalculadora.blogspot.com/")

# Seleciono o elemento por link_text
campo_busca = browser.find_element_by_link_text("Compartilhar no Facebook").click()
print("Tudo certo!!!")
time.sleep(10) # tempo para sair do sistema

# Fechar navegador
browser.quit()

"""
OBS:
Compartilhar no Facebook esse é o texto que descreve o botao.

"""
