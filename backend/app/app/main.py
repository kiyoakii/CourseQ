from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    visit_time = db.Column(db.Integer)

    def __init__(self):
        visit_time = int(time.time())
        self.visit_time = visit_time

    def __repr__(self):
        return '<Post %s>' % str(self.visit_time)


db.create_all()


@app.route("/")
def hello():
    visit = Visit()
    db.session.add(visit)
    db.session.commit()
    print(Visit.query.all())
    return "Hello World!"


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
    