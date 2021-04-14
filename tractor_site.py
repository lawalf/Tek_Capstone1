import os
from forms import  AddForm , DelForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################

        # SQL DATABASE AND MODELS

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:JigglyPuff1234@localhost/tractordb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class Tractor(db.Model):

    __tablename__ = 'Tractors'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Tractor type: {self.name}"

############################################

        # VIEWS WITH FORMS

##########################################
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_tractor():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        # Add new Tractor to database
        new_tractor = Tractor(name)
        db.session.add(new_tractor)
        db.session.commit()

        return redirect(url_for('list_tractor'))

    return render_template('add.html',form=form)

@app.route('/list')
def list_tractor():
    # Grab a list of tractors from database.
    tractors = Tractor.query.all()
    return render_template('list.html', tractors=tractors)

@app.route('/delete', methods=['GET', 'POST'])
def del_tractor():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        tractor = Tractor.query.get(id)
        db.session.delete(tractor)
        db.session.commit()

        return redirect(url_for('list_tractor'))
    return render_template('delete.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
