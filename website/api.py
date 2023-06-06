from flask import Blueprint, request, jsonify
from . import db
from .models import Todo
from werkzeug.utils import secure_filename
import os

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


UPLOAD_FOLDER = 'static/files'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@api.route("/upload", methods=["POST"])
def upload():

    # file = form.file.data # First grab the file
    file = request.files['file']
    if not file:
        return 'No file uploaded!', 400

    filename = secure_filename(file.filename)
    mimetype = file.mimetype

    if not filename or not mimetype:
        return 'Bad upload!', 400

    file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
              UPLOAD_FOLDER, secure_filename(file.filename)))  # Then save the file

    return 'File Uploaded!', 200
