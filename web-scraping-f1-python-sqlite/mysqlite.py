import sqlite3
import pandas as pd
import os

base_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_path, "data", "database_f1.db")

def update_sqlite_racers(df_racers_today):
    conect = sqlite3.connect(db_path)
    cursor = conect.cursor

    # cria tabela se não existir
    cursor.execute("CREATE TABLE IF NOT EXISTS drivers (round INTEGER, nome TEXT, abreviacao TEXT, posicao INTEGER, pontos REAL)")
    # pega o round maximo
    cursor.execute("SELECT MAX(round) FROM drivers")
    max_round = cursor.fetchone()[0]
    new_round = (max_round or 0) + 1;
    df_racers_today["round"] = new_round
    # insere os dados na tabela
    df_racers_today.tosql("drivers", conect, if_exists="append",index=False)
    cursor.commit()
    cursor.close()

def update_sqlite_teams(df_teams_today):
    conect = sqlite3.connect(db_path)
    cursor = conect.cursor

    # cria tabela se não existir
    cursor.execute("CREATE TABLE IF NOT EXISTS teams (round INTEGER, nome TEXT, abreviacao TEXT, posicao INTEGER, pontos REAL)")
    # pega o round maximo
    cursor.execute("SELECT MAX(round) FROM teams")
    max_round = cursor.fetchone()[0]
    new_round = (max_round or 0) + 1;
    df_teams_today["round"] = new_round
    # insere os dados na tabela
    df_teams_today.tosql("teams", conect, if_exists="append",index=False)
    cursor.commit()
    cursor.close()