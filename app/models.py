from flask import url_for
from app import db

class JSONifyCollectionMixin(object):
    @staticmethod
    def to_collection(query, page, per_page, endpoint, **kwargs):
        pagin = query.paginate(page, per_page, False)
        data = {
            'items': [item.to_dict() for item in pagin.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_page': pagin.pages,
                'total_items': pagin.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page, **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if pagin.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if pagin.has_prev else None
            }
        }
        return data
    
class Restaurant(JSONifyCollectionMixin, db.Model):
    placeID = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    name = db.Column(db.String(64), index=True)
    address = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    country = db.Column(db.String(64))
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
    
    def to_dict(self):
        data = {
            'placeID': self.placeID,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'name': self.name,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'country': self.country,
            'fax': self.fax,
            'zip_code': self.zip_code,
            'alcohol': self.alcohol,
            'smoking_area': self.smoking_area,
            'dress_code': self.dress_code,
            'accessibility': self.accessibility,
            'price': self.price,
            'url': self.url,
            'ambience': self.ambience,
            'franchise': self.franchise,
            'area': self.area,
            'other_services': self.other_services
        }
        return data