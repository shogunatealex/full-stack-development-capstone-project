Heroku App URL: https://udacity-capstone-alex-a234.herokuapp.com

# Full Stack Capstone Project

This app is the capstone project for the udacity full stack nanodegree. It is used to showcase the collection of knowlege in the app that includes how to create a full stack application. This application utilizes the following tech stack.

SQLAlchemy: as our ORM
PostgreSQL: as our database
Python3: and Flask as our server language and server framework
Gunicorn: as our python server
Flask-Migrate: for creating and running schema migrations
Auth0: as our authentication provider
Heroku: as a way to showcase our application



## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
./setup.sh
```

This will automatically install all dependencies, export the basic variables for the application and start the gunicorn server.

You will be able to find this application on 127.0.0.1:8000

## Testing & Authentication

This application includes a postman collection that is preconfigured to test all the endpoints. It can be imported via postman and the various endpoints can be tested. All three tokens are stored as environment variables in the collection. Feel free to change them out in the collection's authorization tab to test the different roles. It's preconfigured for the executive producer token.

In postman there is also a variable named domain. Changing that to https://udacity-capstone-alex-a234.herokuapp.com will allow you to test the live version of the endpoints.


## Error Handling

Errors are returned as JSON objects in the following format:

```json
{
  "success": false,
  "message": "Bad Request"
}
```

NOTE: the actual error code will come in the response object. Like response.status_code


## Permissions

Executive Producer: All permissions
Casting Director: All permissions except creating and deleting movies
Casting Assistant: Only get actors and get movies

## Endpoints


### GET /actors
- General:
  - Returns a list of actors
- Sample: ```bash curl http:127.0.0.1:5000/actors ```
```json
{
    "actors": {
        "1": {
            "age": 57,
            "gender": "male",
            "id": 1,
            "name": "David Spade"
        }
    },
    "success": true
}

```

### POST /actors
- General:
  - Creates a new actor with a given name, age, and gender. Created question will be returned. Difficulty must be a number between 1-5
- Sample: ```bash curl http:127.0.0.1:5000/actors -X POST -H "Content-Type: application/json -d {"name": "David Spade","age": 57,"gender": "male"} ```
```json
{
    "actors": {
        "1": {
            "age": 57,
            "gender": "male",
            "id": 1,
            "name": "David Spade"
        }
    },
    "success": true
}

```

### DELETE /actors/<actor-id>
- General:
  - Deletes an actor given an id. Will retrun 404 if the actor is not found. 
- Sample: ```bash curl http:127.0.0.1:5000/actors/1 -X DELETE ```
```json
{
    "delete": 1,
    "success": true
}
```

### PATCH /actors/<actor-id>
- General:
  - Will update an actor based on an actor id. Will only update the values supplied and the full record is returned
- Sample: ```bash curl http:127.0.0.1:5000/actors/1 -X PATCH -H "Content-Type: application/json -d {"name": "Bill The Murray"} ```
```json
{
    "actors": {
        "4": {
            "age": 57,
            "gender": "male",
            "id": 4,
            "name": "Bill The Murray"
        }
    },
    "success": true
}

```

### GET /movies
- General:
  - Retrieves a list of movies. Movies contain a title and a release date.
- Sample: ```bash curl http:127.0.0.1:5000/movies ```
```json
{
    "movies": {
        "1": {
            "id": 1,
            "release_date": "01/01/2020",
            "title": "Another Fantastic Movie 3"
        }
    },
    "success": true
}

```

### POST /movies
- General:
  - Adds a new movie to the database
- Sample: ```bash curl http:127.0.0.1:5000/movies -X POST -H "Content-Type: application/json -d {"title" : "Another Fantastic Movie 3","release_date": "01/01/2020"} ```
```json
{
    "movies": {
        "1": {
            "id": 1,
            "release_date": "01/01/2020",
            "title": "Another Fantastic Movie 3"
        }
    },
    "success": true
}
```

### DELETE /movies/<movie-id>
- General:
  - Deletes a movie given an id. Will retrun 404 if the actor is not found. 
- Sample: ```bash curl http:127.0.0.1:5000/movie/1 -X DELETE ```
```json
{
    "delete": 1,
    "success": true
}
```
  
  
### PATCH /movies/<movie-id>
- General:
  - Will update a movie based on a movie id. Will only update the values supplied and the full record is returned
- Sample: ```bash curl http:127.0.0.1:5000/movies/1 -X PATCH -H "Content-Type: application/json -d {"title": "New Title"} ```
```json
{
    "movies": {
        "1": {
            "id": 1,
            "release_date": "01/01/2020",
            "title": "New Title"
        }
    },
    "success": true
}

```

