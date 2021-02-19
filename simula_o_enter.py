from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Criar instância do navegador
browser = webdriver.Chrome(ChromeDriverManager().install())# NÃO browser = webdriver.Chrome()

# Criar instância do navegador
#browser = webdriver.Chrome() -> used browser = webdriver.Chrome(ChromeDriverManager().install())

# Abrir a página do Google
browser.get('http://google.com.br/')

# Seleciono o elemento por nome 
campo_busca = browser.find_element_by_name('q')

#o que vai ser digitado no campo
campo_busca.send_keys('Joao e maria')

# Simular que o enter
campo_busca.send_keys(Keys.ENTER)

# Fechar navegador
browser.quit()
