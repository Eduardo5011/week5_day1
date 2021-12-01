from flask import render_template, request, flash, redirect, url_for
import requests
from .forms import PokeForm
from flask_login import login_required, current_user
from .import bp as main
from app.models import Pokemon, User







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




@main.route('/attack/<int:defender_id>')
@login_required
def attack(defender_id):
    user_attack= 0
    user_defense = 0
    defender_attack= 0
    defender_defense= 0
    
    pokemon = Pokemon.query.all()
    for poke in pokemon:
        if poke.user_id == current_user.id:
            user_attack += poke.base_attack
            user_defense += poke.base_defense
        if poke.user_id == defender_id:
            defender_attack += poke.base_attack
            defender_defense += poke.base_defense
    if user_attack > defender_defense:
        flash(f"You have won", 'success') 
        return render_template('battle.html.j2')
    elif  user_attack < defender_defense:
        flash(f"You have lost") 
        return render_template('battle.html.j2') 
    else:
        flash(f"Tie")    
    
    
    return redirect('battle.html.j2')


@main.route('/remove/<int:id>')
@login_required
def remove(id):
    pokemon_to_remove = Pokemon.query.get(id)
    pokemon_to_remove.release()
    flash(f"pokemon has been removed {pokemon_to_remove}", 'success')
    return redirect(url_for('main.poke_team'))  


@main.route('/show_users') 
@login_required
def show_users():
    users= User.query.all()   
    pokemon=Pokemon.query.all()

    return render_template('battle.html.j2', users=users, pokemon=pokemon)





