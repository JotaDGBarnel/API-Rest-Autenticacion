from flask import request, jsonify, Blueprint
from app.aplicacion import db, ma, Rol

role = Blueprint('rol', __name__)

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nom', 'desc', 'fecha')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

@role.route('/tasks', methods=['Post'])
def create_task():
  nom = request.json['nom']
  desc = request.json['desc']
  fecha = request.json['fecha']

  new_task= Rol(nom, desc, fecha)

  db.session.add(new_task)
  db.session.commit()

  return task_schema.jsonify(new_task)

@role.route('/tasks', methods=['GET'])
def get_tasks():
  all_tasks = Rol.query.all()
  result = tasks_schema.dump(all_tasks)
  return jsonify(result)

@role.route('/tasks/<id>', methods=['GET'])
def get_task(id):
  task = Rol.query.get(id)
  return task_schema.jsonify(task)

@role.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
  task = Rol.query.get(id)

  nom = request.json['nom']
  desc = request.json['desc']
  fecha = request.json['fecha']

  task.nom = nom
  task.desc = desc
  task.fecha = fecha

  db.session.commit()

  return task_schema.jsonify(task)

@role.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
  task = Rol.query.get(id)
  db.session.delete(task)
  db.session.commit()
  return task_schema.jsonify(task)
