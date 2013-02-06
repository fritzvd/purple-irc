import sqlite3
from flask import *
from contextlib import closing
app = Flask(__name__)
app.config.from_object(__name__)

DATABASE = 'test.db'
DEBUG = True
SECRET_KEY = 'dev_key'

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql') as f:
			db.cursor().executescript(f.read())
		db.commit

@app.before_request
def before_request():
	g.db = connect_db()

if __name__== "__main__":
	app.run()