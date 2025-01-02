import os
import discord
from discord.ext import commands
import time

# Set up your bot with the necessary intents
intents = discord.Intents.default()
intents.messages = True  # Ensures the bot can receive messages
intents.guilds = True    # For guild-related events
intents.message_content = True  # Required for reading message content in interactions (for slash commands)

bot = commands.Bot(command_prefix="!", intents=intents)

# An example of a simple slash command with improved functionality
@bot.tree.command(name="hello", description="Say hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello! How can I assist you today? 😊")

# Event when bot is ready (showcase some useful information)
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print(f"Bot is connected to {len(bot.guilds)} server(s).")
    print("------")
    # Sync the commands with Discord API
    await bot.tree.sync()
    print("Commands synced successfully!")

# A slash command for checking the bot's latency
@bot.tree.command(name="ping", description="Check the bot's latency.")
async def ping(interaction: discord.Interaction):
    latency = bot.latency * 1000  # Convert to milliseconds
    await interaction.response.send_message(f"Pong! Latency is {latency:.2f}ms")

# A slash command to provide detailed information about the bot
@bot.tree.command(name="info", description="Get detailed information about the bot.")
async def info(interaction: discord.Interaction):
    uptime = time.time() - bot.start_time
    uptime_str = f"{uptime // 3600:.0f} hours { (uptime % 3600) // 60:.0f} minutes"
    embed = discord.Embed(title="Bot Information", color=discord.Color.blurple())
    embed.add_field(name="Bot Name", value=bot.user.name, inline=True)
    embed.add_field(name="Bot ID", value=bot.user.id, inline=True)
    embed.add_field(name="Uptime", value=uptime_str, inline=True)
    embed.add_field(name="Servers Connected", value=len(bot.guilds), inline=True)
    embed.set_footer(text="Developed by YourName")
    await interaction.response.send_message(embed=embed)

# A slash command for sending a custom greeting with user's name
@bot.tree.command(name="greet", description="Send a personalized greeting!")
async def greet(interaction: discord.Interaction, user: discord.User):
    await interaction.response.send_message(f"Hello, {user.mention}! How are you today? 😃")

# Command to send an embed with a random joke
@bot.tree.command(name="joke", description="Send a random joke!")
async def joke(interaction: discord.Interaction):
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "I only know 25 letters of the alphabet. I don't know y."
    ]
    joke = random.choice(jokes)
    embed = discord.Embed(title="Random Joke", description=joke, color=discord.Color.green())
    await interaction.response.send_message(embed=embed)

# A command to check a user's account creation date
@bot.tree.command(name="accountinfo", description="Get information about a user's account.")
async def accountinfo(interaction: discord.Interaction, user: discord.User):
    account_age = discord.utils.format_dt(user.created_at, style="F")
    join_date = discord.utils.format_dt(user.joined_at, style="F")
    embed = discord.Embed(title=f"{user.name}'s Account Information", color=discord.Color.blue())
    embed.add_field(name="Account Created", value=account_age, inline=True)
    embed.add_field(name="Joined Server", value=join_date, inline=True)
    embed.set_thumbnail(url=user.avatar.url)
    await interaction.response.send_message(embed=embed)

# A command for checking the server's member count
@bot.tree.command(name="serverinfo", description="Get information about the current server.")
async def serverinfo(interaction: discord.Interaction):
    guild = interaction.guild
    member_count = guild.member_count
    text_channels = len(guild.text_channels)
    voice_channels = len(guild.voice_channels)
    embed = discord.Embed(title=f"Server Information: {guild.name}", color=discord.Color.purple())
    embed.add_field(name="Member Count", value=member_count, inline=True)
    embed.add_field(name="Text Channels", value=text_channels, inline=True)
    embed.add_field(name="Voice Channels", value=voice_channels, inline=True)
    embed.set_footer(text=f"Requested by {interaction.user.name}")
    await interaction.response.send_message(embed=embed)

# Set up the bot's start time (for uptime calculation)
@bot.event
async def on_ready():
    bot.start_time = time.time()
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print(f"Bot is connected to {len(bot.guilds)} server(s).")
    print("------")
    # Sync the commands with Discord API
    await bot.tree.sync()
    print("Commands synced successfully!")

# Run the bot with the token stored in your environment variables
bot.run(os.getenv("DISCORD_TOKEN"))
