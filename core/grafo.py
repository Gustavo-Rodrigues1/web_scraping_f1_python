import pandas
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import os

def generate_plot(df_racers, df_teams):
    #Garante que Round esteja em inteiro
    df_racers['round'] = df_racers['round'].astype(int)
    
    # Cores baseadas nos uniformes da temporada atual
    team_color = {
        "Red Bull": "#1E41FF",       # azul escuro
        "Ferrari": "#DC0000",        # vermelho
        "Mercedes": "#00D2BE",       # azul-piscina
        "McLaren": "#FF8700",        # laranja
        "Aston Martin": "#006F62",   # verde escuro
        "Alpine": "#0090FF",         # azul
        "Williams": "#005AFF",       # azul royal
        "Racing Bulls": "#6692FF",             # azul claro
        "Sauber": "#52E252",    # verde
        "Haas": "#B6BABD"   # cinza claro
    }
    
    racer_team = {
        #Alpine
        "Jack Doohan": "Alpine",
        "Pierre Gasly": "Alpine",
        "Franco Colapinto": "Alpine",
        #Red bull racing
        "Max Verstappen": "Red Bull",
        "Yuki Tsunoda": "Red Bull",
        #Kick Sauber
        "Gabriel Bortoleto": "Sauber",
        "Nico Hülkenberg": "Sauber",
        #Rb
        "Isack Hadjar": "Racing Bulls",
        "Liam Lawson": "Racing Bulls",
        #Ferrari
        "Lewis Hamilton": "Ferrari",
        "Charles Leclerc": "Ferrari",
        #Mercedes
        "Kimi Antonelli": "Mercedes",
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
        #Haas
        "Esteban Ocon": "Haas",
        "Oliver Bearman": "Haas"
    }
    
    # Total de pontos finais por piloto divido em duas partes
    total_points_racers = df_racers.groupby("nome")["pontos"].max().sort_values(ascending=False)
    top_10 = total_points_racers.head(10).index
    bottom_10 = total_points_racers.tail(10).index
    
    df_top10 = df_racers[df_racers["nome"].isin(top_10)]
    df_bottom10 = df_racers[df_racers["nome"].isin(bottom_10)]
    
    # Criação dos subplots
    fig = plt.figure(figsize=(20, 10))
    gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1])
    
    # Parte de cima: dois gráficos lado a lado
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    
    # Parte de baixo: um gráfico ocupando a largura total
    ax3 = fig.add_subplot(gs[1, :])  # <- ocupa todas as colunas
    
    # Função para plotar em um eixo específico
    def plot_subplot_racer(ax, df, title):
        for racer_name, racer_data in df.groupby("nome"):
            sorted_data = racer_data.sort_values("round")
            team = racer_team.get(racer_name, "Outro")
            color = team_color.get(team, "gray")
            ax.plot(sorted_data["round"], sorted_data["pontos"], marker='o', label=racer_name, color=color)
            for x, y in zip(sorted_data["round"], sorted_data["pontos"]):
                ax.text(x, y + 0.7, str(y), fontsize=7, ha='center', va='bottom', color=color)
            last_row = sorted_data.iloc[-1]
            abreviacao = last_row["abreviacao"]
            ax.text(last_row["round"] + 0.1, last_row["pontos"], abreviacao,
                    fontsize=9, fontweight='bold', color=color, va='center')
        ax.set_title(title, fontsize=14, fontweight="bold")
        ax.set_xlabel("GP", fontsize=12, fontweight="bold")
        ax.set_ylabel("Pontos acumulados", fontsize=12, fontweight="bold")
        ax.grid(True)
        ax.legend(fontsize=8)
    
    def plot_subplot_team(ax, df, title):
        for team_name, team_data in df.groupby("nome"):
            sorted_data = team_data.sort_values("round")
            color = team_color.get(team_name, "gray")
            ax.plot(sorted_data["round"], sorted_data["pontos"], marker='o', label=team_name, color=color)
            for x, y in zip(sorted_data["round"], sorted_data["pontos"]):
                ax.text(x, y + 2, str(y), fontsize=7, ha='center', va='bottom', color=color)
        ax.set_title(title, fontsize=14, fontweight="bold")
        ax.set_xlabel("GP", fontsize=12, fontweight="bold")
        ax.set_ylabel("Pontos acumulados", fontsize=12, fontweight="bold")
        ax.grid(True)
        ax.legend(fontsize=8)
    
    # Gráficos
    plot_subplot_racer(ax1, df_top10, "Top 10 Primeiros Pilotos - Pontuação Acumulada")
    plot_subplot_racer(ax2, df_bottom10, "10 Últimos Pilotos - Pontuação Acumulada")
    plot_subplot_team(ax3, df_teams, "Pontuação do Campeonato de Construtores de 2025")
    
    
    # Ajuste dos eixos x
    for ax in [ax1, ax2, ax3]:
        ax.set_xticks(np.arange(df_racers["round"].min(), df_racers["round"].max() + 1))
    
    plt.tight_layout()
    output_path = os.path.join("images", "pontuacoes_pilotos_equipes.png")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    