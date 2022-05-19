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

# @api.route('/product/get_all')
# class GetProduct(Resource):
#     response = {
#         200: "OK",
#         403: "Database Error"
#     }
#     api.doc(response)
#     @requires_auth
#     def get(self):
#         try:
#             result = Product.get_products()
#         except Exception as e:
#             return {'msg': str(e)}, 403
#         return result, 200

# @api.route('/security/create/<string:category_code>/<int:security_level>')
# class CreateSecurity(Resource):
#     response = {
#         200: "OK",
#         400: "Bad Input. Required fileds are missing or are malformed",
#         403: "Database error"
#     }
#     @requires_auth
#     def post(self, category_code, security_level):
#         if all([security_level,category_code]) is False:
#             return {'msg':self.response[400]},400
#         try:
#             dict_security = {'category_code': category_code, 'security_level': security_level}
#             Security.create_security(dict_security)
#         except Exception as e:
#             return {'msg':str(e)},403
#         return 200


# @api.route('/security/get_all')
# class GetSecurities(Resource):
#     response = {
#         200: "OK",
#         400: "Bad Input. Required fileds are missing or are malformed",
#         403: "Database error"
#     }
#     @requires_auth
#     def get(self):
#         try:
#             result = Security.get_securities()
#         except Exception as e:
#             return {'msg': str(e)}, 403
#         return result, 200


# @api.route('/category/create/<string:category_name>/<string:category_code>')
# class CreateCategory(Resource):
#     response = {
#         200:"OK",
#         400:"Bad Input",
#         500:"Database Error"
#     }
#     api.doc(response)
#     @requires_auth
#     def post(self, category_name, category_code):
#         if category_name is None:
#             return {'msg':self.response[400]},400
#         try:
#             dict_category = {'category_name': category_name, 'category_code': category_code}
#             Category.create_category(dict_category)
#         except Exception as e:
#             return {'msg':str(e)},500
#         return 200

# @api.route('/category/get_all')
# class GetCategories(Resource):
#     response = {
#         200: "OK",
#         403: "Database Error"
#     }
    
#     api.doc(response)
#     @requires_auth
#     def get(self):
#         try:
#             result = Category.get_categories()
#         except Exception as e:
#             return {'msg': str(e)}, 403
#         return result, 200


# @api.route('/vendor/create/<string:vendor_name>/<string:vendor_code>')
# class CreateVendor(Resource):
#     response = {
#         200: "OK",
#         400: "Bad Input",
#         500: "Database Error"
#     }
#     api.doc(response)
#     @requires_auth
#     def post(self, vendor_name, vendor_code):
#         if all([vendor_name, vendor_code]) is False:
#             return {'msg': self.response[400]}, 400
#         try:
#             dict_vendor = {'vendor_name': vendor_name,
#                              'vendor_code': vendor_code
#             }
#             Vendor.create_vendor(dict_vendor)
#         except Exception as e:
#             return {'msg': str(e)}, 500
#         return 200


# @api.route('/vendor/get_all')
# class GetVendors(Resource):
#     response = {
#         200: "OK",
#         403: "Database Error"
#     }
#     api.doc(response)
#     @requires_auth
#     def get(self):
#         try:
#             result = Vendor.get_vendors()
#         except Exception as e:
#             return {'msg': str(e)}, 403
#         return result, 200
