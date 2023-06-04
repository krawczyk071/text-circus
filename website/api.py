from flask import Blueprint, request, jsonify
from .models import Todo

api = Blueprint('api', __name__)


@api.route("/", methods=["GET"])
def home():
    todo_list = Todo.query.all()

    return jsonify(todo_list[0].title)
