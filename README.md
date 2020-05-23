# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

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

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

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


### GET /questions
- General:
  - Returns a list of questions, total number of questions, a list of categories, and the current category
  - Results are paginated in groups of 10
- Sample: ```bash curl http:127.0.0.1:5000/questions?page=1 ```
```json
{
  "categories": {
    "1": "social studies"
  }, 
  "current_category": null, 
  "questions": [
    {
      "answer": "Dover", 
      "category": "social studies", 
      "difficulty": 2, 
      "id": 1, 
      "question": "What is the capital of Delaware"
    }
  ], 
  "success": true, 
  "total_questions": 1
}

```

### POST /questions
- General:
  - Creates a new questions with a given question, answer, category and difficulty. Created question will be returned. Difficulty must be a number between 1-5
- Sample: ```bash curl http:127.0.0.1:5000/questions -X POST -H "Content-Type: application/json -d {"question":"test", "answer":"test answer", "category":"test", "difficulty":5} ```
```json
{
  "answer": "test answer", 
  "category": 1, 
  "difficulty": "5", 
  "id": 19, 
  "question": "test", 
  "success": true
}

```

### DELETE /questions/<question_id>
- General:
  - Deletes a question given an id. Will retrun 404 if the question is not found. 
- Sample: ```bash curl http:127.0.0.1:5000/questions/1 -X DELETE```
```json
{
  "success": true
}
```

### GET /questions/search
- General:
  - Will search for a question using the question text with the supplied q parameter. Will return a list of questions, the total questions found, the current category, and a success flag.
- Sample: ```bash curl http:127.0.0.1:5000/questions/search?q=tes ```
```json
{
  "current_category": null, 
  "questions": [
    {
      "answer": "test answer", 
      "category": "1", 
      "difficulty": 5, 
      "id": 19, 
      "question": "test"
    }
  ], 
  "success": true, 
  "total_questions": 1
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


