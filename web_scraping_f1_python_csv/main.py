import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.scraper import web_scraping
import core.discord_bot as dm
import core.grafo as gf
import core.compare_last_df as cld
import update_csv as uc
import pandas as pd

# Caminho base dinâmico (raiz do repositório)
base_path = os.path.dirname(os.path.abspath(__file__))

# Caminhos completos
racers_path = os.path.join(base_path, "data", "pontuacoes_pilotos.csv")
teams_path = os.path.join(base_path, "data", "pontuacoes_equipes.csv")

# Leitura
old_df_racers = pd.read_csv(racers_path)
old_df_teams = pd.read_csv(teams_path)

def routine():
    global old_df_racers
    global old_df_teams
    df_racers_today, df_teams_today = web_scraping()
    racers_compare_result = cld.compare_racers(old_df_racers, df_racers_today)
    teams_compare_result = cld.compare_teams(old_df_teams, df_teams_today)
    # Comparação entre dados antigos e extraidos e os atualiza se forem diferentes
    if not racers_compare_result:
        uc.update_csv_racers(df_racers_today)
        old_df_racers = pd.read_csv(racers_path)
    # Comparação entre dados antigos e extraidos e os atualiza se forem diferentes
    if not teams_compare_result:
        uc.update_csv_teams(df_teams_today)
        old_df_teams = pd.read_csv(teams_path)
    if not racers_compare_result or not teams_compare_result:
        gf.generate_plot(old_df_racers, old_df_teams)
        dm.discord_bot_dm()

if __name__ == "__main__":
    routine()