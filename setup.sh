pip3 install -r requirements.txt
export AUTH0_DOMAIN=nihondo.auth0.com
export API_AUDIENCE=udacity-capstone
export ALGORITHMS=RS256
export DATABASE_URL=postgres://localhost:5432/casting
gunicorn wsgi:app