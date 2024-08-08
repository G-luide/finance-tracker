from flask import Flask, jsonify
from flask_cors import CORS
import requests
import config

app = Flask(__name__)
CORS(app)

# Defineeri LHV API detailid
LHV_API_BASE_URL = 'https://api.sandbox.lhv.eu/psd2/v1'
AUTH_TOKEN = 'Bearer Liis-MariMnnik'  # Kasuta autoriseeritud tokenit
CERTIFICATE_PATH = config.CERTIFICATE_PATH
PRIVATE_KEY_PATH = config.PRIVATE_KEY_PATH

@app.route('/')
def index():
    return 'Welcome to the Finance Tracker!'

@app.route('/user-data')
def get_user_data():
    headers = {
        'Authorization': AUTH_TOKEN,
        'Consent-ID': '520189d2-e8bb-48ae-8221-45bed93b7316',  # Kasuta uut Consent-ID-d
        'X-Request-ID': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',  # Kasuta uut X-Request-ID-d
        'Accept': 'application/hal+json;charset=UTF-8'
    }
    
    try:
        response = requests.get(f'{LHV_API_BASE_URL}/accounts?onlyActive=true', headers=headers, cert=(CERTIFICATE_PATH, PRIVATE_KEY_PATH))
        response.raise_for_status()  # Kontrollib HTTP vigu
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(ssl_context=(CERTIFICATE_PATH, PRIVATE_KEY_PATH))

