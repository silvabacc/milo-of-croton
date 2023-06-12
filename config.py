from dotenv import dotenv_values

config = dotenv_values(".env")

DISCORD_TOKEN = config["DISCORD_TOKEN"]
