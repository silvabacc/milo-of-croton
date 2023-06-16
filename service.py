from config import SUPABASE_URL, SUPABASE_KEY, SUPABASE_USER, SUPABASE_USER_PASS
from supabase import create_client, Client
import random

client: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def getPostgresClient():
  session  = client.auth.sign_in_with_password({"email": SUPABASE_USER, "password": SUPABASE_USER_PASS})
  postgrest_client = client.postgrest
  postgrest_client.auth(session.session.access_token) 
  return postgrest_client
    
def getQuote():
  pg_client = getPostgresClient()
  db_result = pg_client.table("quotes").select('*').execute()
  random.shuffle(db_result.data)
  random_quotes = db_result.data
  return random_quotes[0]

def insertQuote(text, author):
  pg_client = getPostgresClient()
  db_result = pg_client.table("quotes").insert({"text": text, "author": author}).execute()
  return db_result.data[0]
