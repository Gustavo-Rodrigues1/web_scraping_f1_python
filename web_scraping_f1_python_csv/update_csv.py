import pandas as pd
import os

base_path = os.path.dirname(os.path.abspath(__file__))

def update_csv_racers(df_racers_today):
    #path com o nome e endereço dos arquivos
    path_racers = os.path.join(base_path, "data", "pontuacoes_pilotos.csv")
        # Atualiza pontuação das equipes
    if os.path.exists(path_racers):
        old_racers_df = pd.read_csv(path_racers)
        # Adiciona a coluna round incrementado mais 1 se a coluna ja existir para valores anteriores
        max_round_racers = old_racers_df["round"].max() if "round" in old_racers_df.columns else 1
        new_round_racers = max_round_racers + 1
        df_racers_today["round"] = new_round_racers
        merged_racers_df = pd.concat([old_racers_df, df_racers_today], ignore_index=True)
    else:
        # Adiciona a coluna round com o valor padrão 1
        df_racers_today["round"] = 1
        merged_racers_df = df_racers_today
    merged_racers_df.to_csv(path_racers, index=False)

def update_csv_teams(df_teams_today):
    #path com o nome e endereço dos arquivos
    path_teams = os.path.join(base_path, "data", "pontuacoes_equipes.csv")
    if os.path.exists(path_teams):
        old_teams_df = pd.read_csv(path_teams)
        # Adiciona a coluna round incrementado mais 1 se a coluna ja existir para valores anteriores
        max_round_team = old_teams_df["round"].max() if "round" in old_teams_df.columns else 1
        new_round_team = max_round_team + 1
        df_teams_today["round"] = new_round_team
        merged_teams_df = pd.concat([old_teams_df, df_teams_today], ignore_index=True)
    else:
        # Adiciona a coluna round com o valor padrão 1
        df_teams_today["round"] = 1
        merged_teams_df = df_teams_today
    merged_teams_df.to_csv(path_teams, index=False)
