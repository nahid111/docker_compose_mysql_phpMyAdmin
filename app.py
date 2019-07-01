from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

DB_HOST = 'localhost:3306'
DB_NAME = 'db_test'
DB_USERNAME = 'root'
DB_PASSWORD = 'secretPassword'

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(191))
    email = db.Column(db.String(191), unique=True)

db.create_all() # In case user table doesn't exists already. Else remove it.

users = User.query.all()
if not users:
    usr1 = User(username='admin', email='admin@example.com')
    usr2 = User(username='staff', email='staff@example.com')
    # Save Users to DB
    db.session.add(usr1)
    db.session.add(usr2)
    db.session.commit()


@app.route('/')
def index():
    users = User.query.all()
    context = {
        "users": users
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

