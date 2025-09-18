import sqlite3
import pandas as pd
import os

try:
    # Conexão com a tabela
    database = sqlite3.connect('web_scraping_f1_python/web-scraping-f1-python-sqlite/data/databasef1.db')

    cursor = database.cursor()

    # Criação das tabelas
    # cursor.execute("CREATE TABLE drivers (round INTEGER, nome TEXT, abreviacao TEXT, posicao INTEGER, pontos REAL)")
    # cursor.execute("CREATE TABLE teams (round INTEGER, nome TEXT, posicao INTEGER, pontos REAL)")

    # Inserção dos dados ja extraidos nas tabelas
    # df_racers = pd.read_csv("web_scraping_f1_python/web_scraping_f1_python_csv/data/pontuacoes_pilotos.csv")
    # df_teams = pd.read_csv("web_scraping_f1_python/web_scraping_f1_python_csv/data/pontuacoes_equipes.csv")

    # for index, row in df_racers.iterrows():
    #     cursor.execute("INSERT INTO drivers (round, nome, abreviacao, posicao, pontos) VALUES (?, ?, ?, ?, ?)", 
    #                    (row['round'], row['nome'], row['abreviacao'], row['posicao'], row['pontos']))
    # for index, row in df_teams.iterrows():
    #     cursor.execute("INSERT INTO teams (round, nome, posicao, pontos) VALUES (?, ?, ?, ?)", 
    #                    (row['round'], row['nome'], row['posicao'], row['pontos']))

    database.commit()
    database.close()
except sqlite3.Error as erro:
    print("Falha ao se conectar com o banco de dados | ", erro)