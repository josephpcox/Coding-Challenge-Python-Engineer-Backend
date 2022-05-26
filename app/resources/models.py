from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from sqlalchemy.sql import text
# from sqlalchemy.orm import relationship, backref
import json

db = SQLAlchemy()

                      
class NetflixTitle(db.Model):
    __tablename__ = 'netflix_titles'
    show_id = db.Column(db.Int(30), primary_key=True)
    show_id = db.Column(db.String(30))
    type = db.Column(db.String)
    title = db.Column(db.String)
    director = db.Column(db.String)
    cast = db.Column(db.String)
    country = db.Column(db.String)
    date_added = db.Column(db.String)
    release_year = db.Column(db.String)
    rating = db.Column(db.String)
    duration = db.Column(db.String)
    listed_in = db.Column(db.String)
    description = db.Column(db.String)

    def __init__self(show_id,
                     type,
                     title,
                     director,
                     cast,
                     country,
                     date_added,
                     release_year,
                     rating,
                     duration,
                     listed_in,
                     description
    ):
        self.show_id = show_id
        self.type = type
        self.title = title
        self.director = director
        self.cast = cast
        self.country = country
        self.date_added = date_added
        self.release_year = release_year
        self.rating - rating
        self.duration = duration
        self.listed_in = listed_in
        self.description = description

    def save_title(self):
        db.session.add(self)
        db.session.commit()

    def delete_title(self):
        db.session.delete(self)
        db.session.commit()
    
    def get_json(self):
        return {
        "id": self.id,
        "show_id": self.show_id,
        "type": self.type,
        "title": self.title,
        "director": self.director,
        "cast": self.cast,
        "country": self.country,
        "date_added": self.date_added,
        "release_year": self.release_year,
        "rating": self.rating,
        "duration": self.duration,
        "listed_in": self.listed_in,
        "description": self.description
        }
    
    @classmethod
    def create_title(cls, dict_title):
        netflix_title = NetflixTitle(**dict_title)
        netflix_title.save_title()
    
    @classmethod
    def delete_title(cls, show_id):
        netflix_title = cls.query.filter_by(id=id)
        netflix_title.delete_title()

    @classmethod
    def update_title(cls, dict_title):
        result = cls.query.filter_by(id = dict_title['id'])
        result[0].show_id = dict_title['show_id']
        result[0].type = dict_title['type']
        result[0].title = dict_title['title']
        result[0].director = dict_title['director']
        result[0].cast = dict_title['cast']
        result[0].country = dict_title['country']
        result[0].date_added = dict_title['date_added']
        result[0].release_year = dict_title['release_year']
        result[0].rating = dict_title['rating']
        result[0].duration = dict_title['duration']
        result[0].listed_in = dict_title['listed_in']
        result[0].description = dict_title['description']
        result[0].save_title()
    
    @classmethod
    def get_all_titles(cls):
        result = []
        for title in cls.query.order_by(text("id asc")).all():
            result.append(title.get_json())
        return result

    @classmethod
    def get_by_type(cls, type):
        result = []
        for title in cls.query.filter_by(type=type):
            result.append(title.get_json())
        return result
    
    @classmethod
    def get_by_title(cls, title):
        result = []
        for title in cls.query.filter_by(title=title):
            result.append(title.get_json())
        return result

    @classmethod
    def get_by_director(cls, director):
        result = []
        for title in cls.query.filter_by(director=director):
            result.append(title.get_json())
        return result
    
    @classmethod
    def get_by_cast(cls, cast):
        result = []
        for title in cls.query.filter_by(cast=cast):
            result.append(title.get_json())
        return result

    @classmethod
    def get_by_country(cls, country):
        result = []
        for title in cls.query.filter_by(country=country):
            result.append(title.get_json())
        return result

    @classmethod
    def get_by_date_added(cls, date_added):
        result = []
        for title in cls.query.filter_by(date_added=date_added):
            result.append(title.get_json())
        return result

    @classmethod
    def get_by_release_year(cls, release_year):
        result = []
        for title in cls.query.filter_by(release_year=release_year):
            result.append(title.get_json())
        return result

    @classmethod
    def get_by_rating(cls, rating):
        result = []
        for title in cls.query.filter_by(rating=rating):
            result.append(title.get_json())
        return result

    @classmethod
    def get_by_duration(cls, duration):
        result = []
        for title in cls.query.filter_by(duration=duration):
            result.append(title.get_json())
        return result

    @classmethod
    def get_by_listed_in(cls, listed_in):
        result = []
        for title in cls.query.filter_by(listed_in=listed_in):
            result.append(title.get_json())
        return result

    @classmethod
    def get_by_description(cls, description):
        result = []
        for title in cls.query.filter_by(description=description):
            result.append(title.get_json())
        return result

    

    


