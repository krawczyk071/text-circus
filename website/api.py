from flask import Blueprint, request, jsonify
from . import db
from .models import Todo

api = Blueprint('api', __name__)


@api.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        return jsonify({
            'name': name
        })
    else:
        # todo_list = Todo.query.all()
        todo_list = []

        for todo in Todo.query.all():
            x = todo.__dict__
            x.pop('_sa_instance_state', None)
            todo_list.append(x)

        print(todo_list)
        return jsonify(todo_list)


@api.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({
        'id': new_todo.id,
        'title': new_todo.title,
        'complete': new_todo.complete,
    })
