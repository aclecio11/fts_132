# 1 Importar as bibliotecas:
import pytest
import time

# 2 Classes e definições:
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Selenium_Webdriver():  # A classe começa com maiuscula
    def setup_method(self, method):
        # Declarar o objeto do selenium e instancia-lo com o navegador desejado
        self.driver = webdriver.Chrome('C:/Users/aclecio11/PycharmProjects/fts_132/drivers/chrome/97/chromedriver.exe')
        self.driver.implicitly_wait(30)  # O selenium vai esperar ate 30 segundos pelos elementos
        self.driver.maximize_window()  # Maximiza a janela do navegador no teste


    # Definição do fim - Executa depois do teste:
    def teardown_method(self, method):
        # Destruir o objeto do selenium
        self.driver.quit()

    # Definição do teste:
    @pytest.mark.parametrize('termo, curso, valor',[
        ('mantis', 'Mantis', 'R$ 59,99'),               # teste1
        ('ctfl', 'Preparatório CTFL', 'R$ 199,00'),     # teste2
    ])
    def testar_comprar_curso_mantis(self, termo, curso, valor):
        self.driver.get('https://www.iterasys.com.br')  # Abre o navegador nesse endereço
        # O selenium clica na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').click()
        # O selenium apaga o texto da caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').clear()
        # O selenium escreve 'mantis' na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys(termo)
        # O selenium clica no botao da lupa:
        self.driver.find_element(By.ID, 'btn_form_search').click()
        # o selenium vai clicar no "matricule-se"
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # O selenium valida o nome do curso no carrinho
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == curso
        # O selenium valida o preço:
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == valor
