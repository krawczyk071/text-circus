from flask import Blueprint, render_template, request, redirect, url_for
from .models import Todo
from . import db

views = Blueprint('views', __name__)


@views.route("/")
def home():

    # new_todo = Todo(title="todo 1", complete=False)
    # db.session.add(new_todo)
    # db.session.commit()

    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


@views.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("views.home"))


@views.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("views.home"))


@views.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("views.home"))
