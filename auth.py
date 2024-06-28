from sqlalchemy import create_engine
from supabase import create_client, Client
import psycopg2


database_url = "postgresql://postgres.mmsucpjcvccdxjhymgrc:Elidevia2023!@aws-0-eu-central-1.pooler.supabase.com:6543/postgres"

engine = create_engine(database_url)

try:
    with engine.connect() as conn:
        print("Connected to the database.")
except Exception as e:
    print(f"Unable to connect to the database: {e}")

supabaseUrl: str = "https://mmsucpjcvccdxjhymgrc.supabase.co"
supabaseKey: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1tc3VjcGpjdmNjZHhqaHltZ3JjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTk0NzU1MTcsImV4cCI6MjAzNTA1MTUxN30.dyGLXnPKw4LJZhhU-Mxql0Fhlw-pKFgrapHQUtsZ5tg"

supabase = create_client(supabaseUrl, supabaseKey)

def signup(email, password):
    """Inscription d'un nouvel utilisateur."""
    user, error = supabase.auth.sign_up({
        "email": email,
        "password": password
    })
    if error:
        # Gérez l'erreur ici
        print(error)
    else:
        print("User signed up successfully.")

def login(email, password):
    """Connexion d'un utilisateur."""
    user, error = supabase.auth.sign_in(email=email, password=password)
    if error:
        print(f"Erreur de connexion : {error.message}")
    else:
        print("Connexion réussie :", user)

# Exemple d'utilisation
email = "Abtest25@domaine.com"
password = "motdepasse"

# Inscription
signup(email, password)

# Connexion
login(email, password)