# 🏎️ Web Scraping F1 + Discord Bot

Este projeto coleta dados atualizados sobre a Fórmula 1 por meio de scraping da ESPN F1, gera gráficos de pontuação acumulada dos pilotos e equipes, e envia automaticamente as imagens por mensagem privada usando um bot do Discord.

## 🔧 Tecnologias Utilizadas

- Python 3.x
- Selenium (Para realizar o web scraping)
- Pandas (Uso de dataframes)
- Matplotlib (Criação de gráficos)
- Discord.py (Bot do discord para enivar os dados)
- GitHub Actions (automatização)
- Versões alternativas de armazenamento: CSV, SQLite e Firebase

## 📦 Versões

### 1️⃣ Versão CSV Incremental

Armazena os dados dos GPs em arquivos `.csv` que são atualizados diariamente via GitHub Actions.

- ✅ Vantagem: simples e leve.
- ⚠️ Desvantagem: menos robusto para consultas e análises complexas.

### 2️⃣ Versão SQLite (Em breve)

Armazena os dados em banco relacional local via SQLite.

- ✅ Vantagem: suporte a SQL e estrutura organizada.
- ⚠️ Desvantagem: não escalável para ambientes distribuídos.

### 3️⃣ Versão Firebase (Em breve)

Salva os dados em tempo real na nuvem com o Firebase Realtime Database.

- ✅ Vantagem: ideal para acesso remoto e em tempo real.
- ⚠️ Desvantagem: maior complexidade de configuração.

## 🤖 Automatização com GitHub Actions

O projeto está configurado com `daily_run.yml` para executar diariamente às 13h da tarde(horário de Brasília), realizando scraping, gerando o gráfico e enviando no Discord.

## 📊 Exemplos de Saída

Gráficos gerados:

- Top 10 pilotos
- Bottom 10 pilotos
- Pontuação das equipes

## 📌 To Do

- [x] Implementar a lógica para o gráfico de pontuação das equipes (em andamento)
- [x] Verificação antes do envio da mensagem do Bot, para mandar apenas quando ouver diferença entre os gráficos
- [x] Refatorar
- [X] Finalizar versão SQLite
- [ ] Finalizar versão Firebase
- [x] Enviar imagens no Discord
- [ ] Automatizar com GitHub Actions
- [ ] Adicionar testes unitários para scraping e gráficos
