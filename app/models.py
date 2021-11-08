from app import db
from flask_login import UserMixin 
from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash
from app import login

#added 11/02/21---------



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(200), unique=True, index=True)
    password = db.Column(db.String(200))
    icon = db.Column(db.Integer)
    created_on = db.Column(db.DateTime, default=dt.utcnow)
    posts = db.relationship('Pokemon', backref='author', lazy='dynamic')  #added 11/02/21
    
    

    
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

    def save(self):
        db.session.add(self) 
        db.session.commit()    

    
    def get_icon_url(self):
        return 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{self.icon}.png'

    def __repr__(self):
        return f'<User: {self.id} | {self.email}>'    
    

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

    #added 11/02/21---------
class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique =True, index=True)
    ability = db.Column(db.String(100))
    base_experience = db.Column(db.Integer)
    base_hp = db.Column(db.Integer)
    base_attack = db.Column(db.Integer)
    base_defense = db.Column(db.Integer)
    front_shiny = db.Column(db.String(600))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    #added 11/02/21---------
    def from_dict(self, data):
        self.name = data["name"]
        self.ability = data["ability"]
        self.base_experience = data["base_experience"]
        self.base_hp = data["base_hp"]
        self.base_attack = data["base_attack"]
        self.base_defense = data["base_defense"]
        self.front_shiny = data["front_shiny"]



    def save(self):
        db.session.add(self) 
        db.session.commit()


    # added 11/02/21---------
    def __repr__(self):
        return f'<id:{self.id} | Pokemon: {self.name}">'

    
         