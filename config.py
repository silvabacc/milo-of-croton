from dotenv import load_dotenv
load_dotenv()

import os

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
SUPABASE_USER = os.environ.get("SUPABASE_USER")
SUPABASE_USER_PASS = os.environ.get("SUPABASE_USER_PASS")
LOOP_HOURS = os.environ.get("LOOP_HOURS")
