from cgitb import reset
from distutils.log import error
from flask import Flask
from app.authentication import auth
from flask_restplus import Resource, Api
from app.resources.models import NetflixTitle
from app.authentication.auth import AuthError,requires_auth
from flask_cors import cross_origin

api = Api()

@api.route('/api/netflix_titles/get_all')
class GetAllNetflixTitles(Resource):
    def get(self):
        try:
            result = NetflixTitle.get_all_titles()
            return result
        except Exception as e:
            return {"msg": str(e)} 
@api.route('/api/netflix_titles/get_by_title_name/<string:title_name>')
class GetNetflixTitles(Resource):
    def get(self, title_name):
        try:
            result = NetflixTitle.get_by_title(title=title_name)
            return result
        except Exception as e:
            return {"msg":str(e)}
@api.route('/api/netflix_titles/get_by_type/<string:type>')
class GetNetflixTitlesByType(Resource):
    def get(self, type):
        try:
            result = NetflixTitle.get_by_type(type=type)
            return result
        except Exception as e:
            return {"msg":str(e)}

@api.route('/api/netflix_titles/get_by_director/<string:director>')
class GetNetflixTitlesByDirector(Resource):
    def get(self, director):
        try:
            result = NetflixTitle.get_by_director(director=director)
            return result
        except Exception as e:
            return {"msg":str(e)}

@api.route('/api/netflix_titles/get_by_cast/<string:cast>')
class GetNetflixTitlesByCast(Resource):
    def get(self, cast):
        try:
            result = NetflixTitle.get_by_cast(cast=cast)
            return result
        except Exception as e:
            return {"msg":str(e)}
@api.route('/api/netflix_titles/get_by_country/<string:country>')
class GetNetflixTitlesByCountry(Resource):
    def get(self, country):
        try:
            result = NetflixTitle.get_by_country(country=country)
            return result
        except Exception as e:
            return {"msg":str(e)}
@api.route('/api/netflix_titles/get_by_date_added/<string:date>')
class GetNetflixTitlesByDateAdded(Resource):
    def get(self, date):
        try:
            result = NetflixTitle.get_by_date_added(date_added=date)
            return result
        except Exception as e:
            return {"msg":str(e)}
            
@api.route('/api/netflix_titles/get_by_release_year/<string:year>')
class GetNetflixTitlesByReleaseYear(Resource):
    def get(self, year):
        try:
            result = NetflixTitle.get_by_release_year(release_year=year)
            return result
        except Exception as e:
            return {"msg":str(e)}

@api.route('/api/netflix_titles/get_by_rating/<string:rating>')
class GetNetflixTitlesByRating(Resource):
    def get(self, rating):
        try:
            result = NetflixTitle.get_by_rating(rating=rating)
            return result
        except Exception as e:
            return {"msg":str(e)}

@api.route('/api/netflix_titles/get_by_duration/<string:duration>')
class GetNetflixTitlesByDuration(Resource):
    def get(self, duration):
        try:
            result = NetflixTitle.get_by_duration(duration=duration)
            return result
        except Exception as e:
            return {"msg":str(e)}

@api.route('/api/netflix_titles/get_by_listed_in/<string:listed_in>')
class GetNetflixTitlesByListedIn(Resource):
    def get(self, listed_in):
        try:
            result = NetflixTitle.get_by_listed_in(listed_in=listed_in)
            return result
        except Exception as e:
            return {"msg":str(e)}

@api.route('/api/netflix_titles/get_by_description/<string:description>')
class GetNetflixTitlesByDescription(Resource):
    def get(self, description):
        try:
            result = NetflixTitle.get_by_description(description=description)
            return result
        except Exception as e:
            return {"msg":str(e)}
