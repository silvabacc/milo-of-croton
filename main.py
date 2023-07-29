import discord
from discord.ext import tasks
from discord import app_commands
from config import DISCORD_TOKEN, LOOP_HOURS
from add_quote_modal import AddQuoteModal
from service import getQuote
from embeds import quote_embed

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
  await tree.sync()
  print(f'We have logged in as {client.user}')
  send_quote.start()

@tree.command(name = "quote", description="Replies with a quote")
async def quote(interaction):
  quote = getQuote()
  await interaction.response.send_message(embed=quote_embed(author=quote['author'], quote=quote['text'], id=quote["id"]))

@tree.command(name = "add_quote", description="Adds a quote")
async def add_quote(interaction):
  await interaction.response.send_modal(AddQuoteModal())

@tree.command(name = "delete_quote", description="Delete a quote by passing the ID", guild=discord.Object(id=752537720676548638))
async def delete_quote(interaction):
  await interaction.response.send_message("deleting...")

@tasks.loop(hours=int(LOOP_HOURS))  
async def send_quote():
  quote = getQuote()

  guilds = client.guilds
  channels = []

  for guild in guilds:
    channel = next((channel for channel in guild.text_channels if channel.name == 'stoic-quotes'), None)
    channels.append(channel)

  for channel in channels:
    if(channel != None):
      await channel.send(embed=quote_embed(author=quote["author"], quote=quote["text"], id=quote["id"]))
    
client.run(DISCORD_TOKEN)