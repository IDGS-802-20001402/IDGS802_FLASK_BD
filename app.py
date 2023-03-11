from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
import forms

from flask import jsonify
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db #ORM
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)

@app.route('/ABCompleto', methods=['GET', 'POST'])	
def ABCompleto():
    alumnos = Alumnos.query.all()
    form = forms.UserForm(request.form)

    if request.method == 'POST' and form.validate():
        alumno = Alumnos(form.nombre.data, form.apellido.data, form.email.data)
        db.session.add(alumno)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('ABCompleto.html', alumnos=alumnos, form=form)

@app.route('/', methods=['GET', 'POST'])
def index():

    form = forms.UserForm(request.form)

    if request.method == 'POST' and form.validate():
        alumno = Alumnos(form.nombre.data, form.apellido.data, form.email.data)
        db.session.add(alumno)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('index.html', form=form)

@app.route('/modificar/<id>', methods=['GET', 'POST'])
def modificar(id):
    form = forms.UserForm(request.form)

    if request.method == 'GET':
        alum1 = db.session.query(Alumnos).filter_by(id=id).first()
        form.id.data = alum1.id
        form.nombre.data = alum1.nombre
        form.apellido.data = alum1.apellido
        form.email.data = alum1.email
    else:
        if request.method == 'POST' and form.validate():
            alum1 = db.session.query(Alumnos).filter_by(id=id).first()
            alum1.nombre = form.nombre.data
            alum1.apellido = form.apellido.data
            alum1.email = form.email.data
            db.session.add(alum1)
            db.session.commit()
            return redirect(url_for('ABCompleto'))
    
    return render_template('modificar.html', form=form)

@app.route('/eliminar/<id>', methods=['POST'])
def eliminar(id):
    if request.method == 'POST':
        alum1 = db.session.query(Alumnos).filter_by(id=id).first()
        db.session.delete(alum1)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return redirect(url_for('ABCompleto'))

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()