from config import SUPABASE_URL, SUPABASE_KEY, SUPABASE_USER, SUPABASE_USER_PASS
from supabase import create_client, Client
import random

client: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
session  = client.auth.sign_in_with_password({"email": SUPABASE_USER, "password": SUPABASE_USER_PASS})
postgrest_client = client.postgrest
postgrest_client.auth(session.session.access_token) 
  
def getQuote():
  db_result = postgrest_client.table("quotes").select('*').execute()
  random.shuffle(db_result.data)
  random_quotes = db_result.data
  return random_quotes[0]

def insertQuote(text, author):
  db_result = postgrest_client.table("quotes").insert({"text": text, "author": author}).execute()
  return db_result.data[0]
