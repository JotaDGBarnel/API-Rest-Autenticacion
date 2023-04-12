from flask import request, jsonify, Blueprint
from app.aplicacion import db, ma, Usuario

user = Blueprint('user', __name__)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nom', 'con', 'correo')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user.route('/userC', methods=['Post'])
def create_user():

  nom = request.json['nom']
  con = request.json['con']
  correo = request.json['correo']

  new_user = Usuario(nom, con, correo)

  db.session.add(new_user)
  db.session.commit()

  return user_schema.jsonify(new_user)

@user.route('/usersG', methods=['GET'])
def get_users():
  all_users = Usuario.query.all()
  result = users_schema.dump(all_users)
  return jsonify(result)

@user.route('/userG/<id>', methods=['GET'])
def get_user(id):
  usu = Usuario.query.get(id)
  return user_schema.jsonify(usu)

@user.route('/userU/<id>', methods=['PUT'])
def update_user(id):
  usu = Usuario.query.get(id)

  nom = request.json['nom']
  con = request.json['con']
  correo = request.json['correo']

  usu.nom = nom
  usu.con = con
  usu.correo = correo

  db.session.commit()

  return user_schema.jsonify(usu)

@user.route('/userD/<id>', methods=['DELETE'])
def delete_user(id):
  usu = Usuario.query.get(id)
  db.session.delete(usu)
  db.session.commit()
  return user_schema.jsonify(usu)

@user.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to my API'})




