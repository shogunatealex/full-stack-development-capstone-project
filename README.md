# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
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
export FLASK_APP=api
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `api` directs flask to use the `api` directory and the `__init__.py` file to find the application. 


## Error Handling

Errors are returned as JSON objects in the following format:

```json
{
  "success": false,
  "message": "Bad Request"
}
```

NOTE: the actual error code will come in the response object. Like response.status_code

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
- Sample: ```bash curl http:127.0.0.1:5000/actors -X POST -H "Content-Type: application/json -d {"name": "Bill The Murray"} ```
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

### GET /categories
- General:
  - Retrieves a list of categories where the key is the category id and the value is the name of the category
- Sample: ```bash curl http:127.0.0.1:5000/categories ```
```json
{
  "categories": {
    "1": "history"
  }
}

```

### GET /categories/<category_id>/questions
- General:
  - Retrieves a list of questions that match a specific category id. Returns a list of the total questions, the total questions, the current cateogry, and a success flag
- Sample: ```bash curl http:127.0.0.1:5000/categories/1/questions ```
```json
{
  "current_category": "history", 
  "questions": [
    {
      "answer": "really good", 
      "category": "history", 
      "difficulty": 2, 
      "id": 1, 
      "question": "How good are these pancackes"
    }, 
  ], 
  "success": true, 
  "total_questions": 1
}
```

### POST /quizzes
- General:
  - Takes an array of previous questions and the quiz category and returns a random question not yet taken for the quiz
- Sample: ```bash curl http:127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json -d {"previous_questions":[1,4],"quiz_category":{"type":"history","id":"1"}} ```

```json
{
  "question": {
    "answer": "really good", 
    "category": "history", 
    "difficulty": 2, 
    "id": 17, 
    "question": "How good are these pancackes"
  }, 
  "success": true
}
```


