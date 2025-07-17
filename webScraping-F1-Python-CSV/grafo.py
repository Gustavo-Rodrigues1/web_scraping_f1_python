import pandas as pd
import matplotlib.pyplot as plt

#Leitura das informações dos arquivos CSV para um dataframe
df_racers = pd.read_csv("webScraping-F1-Python-CSV\\pontuacoes_pilotos.csv")
# df_teams = pd.read_csv("webScraping-F1-Python-CSV\\pontuacoes_equipes.csv")

#Garante que Round esteja em inteiro
df_racers['round'] = df_racers['round'].astype(int)

# Cores baseadas nos uniformes da temporada atual
team_color = {
    "Red Bull Racing": "#1E41FF",       # azul escuro
    "Ferrari": "#DC0000",        # vermelho
    "Mercedes": "#00D2BE",       # azul-piscina
    "McLaren": "#FF8700",        # laranja
    "Aston Martin": "#006F62",   # verde escuro
    "Alpine": "#0090FF",         # azul
    "Williams": "#005AFF",       # azul royal
    "RB": "#6692FF",             # azul claro
    "Kick Sauber": "#52E252",    # verde
    "Haas F1 Team ": "#B6BABD",           # cinza claro
}

racer_team = {
    #Alpine
    "Jack Doohan": "Alpine",
    "Pierre Gasly": "Alpine",
    "Franco Colapinto": "Alpine",
    #Red bull racing
    "Max Verstappen": "Red Bull Racing",
    "Yuki Tsunoda": "Red Bull Racing",
    #Kick Sauber
    "Gabriel Bortoleto": "Kick Sauber",
    "Nico Hülkenberg": "Kick Sauber",
    #Rb
    "Isack Hadjar": "RB",
    "Liam Lawson": "RB",
    #Ferrari
    "Lewis Hamilton": "Ferrari",
    "Charles Leclerc": "Ferrari",
    #Mercedes
    "Andrea Kimi Antonelli": "Mercedes",
    "George Russell": "Mercedes",
    #Aston Martin
    "Fernando Alonso": "Aston Martin",
    "Lance Stroll": "Aston Martin",
    #Williams
    "Alexander Albon": "Williams",
    "Carlos Sainz Jr.": "Williams",
    #McLaren
    "Lando Norris": "McLaren",
    "Oscar Piastri": "McLaren",
    #Haas F1 Team
    "Esteban Ocon": "Haas F1 Team",
    "Oliver Bearman": "Haas F1 Team",
    
}

# Total de pontos finais por piloto
total_points = df_racers.groupby("nome")["pontos"].max().sort_values(ascending=False)
top_10 = total_points.head(10).index
bottom_10 = total_points.tail(10).index

df_top10 = df_racers[df_racers["nome"].isin(top_10)]
df_bottom10 = df_racers[df_racers["nome"].isin(bottom_10)]

# Criação dos subplots
fig, axs = plt.subplots(1, 2, figsize=(20, 8), sharex=True)

# Função para plotar em um eixo específico
def plot_subplot(ax, df, title):
    for racer_name, racer_data in df.groupby("nome"):
        sorted_data = racer_data.sort_values("round")
        team = racer_team.get(racer_name, "Outro")
        color = team_color.get(team, "gray")
        ax.plot(sorted_data["round"], sorted_data["pontos"], marker='o', label=racer_name, color=color)
        for x, y in zip(sorted_data["round"], sorted_data["pontos"]):
            ax.text(x, y + 1, str(y), fontsize=7, ha='center', va='bottom', color=color)
            last_row = sorted_data.iloc[-1]
            abreviacao = last_row["abreviacao"]
            ax.text(last_row["round"] + 0.1, last_row["pontos"], abreviacao,
                fontsize=9, fontweight='bold', color=color, va='center')
    ax.set_title(title, fontsize=12)
    ax.set_ylabel("Pontos acumulados", fontsize=12)
    ax.grid(True)

# Gráficos
plot_subplot(axs[0], df_top10, "Top 10 Primeiros Pilotos - Pontuação Acumulada")
plot_subplot(axs[1], df_bottom10, "10 Últimos Pilotos - Pontuação Acumulada")
axs[0].set_xlabel("GP", fontsize=12)
axs[1].set_xlabel("GP", fontsize=12)
plt.xticks(range(df_racers["round"].min(), df_racers["round"].max() + 1))
plt.tight_layout()
plt.savefig("webScraping-F1-Python-CSV\\pontuacoes_pilotos.png", dpi=300, bbox_inches='tight')
