import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from api.api import create_app
from models.models import setup_db, Movie, Actor


class CastingTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)


        self.casting_director = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVzUWZSd1FrTHhyU20zQTBSc3gzNyJ9.eyJpc3MiOiJodHRwczovL25paG9uZG8uYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzE1M2Y0NDUzZTIzMGM3MWQ5MzIyNiIsImF1ZCI6InVkYWNpdHktY2Fwc3RvbmUiLCJpYXQiOjE1OTAyNTg5MDQsImV4cCI6MTU5MDI2NjEwNCwiYXpwIjoidjRrd1hSSEsyUHV6RnFiNHFEbTFoUTVSUUZPcXcyZFoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvciIsImRlbGV0ZTphY3RvciIsImVkaXQ6YWN0b3IiLCJlZGl0Om1vdmllIiwicmVhZDphY3RvcnMiLCJyZWFkOm1vdmllcyJdfQ.Jx6n4VRoDRSyJz2BNNGXNIdwSyB31kvWRRAFMfSiMm-INIq1xwk1EgnT5MwJ2f4Bzw2qMOpmO3P_lMy5OBKAr2QJXk52DuBCYKWlURHZO19OQFtHQ2_rWWTmh_iZJPrCpEZ7B1IgjZqSV34fkV377aTfEaYTIls54eBYZxYDb4X5NgnGsttClJYTx8O5tKL2wAvKOo2ATrGhJSStFOKHjWYP6NKMtA9VVfepD9-XNq7anpaEVJfOHOtaXc54Mcmi03MKVpKgtoke4ygOECXJUq_mJCNH_ur7iC_Yi52e7aVmqW-9mnuNxR0Om47hJQrCUk5jV9w3ZP9y6ywBOlKbBw"
        self.executive_producer = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVzUWZSd1FrTHhyU20zQTBSc3gzNyJ9.eyJpc3MiOiJodHRwczovL25paG9uZG8uYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzE1M2M2NTgzMGE5MGM2ZmU5YmM4MyIsImF1ZCI6InVkYWNpdHktY2Fwc3RvbmUiLCJpYXQiOjE1OTAyNjA4NjQsImV4cCI6MTU5MDI2ODA2NCwiYXpwIjoidjRrd1hSSEsyUHV6RnFiNHFEbTFoUTVSUUZPcXcyZFoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvciIsImNyZWF0ZTptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImVkaXQ6YWN0b3IiLCJlZGl0Om1vdmllIiwicmVhZDphY3RvcnMiLCJyZWFkOm1vdmllcyJdfQ.cpHe-28qnvVUW-dwcq6Ck175Mu7YJxw2lbW3vho8AAF5hfPE16WH7q2XHG2AVy4p91WzXZnMnuuH6blYDR9_YNKl5EMTwOgy6UKX4_w7EXCJBPZwnJwwYwkagwVYW5aHtVSLCI1KNVSttD4YmgF3F7Z_mXg8gWSIDloFVKzhqVwtuHsuC_20Zt9qOe3Q9hXRnIp6-3UXx5lUGHP8910wEyfPA92EE7Ddr-j91kQ_8dETZReh54tzXMklQkdMZfSKQ0QXrXmQzazzYKA0jU9KF7vUD0uwqsd1lzTgLnp6c2r-ieJFCAFNczvzjfZR_rnAZCTDSyo8_tIkCZKem1EcTA"


        self.new_actor = {
            "name": "David Spade",
            "age": 57,
            "gender": "male"
        }

        self.new_actor_patch = {
            "name": "David Spadea",
        }

        self.new_movie = {
            "title" : "Another Fantastic Movie 3",
            "release_date": "01/01/2020"
        }

        self.new_movie_patch = {
            "title" : "Another Fantastic Movie",
        }

        self.new_movie_bad = {
            "title" : "Another Fantastic Movie 3",
        }


        self.new_actor_bad = {
            "name": "David Spade",
            "age": 57,
        }



        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after each test"""
        pass


# https://nihondo.auth0.com/authorize?audience=udacity-capstone&response_type=token&client_id=v4kwXRHK2PuzFqb4qDm1hQ5RQFOqw2dZ&redirect_uri=http://localhost:8080
    def test_post_actor(self):
        res = self.client().post('/actors',headers={

        "Authorization": "Bearer {}".format(
            self.casting_director)
        },  json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)

        pass



    def test_422_post_actor(self):
        res = self.client().post('/actors',headers={
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

        res = self.client().patch('/movies/' + str(actor.id),headers={
                                            "Authorization": "Bearer {}".format(
                                                self.executive_producer)
                                            },  
                                            json=self.new_actor_patch)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        pass

    def test_actors_successfully_grabbed(self):
        res = self.client().get('/actors', headers={
                                            "Authorization": "Bearer {}".format(
                                                self.casting_director)
                                            })
        data = json.loads(res.data)
        self.assertTrue(len(data['actors']))
        self.assertEqual(data['success'], True)


    def test_post_movie(self):
        res = self.client().post('/movies',headers={

        "Authorization": "Bearer {}".format(
            self.executive_producer)
        },  json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)

        pass



    def test_422_post_movie(self):
        res = self.client().post('/movies',headers={
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

        res = self.client().patch('/movies/' + str(movie.id),headers={
                                            "Authorization": "Bearer {}".format(
                                                self.executive_producer)
                                            },  
                                            json=self.new_movie_patch)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        pass



    def test_403_post_movie_casting_director(self):
        res = self.client().post('/movies',headers={
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

    def test_403_delete_movie_casting_director(self):

        movie = Movie.query.first()
        res = self.client().delete('/movies/' + str(movie.id),
                                            headers={
                                            "Authorization": "Bearer {}".format(
                                                self.casting_director)
                                            })
        newData = json.loads(res.data)
        self.assertEqual(res.status_code, 403)

        
        

    # def test_404_delete_questions(self):
    #     res = self.client().delete('/questions/10000')
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'The resource could not be found')
    



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()