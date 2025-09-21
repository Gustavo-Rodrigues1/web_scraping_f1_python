import sqlite3
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.scraper import web_scraping
import core.discord_bot as dm
import core.grafo as gf
import mysqlite as ms
import pandas as pd

# Caminho base dinâmico (raiz do repositório)
base_path = os.path.dirname(os.path.abspath(__file__))

# Caminho do banco de dados
db_path = os.path.join(base_path, "data", "databasef1.db")

# Cria conexão SQLite
conect = sqlite3.connect(db_path)

# Leitura
old_df_racers = pd.read_sql("SELECT * FROM drivers", conect)
old_df_teams = pd.read_sql("SELECT * FROM teams", conect)

def compare_racers(old_df_racers, df_racers_today):
    # Pega o último round
    max_round_racers = old_df_racers["round"].max()
    # Dados do último round
    df_last_round_racers = old_df_racers[old_df_racers["round"] == max_round_racers].drop(columns=["round"]).reset_index(drop=True)
    # Comparação entre dados antigos e extraidos
    return df_racers_today.equals(df_last_round_racers)

def compare_teams(old_df_teams, df_teams_today):
    # Pega o último round
    max_round_teams = old_df_teams["round"].max()
    # Dados do último round
    df_last_round_teams = old_df_teams[old_df_teams["round"] == max_round_teams].drop(columns=["round"]).reset_index(drop=True)
    # Comparação entre dados antigos e extraidos
    return df_teams_today.equals(df_last_round_teams)

def routine():
    global old_df_racers
    global old_df_teams
    df_racers_today, df_teams_today = web_scraping()
    racers_compare_result = compare_racers(old_df_racers, df_racers_today)
    teams_compare_result = compare_teams(old_df_teams, df_teams_today)
    # Comparação entre dados antigos e extraidos e os atualiza se forem diferentes
    if not racers_compare_result:
        ms.update_sqlite_racers(df_racers_today, conect)
        old_df_racers = pd.read_sql("SELECT * FROM drivers", conect)
    # Comparação entre dados antigos e extraidos e os atualiza se forem diferentes
    if not teams_compare_result:
        ms.update_sqlite_teams(df_teams_today, conect)
        old_df_teams = pd.read_sql("SELECT * FROM teams", conect)
    if not racers_compare_result or not teams_compare_result:
        gf.generate_plot(old_df_racers, old_df_teams)
        dm.discord_bot_dm()
    conect.close()

if __name__ == "__main__":
    routine()