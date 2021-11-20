from flask import render_template, request, flash, redirect, url_for
import requests
from .forms import PokeForm
from flask_login import login_required, current_user
from .import bp as main
from app.models import Pokemon






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
            new_pokemon_object = Pokemon()
            new_pokemon_object.from_dict(poke_team)
            new_pokemon_object.save()

            poke_info.append(poke_team)   
            print(poke_info) 
            return render_template('pokeapi.html.j2', information=poke_info, form=form)

        else:
            
            return " Houston we have a problem "   

    return render_template('pokeapi.html.j2', form=form)

@main.route('/poke_team', methods=['GET'])  
@login_required
def poke_team():
    pokemon = Pokemon.query.all()
    return render_template('poketeam.html.j2', pokemon=pokemon)




# @main.route('/attack/ <int:id>')
# @login_required
# def attack(id):
#     user_to_attack = Pokemon.query.get(id)
#     current_user.attack(user_to_attack)
#     flash(f"You have attacked {user_to_attack.poke.names}", 'success')
#     return redirect(url_for('main.poketeam'))


@main.route('/remove/ <int:id>')
@login_required
def remove(id):
    user_to_remove = Pokemon.query.get(id)
    current_user.attack(user_to_remove)
    flash(f"pokemon has been removed {user_to_remove.poke.names}", 'success')
    return redirect(url_for('main.poketeam'))    




