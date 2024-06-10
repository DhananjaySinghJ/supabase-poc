from dotenv import load_dotenv
load_dotenv()

import os

from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

# Fetch the data from the table
data = supabase.table("todos").select("id","name").eq("name", "Item 1").execute()
#print(data)

# Insert data
#data = supabase.table("todos").insert({"name":"Item 2"}).execute()
#print(data)

# Update data
#data = supabase.table("todos").update({"name": "Get milk"}).eq("id", 1).execute()

# Delete data
data = supabase.table("todos").delete().eq("id", 1).execute()