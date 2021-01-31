# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 08:45:21 2021

@author: bruna
"""

from selenium import webdriver
from time import sleep
import pandas as pd

#atribuir os parâmetros da busca no LinkedIn
vaga = input('Escreva a vaga que deseja pesquisar: ')
local = input('Escreva a cidade que deseja pesquisar a vaga: ')

chrome_path = 'D:\\Documentos\\Awari_PREP\\Chromedriver.exe'
driver = webdriver.Chrome(chrome_path)
driver.get('https://br.linkedin.com/jobs/search?keywords=&location=Curitiba%2C%20Paran%C3%A1%2C%20Brasil&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0')
driver.implicitly_wait(10)
    
#pesquisando palavras chaves da vaga
botao_vaga = '/html/body/header/nav/section/section[2]/form/section[1]/input'
busca_vaga = driver.find_element_by_xpath(botao_vaga)
busca_vaga.click()
busca_vaga.send_keys(f'{vaga} \n')
sleep(2)
    
#fechar localidade automática
botao_fechar_local = '/html/body/header/nav/section/section[2]/form/section[2]/button/icon'
fechar_local = driver.find_element_by_xpath(botao_fechar_local)
fechar_local.click()
sleep(2)
    
#pesquisando localidade da vaga
botao_localidade = '/html/body/header/nav/section/section[2]/form/section[2]/input'
busca_localidade = driver.find_element_by_xpath(botao_localidade)
busca_localidade.click()
busca_localidade.send_keys(f'{local} \n')
sleep(2)
resultados = driver.find_elements_by_class_name('result-card')    
lista_descricao = []
lista_titulo = []

while len(resultados) > len(lista_descricao):
    print(f'Quantidade de resultados: {len(resultados)}')
    for r in resultados[len(lista_descricao):]:
        r.click()
        sleep(5)
        try:
            #descricao = driver.find_element_by_xpath('//*[@id="main-content"]/section/div[2]/section[2]')
            descricao = driver.find_element_by_class_name('description')
            lista_descricao.append(descricao.text)             
        except:
            print('Erro')
            pass
    print(f'Quantidade de descrições: {len(lista_descricao)}')
    resultados = driver.find_elements_by_class_name('result-card')
    #SÓ ESTÁ INDO ATÉ A SEGUNDA PÁGINA - PQ?

    if len(lista_descricao) == len(resultados):
        break
        driver.quit()

#salvar resultados em arquivo de texto
def output():
    descricao_salvar = '\n'.join(lista_descricao)
    with open('descricoes_vagas.txt', 'w', encoding='utf-8') as file:
        file.write(descricao_salvar)


