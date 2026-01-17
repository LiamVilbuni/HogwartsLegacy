from flask import Blueprint, redirect, request, render_template
from flask_login import login_required, current_user
from uuid import uuid4

from db.db import *

user = Blueprint('user', __name__, template_folder='templates')

@user.route('/user/content/add', methods=['POST'])
@login_required
def add_content_route():
    content_name = request.form.get('content_name')
    content_data = request.form.get('content_data')
    content_id = str(uuid4())
    result = "Processed Result"
    add_content(current_user.id, content_id, content_name, content_data, result)
    return redirect('/')

@user.route('/user/content/<content_id>/delete', methods=['POST'])
@login_required
def delete_content_route(content_id):
    delete_content(current_user.id, content_id)
    return redirect('/')

@user.route('/user/content/<content_id>')
@login_required
def view_content_route(content_id):
    content = get_content_by_id(current_user.id, content_id)
    if content:
        return render_template('content.html', content=content[0])
    else:
        return "Content not found", 404

@user.route('/user/content')
@login_required
def list_content_route():
    content = get_content(current_user.id)
    return render_template('user.html', content=content)

