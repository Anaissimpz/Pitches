from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pitch = db.relationship('Pitch', backref = 'user', lazy='dynamic')
    comment = db.relationship('Comment',backref = 'user',lazy='dynamic')
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255)) 

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    
    def __repr__(self):
        return f'User {self.username}'

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))   

class Pitch(db.Model):
    __tablename__ = 'pitch'

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    description = db.Column(db.String(255))
    category = db.Column(db.String(255))
    comment = db.relationship('Comment',backref = 'pitch',lazy='dynamic')


    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def clear_pitches(cls):
        Pitch.search_pitches.clear()
    @classmethod
    def get_pitche(cls,pitch_id):
        pitche=Pitch.query.filter_by(user_id=id).all()
        return pitche
    @classmethod 
    def get_pitches(cls):
        pitches = Pitch.query.filter_by().all()
        return pitches
    


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitch.id"))
    content = db.Column(db.String(255))

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()


    @classmethod
    def get_pitchz(cls):
        pitchz=Pitch.query.filter_by(user_id=id).all()
        return pitchz

    @classmethod 
    def get_pitche(cls):
        pitche = Pitch.query.filter_by().all()
        return pitche 
    


class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'

    id = db.Column(db.Integer,primary_key = True)
    pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    
