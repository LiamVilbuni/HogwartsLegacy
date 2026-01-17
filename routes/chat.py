from flask import Blueprint, redirect, request, render_template
from flask_login import login_required, current_user
from uuid import uuid4

from db.db import *

chat = Blueprint('chat', __name__, template_folder='templates')

@chat.route('/chats/<chat_id>')
@login_required
def viewChat(chat_id):
    chat = get_chat_by_id(current_user.id, chat_id)
    if chat:
        return render_template('chat.html', chat=chat[0])
    else:
        return "Chat not found", 404
