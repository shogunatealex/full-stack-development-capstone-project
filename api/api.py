import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models.models import setup_db, Actor, Movie, db
from auth.auth import AuthError, requires_auth


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)


    @app.route('/actors')
    @requires_auth('read:actors')
    def get_actors(payload):
        actors = Actor.query.all()
        data = {}
        for actor in actors:
            data[actor.id] = actor.format()
        return jsonify({
            "success": True,
            "actors": data
            })


    @app.route('/actors', methods=['POST'])
    @requires_auth('create:actor')
    def post_actor(payload):
        req = request.get_json()
        body = {}
        try:
            actor = Actor(name=req['name'],
                        age=req['age'],
                        gender=req['gender'],
                        )
            Actor.insert(actor)
            body['name'] = req['name']
            body['age'] = req['age']
            body['gender'] = req['gender']
            body["id"] = actor.id
        except Exception:
            db.session.close()
            abort(422)
        return jsonify({
            "success": True,
            "actors": 
            {
                body["id"]: body
                
            } 
        }) 


    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(payload, actor_id):
        error = False
        try:
            effected_rows = Actor.query.filter_by(id=actor_id).delete()
            if(effected_rows < 1):
                abort(404) 
            db.session.commit()
        except Exception:
            db.session.rollback()
            error = True
        finally:
            db.session.close()
        if error:
            abort(404)
        else:
            return jsonify({
                'success': True,
                "delete" : actor_id
            })

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('edit:actor')
    def edit_actor(payload, actor_id):
        old_actor = Actor.query.get(actor_id)
        if not old_actor:
            abort(404)
        req = request.get_json()

        body = {}
        try:
            if 'name' in req:
                old_actor.name = req['name']
            if 'age' in req:
                old_actor.age = req['age']
            if 'gender' in req:
                old_actor.gender = req['gender']
            db.session.commit()
            body = old_actor.format()
        except Exception:
            db.session.close()
            abort(422)
        finally:
            db.session.close()
        return jsonify({
            "success": True,
            "actors": 
            {
                body["id"]: body
            } 
        }) 


    @app.route('/movies')
    @requires_auth('read:movies')
    def get_movies(payload):
        movies = Movie.query.all()
        data = {}
        for movie in movies:
            data[movie.id] = movie.format()
        return jsonify({
            "success": True,
            "movies": data
            })


    @app.route('/movies', methods=['POST'])
    @requires_auth('create:movie')
    def post_movie(payload):
        req = request.get_json()
        body = {}
        try:
            movie = Movie(title=req['title'],
                        release_date=req['release_date'],
                        )
            Movie.insert(movie)
            body['title'] = req['title']
            body['release_date'] = req['release_date']
            body["id"] = movie.id
        except Exception:
            db.session.close()
            abort(422)
        finally:
            db.session.close()
        return jsonify({
            "success": True,
            "movies": 
            {
                body["id"]: body
                
            } 
        }) 


    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(payload, movie_id):
        error = False
        try:
            effected_rows = Movie.query.filter_by(id=movie_id).delete()
            if(effected_rows < 1):
                abort(404) 
            db.session.commit()
        except Exception:
            db.session.rollback()
            error = True
        finally:
            db.session.close()
        if error:
            abort(404)
        else:
            return jsonify({
                'success': True,
                "delete" : movie_id
            })



    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('edit:movie')
    def edit_movie(payload, movie_id):
        old_movie = Movie.query.get(movie_id)
        if not old_movie:
            abort(404)
        req = request.get_json()

        body = {}
        try:
            if 'title' in req:
                old_movie.title = req['title']
            if 'release_date' in req:
                old_movie.release_date = req['release_date']
            db.session.commit()
            body = old_movie.format()
        except Exception:
            db.session.close()
            abort(422)
        finally:
            db.session.close()
        return jsonify({
            "success": True,
            "actors": 
            {
                body["id"]: body
            } 
        }) 


    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({
        "success": False,
        "message": "The resource could not be found",
        "status_code": 404
        }), 404


    @app.errorhandler(422)
    def improperlyFormatted(error):
        return jsonify({
        "success": False,
        "message": "There is something wrong with the request",
        "status_code": 422
        }), 422
    
    @app.errorhandler(AuthError)
    def authentification_failed(AuthError):
        return jsonify({
            "success": False,
            "error": AuthError.status_code,
            "message": AuthError.error
        }), AuthError.status_code

    return app