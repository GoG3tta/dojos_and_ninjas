from flask import Flask

DATABASE = 'dojos_and_ninjas_schema' # CHANGE PROJECT_SCHEMA TO SQL SCHEMA

app = Flask(__name__)
app.secret_key = 'this is the way'