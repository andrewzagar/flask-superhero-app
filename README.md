
# Flask SuperHero App

    This is a flask app that takes user input, authenticates them, then pulls information from 
    Superhero Search API and displays it for the user.

    Requires an account setup with https://www.akashj.com/superhero-search-api/ to get a 
    personal X-RapidAPI-Key

## Installation

    Python3 instaliation required
    git clone https://github.com/andrewzagar/flask-superhero-app.git
    cd into project root directory
    create a virtual venv and activate
    pip install -r requirements.txt

    Define envornment variables:
        export SUPER_HERO_API_KEY = <X-RapidAPI-Key>
        export APP_API_KEY = <personal password>

    run command python app.py
    visit localhost:5000/superhero_search
    
    When prompted for auth use:
        username = user
        password = <APP_API_KEY>
