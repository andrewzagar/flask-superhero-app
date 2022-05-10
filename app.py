from flask import Flask, render_template, request, jsonify
import requests
import logging
import os
app = Flask(__name__)

 # log = logging.getLogger(__name__)

superhero_api_key = os.environ.get("SUPERHERO_API_KEY")
if not superhero_api_key:
    raise Exception("SUPERHERO_API_KEY must be set as an env var. See readme.")

@app.route('/superhero_search', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['GET'])
def submit_form():

    url = "https://superhero-search.p.rapidapi.com/api/"

    headers = {
	    "X-RapidAPI-Key": superhero_api_key
    }
    hero_type = request.args.get('Hero_Villan')
    hero_name = request.args.get('content')
    if True:
        response = requests.request("GET", url, headers=headers, params={hero_type: hero_name})
        # From api
        if response.text == 'Hero Not Found':
            response = {"error": "not_found"}
        else:
            response = response.json()
    else:
        response = {'id': 644, 'name': 'Superman', 'slug': '644-superman', 'powerstats': {'intelligence': 94, 'strength': 100, 'speed': 100, 'durability': 100, 'power': 100, 'combat': 85}, 'appearance': {'gender': 'Male', 'race': 'Kryptonian', 'height': ["6'3", '191 cm'], 'weight': ['225 lb', '101 kg'], 'eyeColor': 'Blue', 'hairColor': 'Black'}, 'biography': {'fullName': 'Clark Kent', 'alterEgos': 'Superman Prime One-Million', 'aliases': ['Clark Joseph Kent', 'The Man of Steel', 'the Man of Tomorrow', 'the Last Son of Krypton', 'Big Blue', 'the Metropolis Marvel', 'the Action Ace'], 'placeOfBirth': 'Krypton', 'firstAppearance': 'ACTION COMICS #1', 'publisher': 'Superman Prime One-Million', 'alignment': 'good'}, 'work': {'occupation': 'Reporter for the Daily Planet and novelist', 'base': 'Metropolis'}, 'connections': {'groupAffiliation': 'Justice League of America, The Legion of Super-Heroes (pre-Crisis as Superboy); Justice Society of America (pre-Crisis Earth-2 version); All-Star Squadron (pre-Crisis Earth-2 version)', 'relatives': 'Lois Lane (wife), Jor-El (father, deceased), Lara (mother, deceased), Jonathan Kent (adoptive father), Martha Kent (adoptive mother), Seyg-El (paternal grandfather, deceased), Zor-El (uncle, deceased), Alura (aunt, deceased), Supergirl (Kara Zor-El, cousin), Superboy (Kon-El/Conner Kent, partial clone)'}, 'images': {'xs': 'https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/644-superman.jpg', 'sm': 'https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/644-superman.jpg', 'md': 'https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/644-superman.jpg', 'lg': 'https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/644-superman.jpg'}}
    return render_template('index.html', superhero_data=response)

if __name__ == "__main__":
    
    app.run(debug=True)