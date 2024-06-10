from dotenv import load_dotenv
load_dotenv()

import os
import time
from supabase import create_client, Client
from gotrue.errors import AuthApiError

# Load environment variables
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# Create a Supabase client
supabase: Client = create_client(url, key)

# Define the email and password for the new user
email = "dhananjay@prodt.co"
password = "Dhananjay@1234"

# user = supabase.auth.sign_up({
#             "email": email,
#                 "password": password
#             })

session = supabase.auth.sign_in_with_password({ "email": email, "password": password })
            
