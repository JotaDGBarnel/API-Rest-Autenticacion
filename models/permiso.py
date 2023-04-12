from flask import request, jsonify, Blueprint
from app.aplicacion import db, ma, Permiso

permission = Blueprint('permission', __name__)

class PermissionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nom', 'desc', 'fecha')

permission_schema = PermissionSchema()
permissions_schema = PermissionSchema(many=True)

@permission.route('/permissionC', methods=['Post'])
def create_permission():
  nom = request.json['nom']
  desc = request.json['desc']
  fecha = request.json['fecha']

  new_permission = Permiso(nom, desc, fecha)

  db.session.add(new_permission)
  db.session.commit()

  return permission_schema.jsonify(new_permission)

@permission.route('/permissionsG', methods=['GET'])
def get_permissions():
  all_permissions = Permiso.query.all()
  result = permissions_schema.dump(all_permissions)
  return jsonify(result)

@permission.route('/permissionG/<id>', methods=['GET'])
def get_permission(id):
  permission = Permiso.query.get(id)
  return permission_schema.jsonify(permission)

@permission.route('/permissionU/<id>', methods=['PUT'])
def update_permission(id):
  permission = Permiso.query.get(id)

  nom = request.json['nom']
  desc = request.json['desc']
  fecha = request.json['fecha']

  permission.nom = nom
  permission.desc = desc
  permission.fecha = fecha

  db.session.commit()

  return permission_schema.jsonify(permission)

@permission.route('/permissionD/<id>', methods=['DELETE'])
def delete_permission(id):
  permission = Permiso.query.get(id)
  db.session.delete(permission)
  db.session.commit()
  return permission_schema.jsonify(permission)