from supabase import create_client, Client

url: str = "your_supabase_url"
key: str = "your_supabase_key"
supabase: Client = create_client(url, key)

# Authenticate user
email = "user@example.com"
password = "password123"

response = supabase.auth.sign_in(email=email, password=password)

if response["status_code"] == 200:
    print("User authenticated successfully!")
else:
    print("Authentication failed.")