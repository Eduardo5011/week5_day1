from app import db
from flask_login import UserMixin 
from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash
from app import login

#added 11/02/21---------
pokemon =db.table(
    'pokemons',
    db.Column('add_pokemon_id', db.Integer),
    db.Column('remove_pokemon_id', db.Integer)
)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(200), unique=True, index=True)
    password = db.Column(db.String(200))
    icon = db.Column(db.Integer)
    created_on = db.Column(db.DateTime, default=dt.utcnow)
    add_pokemon = db.relationship('AddPokemon', backref='author', lazy='dynamic')  #added 11/02/21
    

    def __repr__(self):
        return f'<User: {self.id} | {self.email}>'

    def from_dict(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data["email"]
        self.icon = data['icon']
        self.password = self.hash_password(data['password'])

    
    def hash_password(self, original_password):
        return generate_password_hash(original_password)

    
    def check_hashed_password(self, login_password):
        return check_password_hash(self.password, login_password)

    
    def get_icon_url(self):
        return 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{self.icon}.png'
    

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

    #added 11/02/21---------
class AddPokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    date_updated = db.Column(db.DateTime, onupdate=dt.utcnow) 
    pokemon = db.Column(db.text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def save(self):
        db.session.add(self) 
        db.session.commit()


    # added 11/02/21---------
    def edit(self, new_pokemon):
        self.pokemon=new_pokemon    
        self.save

    # added 11/02/21---------
    def __repr__(self):
        return f'<id:{self.id} | AddPokemon: {self.pokemon[:15]}">'


         