from supabase import create_client, Client

url: str = "aws-0-eu-central-1.pooler.supabase.com"
key: str = "Elidevia2023"
supabase: Client = create_client(url, key)

email = "samu.abid@gmail.com"
password = "SamuelMDP"

user = supabase.auth.sign_up(email, password)

if response["status_code"] == 200:
    print("User signup successfully!")
else:
    print("Signup failed.")