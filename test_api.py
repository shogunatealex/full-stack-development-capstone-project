import os
from os import environ
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from api import create_app
from models.models import setup_db, Movie, Actor


class CastingTestCase(unittest.TestCase):
    """This class represents the casting test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_test"
        self.database_path = "postgres://localhost:5432/casting_test"
        setup_db(self.app, self.database_path)

        self.casting_director = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVzUWZSd1FrTHhyU20zQTBSc3gzNyJ9.eyJpc3MiOiJodHRwczovL25paG9uZG8uYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzE1M2Y0NDUzZTIzMGM3MWQ5MzIyNiIsImF1ZCI6InVkYWNpdHktY2Fwc3RvbmUiLCJpYXQiOjE1OTAzMzc0ODAsImV4cCI6MTU5MDQyMzg4MCwiYXpwIjoidjRrd1hSSEsyUHV6RnFiNHFEbTFoUTVSUUZPcXcyZFoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvciIsImRlbGV0ZTphY3RvciIsImVkaXQ6YWN0b3IiLCJlZGl0Om1vdmllIiwicmVhZDphY3RvcnMiLCJyZWFkOm1vdmllcyJdfQ.Hj86AzdbXALp4JQZGLVzQBc6JdBck8XzPkmUqsAZflRYg-pNGKb69wf5z4d1y2kJ8Eo-ZbrrHcgq5nPxeVBHVMlgszbK5goI-1sPfZiv988p6G-KPBAlpocpwQAp6hiY-rRp4cZiG92rilGJx9aFw6J_kvoT9Rr_16PT6zq4JvWN5UhOzcTr0A2FRljS-IoYgG6IJTibomwD3Bj1JkZVXkAbShyM7Ii5pevwFwO742lx-W2i4ssiknPVqOzd1EmGbYEckcHei5_sww3YEFPVfsB0l_54PcZqh9pXXRV6T46X18Mv1u6p_MoYunIHUFfOrv0qCFjsqN008Coyh2Cozw"
        self.executive_producer = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVzUWZSd1FrTHhyU20zQTBSc3gzNyJ9.eyJpc3MiOiJodHRwczovL25paG9uZG8uYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzE1M2M2NTgzMGE5MGM2ZmU5YmM4MyIsImF1ZCI6InVkYWNpdHktY2Fwc3RvbmUiLCJpYXQiOjE1OTAzMzczNDksImV4cCI6MTU5MDQyMzc0OSwiYXpwIjoidjRrd1hSSEsyUHV6RnFiNHFEbTFoUTVSUUZPcXcyZFoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvciIsImNyZWF0ZTptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImVkaXQ6YWN0b3IiLCJlZGl0Om1vdmllIiwicmVhZDphY3RvcnMiLCJyZWFkOm1vdmllcyJdfQ.RIUyuCEbhRuhk9R1S6AcIxt29jD3rI3W-JsHjoZbz9McyhYrnBejzVcx0iDgmehiXBBL2Sz4ritzoKEA1D0uFafBIMUsvQlNtoPFhEiOsxQtjlZSsK0lMUw4lUIsOT3zPBRJ7WKwXXREXi6j2AOxTce8o3WyrSmFJXGMVQUn0Xtx0nYdBO_brko9jQfCEa5Jrb19LYIuyRpxjXH83l6piIoPapgl2pSFTo-dDfD-6Eowch8UCVfp5EURXzO9FnJOjVki9vq04-zlOuEvkRWK9we0fY3vY1QuyUNBDxUGO4_sEEUZwhnIL9hr7rVpvlt8nKon_5aM6fK1wlk3_xCrjg"
        self.casting_assistant = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVzUWZSd1FrTHhyU20zQTBSc3gzNyJ9.eyJpc3MiOiJodHRwczovL25paG9uZG8uYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzk5MjU0Zjc5MDhjMGM2OGEyZjA3OSIsImF1ZCI6InVkYWNpdHktY2Fwc3RvbmUiLCJpYXQiOjE1OTAzMzc1NTQsImV4cCI6MTU5MDQyMzk1NCwiYXpwIjoidjRrd1hSSEsyUHV6RnFiNHFEbTFoUTVSUUZPcXcyZFoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbInJlYWQ6YWN0b3JzIiwicmVhZDptb3ZpZXMiXX0.dOnHZgkAy0WuMglwYHd8i4jJO6s8ND1024pHKm9cKey5aCozoDMEwW4lSUjT7UUy1_WcGIYsPZGWsBf1tGjASlUCHKDrNvqSURtZ42FlVNzTXNnfAfnnXlaTyfBqSu1NQ9ZFI2Lu-Thgiwuu1bA_0Pquvzps1A3G2akNMeDCsluw0jGwaVJ9Zff2wncjAEuX4GDX0nrlH5K235epkOjPz5Ei5Mv-KO8IaiQ_EY2JzSHjI13h9lT2Zl9xxFnBtshZsC2rAvJO-g-2l2AiI8Rt7zI9WPOwWxBF--joyVJbtvsWZ3kVdA8Wlwk47iUWSk1bvsA0dgWMG1bdRBP3teAcgg"

        self.new_actor = {
            "name": "David Spade",
            "age": 57,
            "gender": "male"
        }

        self.new_actor_patch = {
            "name": "David Spadea",
        }

        self.new_movie = {
            "title": "Another Fantastic Movie 3",
            "release_date": "v"
        }

        self.new_movie_patch = {
            "title": "Another Fantastic Movie",
        }

        self.new_movie_bad = {
            "title": "Another Fantastic Movie 3",
        }

        self.new_actor_bad = {
            "name": "David Spade",
            "age": 57,
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

            self.db.drop_all()
            # create all tables
            self.db.create_all()
            # seed with one value
            self.actor = Actor(name='test', age=45, gender='male')
            self.movie = Movie(title='hello', release_date="01/01/2020")

            self.actor.insert()
            self.movie.insert()

    def tearDown(self):
        self.db.drop_all('__all__', self.app)
        """Executed after each test"""
        pass

    def test_post_actor(self):
        res = self.client().post('/actors', headers={

            "Authorization": "Bearer {}".format(
                self.casting_director)
        }, json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)

        pass

    def test_422_post_actor(self):
        res = self.client().post('/actors', headers={
            "Authorization": "Bearer {}".format(
                self.casting_director)
        },
            json=self.new_actor_bad)
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 422)
        pass

    def test_patch_actor(self):
        actor = Actor.query.first()

        res = self.client().patch('/actors/' + str(actor.id), headers={
            "Authorization": "Bearer {}".format(
                self.executive_producer)
        },
            json=self.new_actor_patch)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        pass

    def test_patch_actor_404(self):
        res = self.client().patch('/actors/23432423423', headers={
            "Authorization": "Bearer {}".format(
                self.executive_producer)
        },
            json=self.new_actor_patch)
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 404)
        pass

    def test_actors_successfully_grabbed(self):
        res = self.client().get('/actors', headers={
            "Authorization": "Bearer {}".format(
                self.casting_director)
        })
        data = json.loads(res.data)
        self.assertTrue(len(data['actors']))
        self.assertEqual(data['success'], True)

    def test_actors_401(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 401)

    def test_post_movie(self):
        res = self.client().post('/movies', headers={

            "Authorization": "Bearer {}".format(
                self.executive_producer)
        }, json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)

        pass

    def test_422_post_movie(self):
        res = self.client().post('/movies', headers={
            "Authorization": "Bearer {}".format(
                self.executive_producer)
        },
            json=self.new_movie_bad)
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 422)
        pass

    def test_patch_movie(self):
        movie = Movie.query.first()

        res = self.client().patch('/movies/' + str(movie.id), headers={
            "Authorization": "Bearer {}".format(
                self.executive_producer)
        },
            json=self.new_movie_patch)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        pass

    def test_patch_movie_404(self):
        res = self.client().patch('/movies/2342342423', headers={
            "Authorization": "Bearer {}".format(
                self.executive_producer)
        },
            json=self.new_movie_patch)
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 404)
        pass

    def test_403_post_movie_casting_director(self):
        res = self.client().post('/movies', headers={
            "Authorization": "Bearer {}".format(
                self.casting_director)
        },
            json=self.new_movie_bad)
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 403)
        pass

    def test_movies_successfully_grabbed(self):
        res = self.client().get('/movies', headers={
            "Authorization": "Bearer {}".format(
                self.casting_director)
        })
        data = json.loads(res.data)
        self.assertTrue(len(data['movies']))
        self.assertEqual(data['success'], True)

    def test_movies_401(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_actor(self):

        actor = Actor.query.first()
        res = self.client().delete('/actors/' + str(actor.id),
                                   headers={
            "Authorization": "Bearer {}".format(
                self.casting_director)
        })
        newData = json.loads(res.data)

        newActor = Actor.query.get(actor.id)
        self.assertTrue(newActor is None)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(newData['success'], True)

    def test_delete_actor_404(self):
        res = self.client().delete('/actors/234324234',
                                   headers={
                                       "Authorization": "Bearer {}".format(
                                           self.casting_director)
                                   })
        newData = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(newData['success'], False)

    def test_delete_movie_404(self):
        res = self.client().delete('/movies/234234234234',
                                   headers={
                                       "Authorization": "Bearer {}".format(
                                           self.executive_producer)
                                   })
        newData = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(newData['success'], False)

    def test_403_delete_movie_casting_director(self):

        movie = Movie.query.first()
        res = self.client().delete('/movies/' + str(movie.id),
                                   headers={
            "Authorization": "Bearer {}".format(
                self.casting_director)
        })
        newData = json.loads(res.data)
        self.assertEqual(res.status_code, 403)

    def test_delete_movie(self):

        movie = Movie.query.first()
        res = self.client().delete('/movies/' + str(movie.id),
                                   headers={
            "Authorization": "Bearer {}".format(
                self.executive_producer)
        })
        newData = json.loads(res.data)

        newMovie = Movie.query.get(movie.id)
        self.assertTrue(newMovie is None)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(newData['success'], True)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
