
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

@api.route('/api/netflix_titles/update_title/')
class UpdateNetflixTitles(Resource):

    parser = api.parser()
    parser.add_argument("id", type=str, help="id is required", required=True)
    parser.add_argument("show_id", type=str, help="show_id")
    parser.add_argument("type", type=str, help="show_id is required", required=True)
    parser.add_argument("title", type=str, help="type is required", required=True)
    parser.add_argument("director", type=str, help="type is required", required=True)
    parser.add_argument("country", type=str, help="type is required", required=True)
    parser.add_argument("date_added", type=str, help="type is required", required=True)
    parser.add_argument("release_year", type=str, help="type is required", required=True)
    parser.add_argument("rating", type=str, help="type is required", required=True)
    parser.add_argument("duration", type=str, help="type is required", required=True)
    parser.add_argument("listed_in", type=str, help="type is required", required=True)
    parser.add_argument("description", type=str, help="type is required", required=True)
    parser.add_argument("cast", type=str, help="cast/actors of the title title", required=False)

    @api.expect(parser)
    def put(self):
        try:
            request_data=self.parser.parse_args(strict=True)
            NetflixTitle.update_title(request_data)
            return 200
        except Exception as e:
            return {"msg":str(e)}

@api.route('/api/netflix_titles/create_title/')
class CreateNetflixTitles(Resource):

    parser = api.parser()
    parser.add_argument("show_id", type=str, help="show id", required=False)
    parser.add_argument("type", type=str, help="title type", required=False)
    parser.add_argument("title", type=str, help="title of the title", required=True)
    parser.add_argument("director", type=str, help="director of the title", required=False)
    parser.add_argument("country", type=str, help="country of title is hosted", required=False)
    parser.add_argument("date_added", type=str, help="date the title was added", required=False)
    parser.add_argument("release_year", type=str, help="release year of the title", required=False)
    parser.add_argument("rating", type=str, help="rating of the title", required=False)
    parser.add_argument("duration", type=str, help="duration of the title", required=False)
    parser.add_argument("listed_in", type=str, help="listed in of the title", required=False)
    parser.add_argument("description", type=str, help="description of the title", required=False)
    parser.add_argument("cast", type=str, help="cast/actors of the title title", required=False)

    @api.expect(parser)
    def post(self):
        try:
            request_data=self.parser.parse_args(strict=True)
            NetflixTitle.create_title(request_data)
            return 200
        except Exception as e:
            return {"msg":str(e)}

@api.route('/api/netflix_titles/delete_title/<string:id>')
class DeleteNetflixTitlesByDescription(Resource):
    def delete(self, id):
        try:
            NetflixTitle.delete_title(id=id)
            return 200
        except Exception as e:
            return {"msg":str(e)}
