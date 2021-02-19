from selenium import webdriver

#USAR ISSO
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(ChromeDriverManager().install())# NÃO browser = webdriver.Chrome()

# Criar instância do navegador
#firefox = webdriver.Chrome()

# Abrir a página do devmedia
browser.get('https://www.devmedia.com.br/guia/python/37024')

# Seleciono todos os elementos que possuem a class guia-topo-destaque
posts = browser.find_elements_by_class_name('guia-topo-destaque')

for post in posts:
    #mostra as coisas do acesso-mvp-topo
    post_title = post.find_element_by_class_name('acesso-mvp-topo')

    print(post_title.text)

# Fechar navegador
browser.quit()
