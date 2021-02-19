import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Criar instância do navegador
browser = webdriver.Chrome(ChromeDriverManager().install())# NÃO browser = webdriver.Chrome()

# Criar instância do navegador
#browser = webdriver.Chrome() -> used browser = webdriver.Chrome(ChromeDriverManager().install())

# Abrir a página do Google
browser.get("https://www.facebook.com/MSNBrasil/")

# Seleciono o elemento por nome 
campo_busca = browser.find_element_by_name('email')

#o que vai ser digitado no campo
campo_busca.send_keys('email@joao.hotmail.com')

# Simular o enter 
campo_busca.send_keys(Keys.ENTER)

time.sleep(10) # tempo para sair do sistema

# Fechar navegador
browser.quit()
