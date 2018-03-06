Web app for the landing page

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
* Run the server using manage.py
```
python manage.py runserver
```

## Staging testing
* Install the dependencies in library folder    
```
pip install -t lib -r requirements.txt
```
* Use the file *app_yaml.frame* as a wireframe for creating the [app.yaml](https://cloud.google.com/appengine/docs/flexible/python/configuring-your-app-with-app-yaml) file.
* Fill in the appropriate values of username, password, database and instance name
* Deploy the version in staging enviornment using the [--version](https://cloud.google.com/sdk/gcloud/reference/app/deploy) flag, and use the `--no-promote` flag so that this version receives zero traffic.
```
gcloud app deploy --no-promote --version app-staging app.yaml
```
* Use `gcloud app browse`to open the deployed app in browser


## Production launch
* Install the dependencies in library folder    
```
pip install -t lib -r requirements.txt
```
* Reuse the same app.yaml file, but drop the `--version`and `--no-promote` flags
```
gcloud app deploy app.yaml
```
* Use `gcloud app browse`to open the deployed app in browser
