from flask import request, jsonify, Blueprint
from app.aplicacion import db, ma, Usuario
from .usuarioDTO import UsuarioDTO, UsuarioDAO


class UsuarioDTO:
    def __init__(self, id, nom, con, correo):
        self.id = id
        self.nom = nom
        self.con = con
        self.correo = correo

class UsuarioDAO:
    def create(self, usuario_dto):
        nom = usuario_dto.nom
        con = usuario_dto.con
        correo = usuario_dto.correo

        new_user = Usuario(nom, con, correo)

        db.session.add(new_user)
        db.session.commit()

        return usuario_dto

    def read_all(self):
        all_users = Usuario.query.all()
        result = [UsuarioDTO(user.id, user.nom, user.con, user.correo) for user in all_users]
        return result

    def read(self, id):
        usu = Usuario.query.get(id)
        return UsuarioDTO(usu.id, usu.nom, usu.con, usu.correo)

    def update(self, usuario_dto):
        usu = Usuario.query.get(usuario_dto.id)

        nom = usuario_dto.nom
        con = usuario_dto.con
        correo = usuario_dto.correo

        usu.nom = nom
        usu.con = con
        usu.correo = correo

        db.session.commit()

        return usuario_dto

    def delete(self, id):
        usu = Usuario.query.get(id)
        db.session.delete(usu)
        db.session.commit()
        return UsuarioDTO(usu.id, usu.nom, usu.con, usu.correo)

user = Blueprint('user', __name__)
usuario_dao = UsuarioDAO()

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nom', 'con', 'correo')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user.route('/userC', methods=['POST'])
def create_user():
    nom = request.json['nom']
    con = request.json['con']
    correo = request.json['correo']

    usuario_dto = UsuarioDTO(None, nom, con, correo)
    usuario_dto = usuario_dao.create(usuario_dto)

    return user_schema.jsonify(usuario_dto)

@user.route('/usersG', methods=['GET'])
def get_users():
    result = usuario_dao.read_all()
    return jsonify(result)

@user.route('/userG/<id>', methods=['GET'])
def get_user(id):
    result = usuario_dao.read(id)
    return user_schema.jsonify(result)

@user.route('/userU/<id>', methods=['PUT'])
def update_user(id):
    nom = request.json['nom']
    con = request.json['con']
    correo = request.json['correo']

    usuario_dto = UsuarioDTO(id, nom, con, correo)
    usuario_dto = usuario_dao.update(usuario_dto)

    return user_schema.jsonify(usuario_dto)

@user.route('/userD/<id>', methods=['DELETE'])
def delete_user(id):
    result = usuario_dao.delete(id)
    return user_schema.jsonify(result)

@user.route('/', methods=['GET'])
def index():