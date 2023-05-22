#!/usr/bin/env python
#shalom

import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bitcoin')
def get_bitcoin_rate():
    try:
        # Fetch Bitcoin rate from CoinGecko API
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
        data = response.json()
        bitcoin_rate = data['bitcoin']['usd']
        return f'Bitcoin rate: ${bitcoin_rate}'
    except requests.exceptions.RequestException as e:
        return f'Error: {str(e)}'

@app.route('/ethereum')
def get_ethereum_rate():
    try:
        # Fetch Ethereum rate from CoinGecko API
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
        data = response.json()
        ethereum_rate = data['ethereum']['usd']
        return f'Ethereum rate: ${ethereum_rate}'
    except requests.exceptions.RequestException as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
