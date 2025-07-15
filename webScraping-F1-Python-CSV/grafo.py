import pandas as pd
import matplotlib.pyplot as plt

#Leitura das informações dos arquivos CSV para um dataframe
df_racers = pd.read_csv("webScraping-F1-Python-CSV\\pontuacoes_pilotos.csv")
# df_teams = pd.read_csv("webScraping-F1-Python-CSV\\pontuacoes_equipes.csv")

#Garante que Round esteja em inteiro
df_racers['round'] = df_racers['round'].astype(int)

#Cria o gráfico
plt.figure(figsize=(14, 8))

#Agrupa por piloto e plota a linha de pontos ao longo das rodadas
for racer_name, racer_data in df_racers.groupby("nome"):
    sorted_data = racer_data.sort_values("round")
    plt.plot(sorted_data["round"], sorted_data["pontos"], marker='o', label=racer_name)

# Estilização
plt.title("Evolução da Pontuação dos Pilotos por Rodada (2025)", fontsize=16)
plt.xlabel("Rodada", fontsize=12)
plt.ylabel("Pontos acumulados", fontsize=12)
plt.legend(fontsize=8, loc="upper left", bbox_to_anchor=(1.05, 1))
plt.grid(True)
plt.tight_layout()
plt.show()