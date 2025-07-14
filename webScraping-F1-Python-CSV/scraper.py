from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

#função de webScraping para extrar dados da página
def web_scraping ():
#Endereço da página de classificação da Fórmula 1
    url = "https://www.espn.com.br/f1/classificacao"
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    #Espera a tabela estar completamente carregada
    wait = WebDriverWait(driver, 10) 
    wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "tr.Table__TR.Table__TR--sm.Table__even"))
)

    racers_lines = driver.find_elements(By.CSS_SELECTOR, "tr.Table__TR.Table__TR--sm.Table__even")
    #vetor de pilotos
    racers = []
    #for pra cada linha da tabela da página de pilotos
    for line in racers_lines:
        try:
            #pega os pontos no span do html da linha
            points = line.find_element(By.CSS_SELECTOR, "span.stat-cell").text.strip()
            #pega a posição do piloto
            position = line.find_element(By.CSS_SELECTOR, "span.team-position").text.strip()
            #coleta o nome do piloto
            name = line.find_element(By.CSS_SELECTOR, "span.dn.show-mobile abbr").get_attribute("title").strip()
            #coleta a abreviação do nome do piloto
            abreviation = line.find_element(By.CSS_SELECTOR, "span.dn.show-mobile abbr").text.strip()

            #Coloca os dados no vetor de pilotos
            racers.append({
                "nome": name,
                "abreviacao": abreviation,
                "posicao": int(position),
                "pontos": int(points),
            })

        # pula linhas que não têm os elementos esperados
        except Exception as error:
            print(f"Erro ao processar linha: {error}")
            break

    #Pega o conteúdi da primeira linha antes da troca de aba
    primeiro_piloto = driver.find_element(By.CSS_SELECTOR, "tr.Table__TR.Table__TR--sm.Table__even").text


    #Muda para a tabela de Construtores(equipes) da Formula 1
    driver.find_element(By.CSS_SELECTOR,'a.AnchorLink.Button--anchorLink[href*="constructores"]'
    ).click()
    
    #Espera a nova tabela com o conteúdo das equipes carregar
    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.CSS_SELECTOR, "tr.Table__TR.Table__TR--sm.Table__even").text != primeiro_piloto
    )

    #salva o dicionário de equipes em uma variável
    teams_lines = driver.find_elements(By.CSS_SELECTOR, "tr.Table__TR.Table__TR--sm.Table__even")
    teams = []

    for line in teams_lines:
        try:
            points = line.find_element(By.CSS_SELECTOR, "span.stat-cell").text.strip()
            position = line.find_element(By.CSS_SELECTOR, "span.team-position").text.strip()
            name = line.find_element(By.CSS_SELECTOR, "span.dn.show-mobile").text.strip()

            teams.append({
                "equipe": name,
                "posicao": int(position),
                "pontos": int(points),
            })
        except Exception as error:
            print(f"Erro ao processar linha: {error}")
            break
    driver.quit()

    #Retorna os dois dataframes
    df_racers = pd.DataFrame(racers)
    df_teams = pd.DataFrame(teams)
    return df_racers, df_teams
