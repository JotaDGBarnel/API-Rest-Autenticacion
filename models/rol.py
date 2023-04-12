from flask import request, jsonify, Blueprint
from app.aplicacion import db, ma, Rol

role = Blueprint('rol', __name__)

class RoleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nom', 'desc', 'fecha')

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

@role.route('/roleC', methods=['Post'])
def create_role():
  nom = request.json['nom']
  desc = request.json['desc']
  fecha = request.json['fecha']

  new_role = Rol(nom, desc, fecha)

  db.session.add(new_role)
  db.session.commit()

  return role_schema.jsonify(new_role)

@role.route('/rolesG', methods=['GET'])
def get_roles():
  all_roles = Rol.query.all()
  result = roles_schema.dump(all_roles)
  return jsonify(result)

@role.route('/rolesG/<id>', methods=['GET'])
def get_role(id):
  role = Rol.query.get(id)
  return role_schema.jsonify(role)

@role.route('/roleU/<id>', methods=['PUT'])
def update_role(id):
  role = Rol.query.get(id)

  nom = request.json['nom']
  desc = request.json['desc']
  fecha = request.json['fecha']

  role.nom = nom
  role.desc = desc
  role.fecha = fecha

  db.session.commit()

  return role_schema.jsonify(role)

@role.route('/roleD/<id>', methods=['DELETE'])
def delete_role(id):
  role = Rol.query.get(id)
  db.session.delete(role)
  db.session.commit()
  return role_schema.jsonify(role)
