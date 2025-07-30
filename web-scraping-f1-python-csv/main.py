from scraper import web_scraping
import pandas as pd
import os

#Leitura das informações dos arquivos CSV para um dataframe
base_path = "web-scraping-f1-python-csv"
old_df_racers = pd.read_csv(os.path.join(base_path, "data", "pontuacoes_pilotos.csv"))
old_df_teams = pd.read_csv(os.path.join(base_path, "data", "pontuacoes_equipes.csv"))

def main():
    df_racers_today, df_teams_today = web_scraping()
    
if __name__ == "__main__":