import os
from os import environ
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from api import create_app
from models.models import setup_db, Movie, Actor


class CastingTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_test"
        self.database_path = "postgres://localhost:5432/casting_test"
        setup_db(self.app, self.database_path)


        self.casting_director = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVzUWZSd1FrTHhyU20zQTBSc3gzNyJ9.eyJpc3MiOiJodHRwczovL25paG9uZG8uYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzE1M2Y0NDUzZTIzMGM3MWQ5MzIyNiIsImF1ZCI6InVkYWNpdHktY2Fwc3RvbmUiLCJpYXQiOjE1OTAyNjkwMzIsImV4cCI6MTU5MDM1NTQzMiwiYXpwIjoidjRrd1hSSEsyUHV6RnFiNHFEbTFoUTVSUUZPcXcyZFoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvciIsImRlbGV0ZTphY3RvciIsImVkaXQ6YWN0b3IiLCJlZGl0Om1vdmllIiwicmVhZDphY3RvcnMiLCJyZWFkOm1vdmllcyJdfQ.PdweJnOJDtemSeWfS-6TIe1_Xr6KT9pvL7_TfNq3YiSsjZ305_Jg_ZP1NpzogoSh7R8PHosbqdzWnUVq3R83dWDUtcwd7snM7orArNJGSsobR_L8zvDrsQkSUZuOQ34P4PRDwInP85qFc-MgCktmEUQn7KlC-AXeuMya2bmR91rivffOpRzLGBxglGqQ1EXYmIajqGwzVRUgK0M4wRu5Dh-0wLFaf7RBYPWnIVB5AGWnUSNbyi3Rpu5eyDYr1lvbzD8f3s1FSXHaxKEVp4BiD6l1tRBMaFJvc0wCn6Au3Yyd2I_BDFi8Gbz6tVjZhzd2q-jAy86zBcZNX_AcyiWbIg"
        self.executive_producer = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVzUWZSd1FrTHhyU20zQTBSc3gzNyJ9.eyJpc3MiOiJodHRwczovL25paG9uZG8uYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzE1M2M2NTgzMGE5MGM2ZmU5YmM4MyIsImF1ZCI6InVkYWNpdHktY2Fwc3RvbmUiLCJpYXQiOjE1OTAyNjkwOTgsImV4cCI6MTU5MDM1NTQ5OCwiYXpwIjoidjRrd1hSSEsyUHV6RnFiNHFEbTFoUTVSUUZPcXcyZFoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvciIsImNyZWF0ZTptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImVkaXQ6YWN0b3IiLCJlZGl0Om1vdmllIiwicmVhZDphY3RvcnMiLCJyZWFkOm1vdmllcyJdfQ.UmcVcd2H8UQla4YFdVEwzCurNofPBZkrMj0BX8yRYmihkFe5NdMl9kmAtX_A55v0DORqGErvBLjdAmUHYC1TafBlt0r-s5gC5J_sA7OFxHyMgzTMSlZaeoWJRtYhidMSThJk_0KJolw85y4BUBPX03_7SlZt3B4GgiIFDqsDzPErZL0CKOuMHk9NkUxZ9t-FqOyYqu6tA_6-hqpieCNBu5O2335j2RXp9Y28tl5XXMCDLGUrcdYJFStuW6biv6S6_xA5s7dG4X54sP8-oKoQKGyMJTFwLArBRsYGhzOBAhOugssqUK5RfenxLb75DKcJLXlJixp0WLBLX8YjXKc7RQ"
        self.casting_assistant = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVzUWZSd1FrTHhyU20zQTBSc3gzNyJ9.eyJpc3MiOiJodHRwczovL25paG9uZG8uYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzk5MjU0Zjc5MDhjMGM2OGEyZjA3OSIsImF1ZCI6InVkYWNpdHktY2Fwc3RvbmUiLCJpYXQiOjE1OTAyNjg1MDQsImV4cCI6MTU5MDM1NDkwNCwiYXpwIjoidjRrd1hSSEsyUHV6RnFiNHFEbTFoUTVSUUZPcXcyZFoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbXX0.oAFrM3riJcG0XCJzzb1aPyi60RonZ4OcTfArmxQQTG-745Uo37M5g9pfLtYtkkNuq9Oddwyukv5Z6j8Zgs2JhFEeZQWuTre1BSOIcFupyjWHieHkiDox8hthmAQ_g9BzJ9-oiZHKahWPeaniTJE4PyE9RGQh-o1mcZA6KJyrrXz1Aqz_oJ1MXup0fNhbMTnNbsJOGkDArJiC5Q6OnqAjkSFK6WuKrm9cgSDtTbg3ATSu_VNS7-dII2WQ5uNrKMdlxvgFonwBbbdrd2IYKGk1M_uD8o58i7zBoc-q_wr7efmrxn-lR5u5scxLkgwJnyno9Jkw9Xwf1STShXWGRTnCUA"

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

        res = self.client().patch('/actors/' + str(actor.id),headers={
                                            "Authorization": "Bearer {}".format(
                                                self.executive_producer)
                                            },  
                                            json=self.new_actor_patch)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        pass

    def test_patch_actor_404(self):
        res = self.client().patch('/actors/23432423423',headers={
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

    def test_patch_movie_404(self):
        res = self.client().patch('/movies/2342342423' ,headers={
                                            "Authorization": "Bearer {}".format(
                                                self.executive_producer)
                                            },  
                                            json=self.new_movie_patch)
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 404)
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