from flask import Blueprint, redirect, request, render_template
from flask_login import login_required, current_user
from uuid import uuid4

from db.db import *

chats = Blueprint('chats', __name__, template_folder='templates')

@chats.route('/chats/analyse', methods=['POST'])
@login_required
def addChat():
    chat_name = request.form.get('chat_name')
    chat_data = request.form.get('chat_data')
    chat_id = str(uuid4())
    chat_analysis = "Processed Result"
    add_chat(current_user.id, chat_id, chat_name, chat_data, chat_analysis)
    return redirect('/')

@chats.route('/chats/delete', methods=['POST'])
@login_required
def delChat():
    chat_id = request.form.get('chat_id')
    delete_chat(current_user.id, chat_id)
    return redirect('/')

@chats.route('/chats')
@login_required
def listChat():
    chats = get_chats(current_user.id)
    return render_template('chats.html', chats=chats, current_user=current_user, house_data = {})
