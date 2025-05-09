# Flask API Backend

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'API Analisis Sentimen Berjalan'