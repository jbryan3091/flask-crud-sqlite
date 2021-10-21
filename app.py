from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/tasks.db' #SQLAlchemy modela datos antes de guardarlos, Crear modelo o clase 
db = SQLAlchemy(app)

#Crea la clase con las propiedades del To-do 
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    done = db.Column(db.Boolean)

# url inicial

@app.route('/')
def home():
    tasks = Task.query.all()
    return render_template('index.html', tasks = tasks)

@app.route('/create-task', methods=['POST']) #POST guarda datos
def create():
    task = Task(content=request.form['content'], done=False) # recibe datos del content y done desde formulario
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/done/<id>')
def done (id):
    task = Task.query.filter_by(id=int(id)).first()
    task.done = not(task.done) # cambiar de False a True o viceversa
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/delete/<id>')
def delete(id):
    task = Task.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(port=5000, debug=True)