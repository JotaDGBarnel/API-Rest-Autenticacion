from flask import request, jsonify, Blueprint
from app.aplicacion import db, ma, Permiso

permission = Blueprint('permission', __name__)

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nom', 'desc', 'fecha')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

@permission.route('/tasks', methods=['Post'])
def create_task():
  nom = request.json['nom']
  desc = request.json['desc']
  fecha = request.json['fecha']

  new_task= Permiso(nom, desc, fecha)

  db.session.add(new_task)
  db.session.commit()

  return task_schema.jsonify(new_task)

@permission.route('/tasks', methods=['GET'])
def get_tasks():
  all_tasks = Permiso.query.all()
  result = tasks_schema.dump(all_tasks)
  return jsonify(result)

@permission.route('/tasks/<id>', methods=['GET'])
def get_task(id):
  task = Permiso.query.get(id)
  return task_schema.jsonify(task)

@permission.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
  task = Permiso.query.get(id)

  nom = request.json['nom']
  desc = request.json['desc']
  fecha = request.json['fecha']

  task.nom = nom
  task.desc = desc
  task.fecha = fecha

  db.session.commit()

  return task_schema.jsonify(task)

@permission.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
  task = Permiso.query.get(id)
  db.session.delete(task)
  db.session.commit()
  return task_schema.jsonify(task)