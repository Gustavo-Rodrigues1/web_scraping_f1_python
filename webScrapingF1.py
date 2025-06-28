from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

#Endereço da página de classificação da Fórmula 1
url = "https://www.espn.com.br/f1/classificacao"
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)

#função de webScraping para extrar dados da página
def webScraping (lines, tipo="piloto"):
    #dicionário para o ranqueamento
    rank = {}
    #for pra cada linha da tabela da página
    for line in lines:
        try:
            #pega os pontos e posição no span do html da linha
            points = line.find_element(By.CSS_SELECTOR, "span.stat-cell").text.strip()
            position = line.find_element(By.CSS_SELECTOR, "span.team-position").text.strip()

            if tipo == "piloto":
                #coleta o nome do piloto
                name = line.find_element(By.CSS_SELECTOR, "span.dn.show-mobile abbr").get_attribute("title").strip()
                #coleta a abreviação do nome do piloto
                abbreviation = line.find_element(By.CSS_SELECTOR, "span.dn.show-mobile abbr").text.strip()

                #Coloca os dados no dicionário
                rank[name] = {
                    "abreviação": abbreviation,
                    "posição": position,
                    "pontos": points
                }

            elif tipo == "equipe":
                #Coleta o nome da equipe
                name = line.find_element(By.CSS_SELECTOR, "span.dn.show-mobile").text.strip()
                #Coloca os dados no dicionário
                rank[name] = {
                    "posição": position,
                    "pontos": points
                }
        # pula linhas que não têm os elementos esperados
        except Exception as error:
            print(f"Erro ao processar linha: {error}")
            break
    return rank 
#Espera a tabela estar completamente carregada
time.sleep(2)

racers_lines = driver.find_elements(By.CSS_SELECTOR, "tr.Table__TR.Table__TR--sm.Table__even")
#salva o dicionário de pilotos em uma variável
racers = webScraping(racers_lines, tipo="piloto")

#Transforma o dicionário em um dataframe
df_pilotos = pd.DataFrame.from_dict(racers, orient='index')
df_pilotos.index.name = "nome"

#Muda para a tabela de Construtores(equipes) da Formula 1
driver.find_element(By.CSS_SELECTOR,'a.AnchorLink.Button--anchorLink[href*="constructores"]'
).click()
#Espera a tabela estar completamente carregada
time.sleep(2)

#salva o dicionário de equipes em uma variável
team_lines = driver.find_elements(By.CSS_SELECTOR, "tr.Table__TR.Table__TR--sm.Table__even")
team = webScraping(team_lines,"equipe")

#Transforma o dicionário em um dataframe
df_equipes = pd.DataFrame.from_dict(team, orient='index')
df_equipes.index.name = "equipe"

driver.quit()

#Exibe os dataframes em um arquivo txt
with open("classificacao_f1.txt", "w", encoding="utf-8") as f:
    f.write("🏎️ CLASSIFICAÇÃO DE PILOTOS\n\n")
    f.write(df_pilotos.to_string())
    f.write("\n\n==============================\n\n")
    f.write("🏁 CLASSIFICAÇÃO DE EQUIPES\n\n")
    f.write(df_equipes.to_string())