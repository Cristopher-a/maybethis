from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
from supabase import create_client, Client

# ----------------------------
# Configuración Supabase
# ----------------------------
SUPABASE_URL = "https://rhttqmtzcmwilzshnxwq.supabase.co" 
SUPABASE_KEY = "tu_supabase_key_aqui"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ----------------------------
# Configuración Flask
# ----------------------------
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'
