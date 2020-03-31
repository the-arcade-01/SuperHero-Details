from flask import Flask, render_template, url_for, redirect, session, request
from flask_sqlalchemy import SQLAlchemy
import json
import requests

app = Flask(__name__)

access_token = '503983410507122'

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        get_name = request.form['typehero']
        base_url = f'https://superheroapi.com/api/{access_token}/search/{get_name}'
        r = requests.get(base_url)
        data = r.json()
        results = data['results'][0]
        name = results['name']
        image = results['image']['url']
        biography = results['biography']
        return render_template('index.html',name = name,image = image,biography = biography)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
