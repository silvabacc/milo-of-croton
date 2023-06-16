from dotenv import dotenv_values

config = dotenv_values(".env")

DISCORD_TOKEN = config["DISCORD_TOKEN"]
SUPABASE_URL = config["SUPABASE_URL"]
SUPABASE_KEY = config["SUPABASE_KEY"]
SUPABASE_USER = config["SUPABASE_USER"]
SUPABASE_USER_PASS = config["SUPABASE_USER_PASS"]
