import os
import discord
from discord.ext import commands

# Set up your bot with the necessary intents
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# An example of a simple slash command
@bot.tree.command(name="hello", description="Say hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello! How can I assist you today?")

# Event when bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")
    # Sync the commands with Discord
    await bot.tree.sync()

@bot.tree.command(name="ping", description="Check the bot's latency.")
async def ping(interaction: discord.Interaction):
    latency = bot.latency * 1000  # Convert to milliseconds
    await interaction.response.send_message(f"Pong! Latency is {latency:.2f}ms")

bot.run(os.getenv('DISCORD_TOKEN'))