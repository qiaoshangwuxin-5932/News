from flask import Flask
from Anews import config
from flask_sqlalchemy import SQLAlchemy

app =Flask(__name__)
app.config.from_object(config)
db= SQLAlchemy(app)

