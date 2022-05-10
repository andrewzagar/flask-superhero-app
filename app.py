from flask import Flask, render_template, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import os

app = Flask(__name__)
auth = HTTPBasicAuth()

# Checking for enviornment variables
superhero_api_key = os.environ.get("SUPERHERO_API_KEY")
if not superhero_api_key:
    raise Exception("SUPERHERO_API_KEY must be set as an env var. See readme.")
app_api_key = os.environ.get("APP_API_KEY")
if not app_api_key:
    raise Exception("APP_API_KEY must be set as an env var. See readme.")

# User data
users = {
    "user": generate_password_hash(app_api_key),
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

# Landing page for search
@app.route('/superhero_search', methods=['GET'])
def index():
    return render_template('index.html')

# Send search to api and display data
@app.route('/submit_form', methods=['GET'])
@auth.login_required
def submit_form():

    url = "https://superhero-search.p.rapidapi.com/api/"

    headers = {
	    "X-RapidAPI-Key": superhero_api_key
    }
    hero_type = request.args.get('Hero_Villain')
    hero_name = request.args.get('content')

    if not hero_name:
        output = {"error": "no entry"}
    else:
        response = requests.request("GET", url, headers=headers, params={hero_type: hero_name})

        if response.text == 'Hero Not Found':
            output = {"error": "not_found"}
        elif response.status_code != 200:
            output = {"error": f"Superhero APi error: {response.text}"} 
        else:
            output = response.json()
    return render_template('index.html', superhero_data=output)

if __name__ == "__main__":
    app.run(debug=True)