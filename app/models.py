from app import db

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    name = db.Column(db.String(64), index=True)
    address = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    country = db.Column(db.Strin(64))
    fax = db.Column(db.String(20))
    zip_code = db.Column(db.String(20))
    alcohol = db.Column(db.String(20))
    smoking_area = db.Column(db.String(20))
    dress_code = db.Column(db.String(20))
    accessibility = db.Column(db.String(20))
    price = db.Column(db.String(20))
    url = db.Column(db.String(128))
    ambience = db.Column(db.String(20))
    franchise = db.Column(db.Boolean)
    area = db.Column(db.String(20))
    other_services = db.Column(db.String(128))
    
    def __repr__(self):
        return 'Restaurant {}'.format(self.name)