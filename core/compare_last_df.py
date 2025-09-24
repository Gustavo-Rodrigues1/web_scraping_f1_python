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