# What is MoodMix?

Simply put, Moodmix is a Flask app that utilizes the emotion-based Face++ API to suggest a DJ mix for a user.

# Quickstart

Run the following commands to bootstrap your environment:

```
git clone https://github.com/randyriback/moodmix
cd moodxix
pip install -r requirements.txt
```

Run the following commands to create your app's database tables and perform the initial migration

```
flask db init
flask db migrate
flask db upgrade
```

To run the web application use:

`flask run`

# Deployment
In your production environment, make sure the FLASK_DEBUG environment variable is unset or is set to 0, so that ProdConfig is used, and set DATABASE_URL which is your postgresql URI for example postgresql://localhost/example (this is set by default in heroku).

For further info, refer to https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/

# Migrations

```
flask db migrate
flask db upgrade
```

For a full migration command reference, run `flask db --help`.
