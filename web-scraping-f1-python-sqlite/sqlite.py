import sqlite3
try:
    # Conexão com a tabela
    database = sqlite3.connect('web_scraping_f1_python/web-scraping-f1-python-sqlite/data/databasef1.db')

    cursor = database.cursor()

    # Criação das tabelas
    # cursor.execute("CREATE TABLE drivers (round INTEGER, nome TEXT, abreviacao TEXT, posicao INTEGER, pontos REAL)")
    # cursor.execute("CREATE TABLE teams (round INTEGER, nome TEXT, posicao INTEGER, pontos REAL)")


    database.commit()
    database.close()
except sqlite3.Error as erro:
    print("Falha ao se conectar com o banco de dados | ", erro)