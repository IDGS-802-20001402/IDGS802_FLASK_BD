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

@app.route('/', methods=['GET', 'POST'])
def index():

    form = forms.UserForm(request.form)

    if request.method == 'POST' and form.validate():
        alumno = Alumnos(form.nombre.data, form.apellido.data, form.email.data)
        db.session.add(alumno)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()