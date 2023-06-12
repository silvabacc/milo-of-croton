import discord
from discord import app_commands
from config import DISCORD_TOKEN

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
  await tree.sync()
  print(f'We have logged in as {client.user}')


#Example Command
@tree.command(name = "foo", description = "Example Command")
async def foo(interaction):
  await interaction.response.send_message('hello')

client.run(DISCORD_TOKEN)