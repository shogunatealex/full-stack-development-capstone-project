import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from .models.models import setup_db, Actor, Movie, db
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)


@app.route('/actors')
@requires_auth('read:actors')
def get_actors():
    actors = Actor.query.all()
    data = {}
    for actor in actors:
        data[actor.id] = actor.format()
    return jsonify({
        "success": True,
        "actors": data
        })


@app.route('/actors', methods=['POST'])
@requires_auth('create:actors')
def post_actor():
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
def delete_actor(actor_id):
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
def edit_actor(actor_id):
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
def get_movies():
    movies = Movie.query.all()
    data = {}
    for movie in movies:
        data[movie.id] = movie.format()
    return jsonify({
        "success": True,
        "movies": data
        })


@app.route('/movies', methods=['POST'])
def post_movie():
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
def delete_movie(movie_id):
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
def edit_movie(movie_id):
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