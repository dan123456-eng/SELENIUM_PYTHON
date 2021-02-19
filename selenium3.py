from selenium import webdriver

#USAR ISSO
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(ChromeDriverManager().install())# NÃO browser = webdriver.Chrome()

# Criar instância do navegador
#firefox = webdriver.Chrome()

# Abrir a página 
browser.get('https://www.devmedia.com.br/guia/python/37024')

# Seleciono todos os elementos que possuem  a footer-content
teste = browser.find_elements_by_class_name('footer-content')

for i in teste:
    print(i.text)

# Fechar navegador
browser.quit()
