from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Alumnos(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    email = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, nombre, apellido, email, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.fecha_nacimiento = fecha_nacimiento

    def __repr__(self):
        return '<Alumno %r>' % self.nombre