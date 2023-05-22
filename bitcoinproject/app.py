#!/usr/bin/env python
#shalom

import requests  # Importing the requests module to make HTTP requests
from flask import Flask, render_template  # Importing the Flask class and the render_template function

app = Flask(__name__)  # Creating a Flask application

@app.route('/')  # Decorator for the root URL
def index():
    return render_template('index.html')  # Render the 'index.html' template

@app.route('/bitcoin')  # Decorator for the '/bitcoin' URL
def get_bitcoin_rate():
    try:
        # Fetch Bitcoin rate from CoinGecko API
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
        data = response.json()  # Convert the response to JSON format
        bitcoin_rate = data['bitcoin']['usd']  # Extract the Bitcoin rate from the JSON response
        return f'Bitcoin rate: ${bitcoin_rate}'  # Return the Bitcoin rate as a string
    except requests.exceptions.RequestException as e:
        return f'Error: {str(e)}'  # Return an error message if there is an exception

@app.route('/ethereum')  # Decorator for the '/ethereum' URL
def get_ethereum_rate():
    try:
        # Fetch Ethereum rate from CoinGecko API
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
        data = response.json()  # Convert the response to JSON format
        ethereum_rate = data['ethereum']['usd']  # Extract the Ethereum rate from the JSON response
        return f'Ethereum rate: ${ethereum_rate}'  # Return the Ethereum rate as a string
    except requests.exceptions.RequestException as e:
        return f'Error: {str(e)}'  # Return an error message if there is an exception

if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask development server
