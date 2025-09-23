import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.scraper import web_scraping
import core.discord_bot as dm
import core.grafo as gf
import pandas as pd
import firebase_admin

def compare_racers(old_df_racers, df_racers_today):
    # preencher

def compare_teams(old_df_teams, df_teams_today):
     # preencher

def routine():
    global old_df_racers
    global old_df_teams
    df_racers_today, df_teams_today = web_scraping()
    racers_compare_result = compare_racers(old_df_racers, df_racers_today)
    teams_compare_result = compare_teams(old_df_teams, df_teams_today)
    # Comparação entre dados antigos e extraidos e os atualiza se forem diferentes
    if not racers_compare_result:
        # preencher
    # Comparação entre dados antigos e extraidos e os atualiza se forem diferentes
    if not teams_compare_result:
        # preencher
    if not racers_compare_result or not teams_compare_result:
        gf.generate_plot(old_df_racers, old_df_teams)
        dm.discord_bot_dm()

if __name__ == "__main__":
    routine()