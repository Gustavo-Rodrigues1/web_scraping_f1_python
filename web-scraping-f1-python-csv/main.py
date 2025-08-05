from scraper import web_scraping
import discord_bot as dm
import grafo as gf
import update_csv as uc
import pandas as pd
import os

# Caminho base dinâmico (raiz do repositório)
base_path = os.path.dirname(os.path.abspath(__file__))

# Caminhos completos
racers_path = os.path.join(base_path, "data", "pontuacoes_pilotos.csv")
teams_path = os.path.join(base_path, "data", "pontuacoes_equipes.csv")

# Leitura
old_df_racers = pd.read_csv(racers_path)
old_df_teams = pd.read_csv(teams_path)

#função para comparar dataframes de corredores
def compare_racers (old_df_racers, df_racers_today):
    # Pega o último round
    max_round_racers = old_df_racers["round"].max()
    # Dados do último round
    df_last_round_racers = old_df_racers[old_df_racers["round"] == max_round_racers].drop(columns=["round"]).reset_index(drop=True)
    # Comparação entre dados antigos e extraidos
    return df_racers_today.equals(df_last_round_racers)

def compare_teams (old_df_teams, df_teams_today):
    # Pega o último round
    max_round_teams = old_df_teams["round"].max()
    # Dados do último round
    df_last_round_teams = old_df_teams[old_df_teams["round"] == max_round_teams].drop(columns=["round"]).reset_index(drop=True)
    # Comparação entre dados antigos e extraidos
    return df_teams_today.equals(df_last_round_teams)

def routine():
    df_racers_today, df_teams_today = web_scraping()
    racers_compare_result = compare_racers(old_df_racers,df_racers_today)
    teams_compare_result = compare_teams(old_df_teams, df_teams_today)
    # Comparação entre dados antigos e extraidos e os atualiza se forem diferentes
    if not racers_compare_result:
        uc.update_csv_racers(df_racers_today)
    # Comparação entre dados antigos e extraidos e os atualiza se forem diferentes
    if not teams_compare_result:
        uc.update_csv_teams(df_teams_today)
    if racers_compare_result or teams_compare_result:
        gf.generate_plot()
        dm.discord_bot_dm()

if __name__ == "__main__":
    routine()