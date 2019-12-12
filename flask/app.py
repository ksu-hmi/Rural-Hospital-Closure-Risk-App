
from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' %self.id

@app.route('/', methods= ['POST', 'GET'])
def home():
    if request.method == 'POST': 
        pass

    #add if statements for each possible state input to bring up folium map
    #if request.method == 'Texas'
        #elif display Texas folium map 
        #points on map for each hospital closure link to indv closure data

    else:
        return render_template('home.html')

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)