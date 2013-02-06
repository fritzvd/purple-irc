import sqlite3
from flask import *
app = Flask(__name__)
app.config.from_object(__name__)

DATABASE = 'test.db'
DEBUG = True
SECRET_KEY = 'dev_key'

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

if __name__== "__main__":
	app.run()