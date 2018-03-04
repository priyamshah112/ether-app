Web app for the landing page

# Testing
This web-app is built to be deployed on the app-engine.
There exist three testing methods:  
1. Develop version for local testing
2. Staging version for testing on the app-engine
3. Production version for production landing-page

## Local testing

* Create a virtual enviornment using either `virtualenv` or `conda create`.
* Then install the required dependencies using:
```
pip install -r requirements.txt
```
* Start the cloud sql proxy using correct parameters, [more details here](https://cloud.google.com/appengine/docs/flexible/python/using-cloud-sql-postgres) 
```
./cloud_sql_proxy -instances=[instance-name]=tcp:[port-number] &
```
* Export the SQLALCHEMY DATABASE URI 
```
export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://[USER_NAME]:[PASSWORD]@127.0.0.1:[port-number]/[DATABASE_NAME]
```
* Export the flask app and run flask
```
export FLASK_APP=main.py
flask run
```

## Staging testing
