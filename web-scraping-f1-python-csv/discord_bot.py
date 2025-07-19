import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    
    user_id = int(os.getenv("USER_ID"))  # seu ID do Discord
    user = await bot.fetch_user(user_id)
    
    await user.send("Olá! Aqui está o gráfico atualizado da F1 🏎️")
    
    with open("webScraping-F1-Python-CSV\\data\\pontuacoes_pilotos.png", "rb") as f:
        await user.send(file=discord.File(f))

    await bot.close()  # fecha após envio (útil para bots automáticos)

bot.run(TOKEN)