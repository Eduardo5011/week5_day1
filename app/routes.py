from flask import render_template, request
import requests
from app import app




@app.route("/", methods = ['GET'])
def index():
    return render_template('index.html.j2')


@app.route('/pokemon', methods = ['GET'])  
def pokemon():
    my_pokemon = ["pikachu", "charizard", "mudkip", "blaziken", "cubone"]

    return render_template("pokemon.html.j2", pokemon = my_pokemon)

@app.route('/login', methods=['GET', 'POST'])  
def login():
    if request.method == 'POST':
        email = request.form.get("email").lower()
        password = request.form.get("password")
        if email in app.config.get("REGISTERED_USERS") and password == app.config.get("REGISTERED_USERS").get(email).get('password'):
            return f"Login success Welcome {app.config.get('REGISTERED_USERS')(email).get('name')}"
        error_string = "Invalid Email password combo"    
        return render_template('login.html.j2', error = error_string)

    return render_template('login.html.j2')





@app.route('/pokeapi', methods=['GET', 'POST'])  
def pokeapi():
    if request.method == 'POST':
        names = request.form.get('name')
        url = f"https://pokeapi.co/api/v2/pokemon/{names}"
        response_name = requests.get(url)
        if response_name.ok:
            data = response_name.json()
            poke_info = []
            poke_team = {
                "name":data["forms"][0]["name"],
                "ability": data["abilities"][0]["ability"]["name"],
                "base_experience":data["base_experience"],
                "base_hp":data["stats"][0]["base_stat"],
                "base_attack":data["stats"][1]["base_stat"],
                "base_defense":data["stats"][2]["base_stat"],   
                "front_shiny":data["sprites"]["front_shiny"],                
            }
            poke_info.append(poke_team)   
            print(poke_info) 
            return render_template('pokeapi.html.j2', information=poke_info)

        else:
            
            return " Houston we had a problem "   

    return render_template('pokeapi.html.j2')
        
        
       
        


                      
       


        
       
   