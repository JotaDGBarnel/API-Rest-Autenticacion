from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/autenticacionusuarios'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# creacion de la tabla Usuario
class Usuario(db.Model):
    id_Usuario = db.Column(db.Integer, primary_key=True)
    Nombre_Usuario = db.Column(db.String(40))
    Contrasena_Usuario = db.Column(db.String(20))
    Correo_Usuario = db.Column(db.String(40))

    # definimos el constructor para cuando se llame la tabla
    def __init__(self, Nombre_Usuario, Contrasena_Usuario, Correo_Usuario):
        self.Nombre_Usuario = Nombre_Usuario
        self.Contrasena_Usuario = Contrasena_Usuario
        self.Correo_Usuario = Correo_Usuario

# Creacion Tabla Rol
class Rol(db.Model):
    id_Rol = db.Column(db.Integer, primary_key=True)
    Nombre_Rol = db.Column(db.String(40))
    Descripcion_Rol = db.Column(db.String(100))
    Fecha_Creacion = db.Column(db.String(20))

    # definimos el constructor para cuando se llame la tabla
    def __init__(self, Nombre_Rol, Descripcion_Rol, Fecha_Creacion):
        self.Nombre_Rol = Nombre_Rol
        self.Descripcion_Rol = Descripcion_Rol
        self.Fecha_Creacion = Fecha_Creacion


# Creacion tabla Permiso
class Permiso(db.model):
    id_Permiso = db.Column(db.Integer, primary_key=True)
    Nombre_Permiso = db.Column(db.String(40))
    Descripcion_Permiso = db.Column(db.String(100))
    Fecha_Creacion = db.Column(db.String(20))

    # definimos el constructor para cuando se llame la tabla
    def __init__(self, Nombre_Permiso, Descripcion_Permiso, Fecha_Creacion):
        self.Nombre_Permiso = Nombre_Permiso
        self.Descripcion_Permiso = Descripcion_Permiso
        self.Fecha_Creacion = Fecha_Creacion

with app.app_context():
    db.create_all()
