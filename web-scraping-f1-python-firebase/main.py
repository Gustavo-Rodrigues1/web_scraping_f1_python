import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.scraper import web_scraping
import core.discord_bot as dm
import core.grafo as gf
import core.compare_last_df as cld
import pandas as pd
import firebase_admin as fb
from firebase_admin import credentials, firestore
import firebase_update as fu

# Caminho para o arquivo das credenciais
cred_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "serviceAccountKey.json")
fb.initialize_app(credentials.Certificate(cred_path))

# Conexão com o Firestore
db = firestore.client()

# Carrega dados antigos
def load_old_data():
    racers_docs = db.collection("drivers").stream()
    teams_docs = db.collection("teams").stream()
    df_racers = pd.DataFrame([doc.to_dict() | {"id": doc.id} for doc in racers_docs])
    df_teams = pd.DataFrame([doc.to_dict() | {"id": doc.id} for doc in teams_docs])
    return df_racers, df_teams

def routine():
    global old_df_racers
    global old_df_teams
    df_racers_today, df_teams_today = web_scraping()
    racers_compare_result = cld.compare_racers(old_df_racers, df_racers_today)
    teams_compare_result = cld.compare_teams(old_df_teams, df_teams_today)
    # Comparação entre dados antigos e extraidos e os atualiza se forem diferentes
    if not racers_compare_result:
       fu.update_firebase_racers(df_racers_today, db)
       old_df_racers, _ = load_old_data() 
    if not teams_compare_result:
       fu.update_firebase_teams(df_teams_today, db)
       _, old_df_teams = load_old_data()
    if not racers_compare_result or not teams_compare_result:
        gf.generate_plot(old_df_racers, old_df_teams)
        dm.discord_bot_dm()

if __name__ == "__main__":
    old_df_racers, old_df_teams = load_old_data()
    routine()