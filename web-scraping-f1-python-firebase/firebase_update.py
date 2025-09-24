def update_firebase_racers(df_racers_today, db):
    drivers_ref = db.collection("drivers")
    # Pega o round maximo
    rounds = [doc.to_dict().get("round", 0) for doc in drivers_ref.stream()]
    max_round = max(rounds) if rounds else 0
    new_round = max_round + 1
    df_racers_today["round"] = new_round
    # Insere os dados na coleção
    for _, row in df_racers_today.iterrows():
        drivers_ref.add(row.to_dict())

def update_firebase_teams(df_teams_today, db):
    teams_ref = db.collection("teams")
    # Pega o round maximo
    rounds = [doc.to_dict().get("round", 0) for doc in teams_ref.stream()]
    max_round = max(rounds) if rounds else 0
    new_round = max_round + 1
    df_teams_today["round"] = new_round
    # Insere os dados na coleção
    for _, row in df_teams_today.iterrows():
        teams_ref.add(row.to_dict())