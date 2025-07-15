from scraper import web_scraping
import pandas as pd
import os

df_racers_today, df_teams_today = web_scraping()

def update_csv():
    #path com o nome e endereço dos arquivos
    path_racers = "webScraping-F1-Python-CSV\\pontuacoes_pilotos.csv"
    path_teams = "webScraping-F1-Python-CSV\\pontuacoes_equipes.csv"

    # Atualiza pontuação dos pilotos
    if os.path.exists(path_racers):
        old_racers_df = pd.read_csv(path_racers)
        merged_racers_df = pd.concat([old_racers_df, df_racers_today], ignore_index=True)
    else:
        merged_racers_df = df_racers_today
    merged_racers_df.to_csv(path_racers, index=False)

    # Atualiza pontuação das equipes
    if os.path.exists(path_teams):
        old_teams_df = pd.read_csv(path_teams)
        merged_teams_df = pd.concat([old_teams_df, df_teams_today], ignore_index=True)
    else:
        merged_teams_df = df_teams_today
    merged_teams_df.to_csv(path_teams, index=False)
update_csv()
