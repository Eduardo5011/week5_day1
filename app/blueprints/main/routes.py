from flask import render_template, request
import requests
from .forms import PokeForm
from flask_login import login_required
from .import bp as main





@main.route("/", methods = ['GET'])
def index():
    return render_template('index.html.j2')


@main.route('/pokeapi', methods=['GET', 'POST'])  
@login_required
def pokeapi():
    form = PokeForm()
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
            return render_template('pokeapi.html.j2', information=poke_info, form=form)

        else:
            
            return " Houston we have a problem "   

    return render_template('pokeapi.html.j2', form=form)