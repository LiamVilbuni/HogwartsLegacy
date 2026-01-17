from flask import Blueprint, redirect, request, render_template
from flask_login import login_required, current_user
from uuid import uuid4

from db.db import *

user = Blueprint('user', __name__, template_folder='templates')

@user.route('/chats/analyse', methods=['POST'])
@login_required
def add_chat_route():
    chat_name = request.form.get('chat_name')
    chat_data = request.form.get('chat_data')
    chat_id = str(uuid4())
    chat_analysis = "Processed Result"
    add_chat(current_user.id, chat_id, chat_name, chat_data, chat_analysis)
    return redirect('/')

@user.route('/chats/delete', methods=['POST'])
@login_required
def delete_chat_route():
    chat_id = request.form.get('chat_id')
    delete_chat(current_user.id, chat_id)
    return redirect('/')

@user.route('/chats/<chat_id>')
@login_required
def view_chat_route(chat_id):
    chat = get_chat_by_id(current_user.id, chat_id)
    if chat:
        return render_template('chat.html', chat=chat[0])
    else:
        return "Chat not found", 404

@user.route('/chats')
@login_required
def list_chat_route():
    chats = get_chat(current_user.id)
    return render_template('chats.html', chats=chats)
