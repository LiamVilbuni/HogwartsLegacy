from flask import Blueprint, redirect, request, render_template
from flask_login import login_required, current_user
from uuid import uuid4

from db.db import *

chat = Blueprint('chat', __name__, template_folder='templates')

@chat.route('/chats/<chat_id>')
@login_required
def viewChat(chat_id):
    chat = get_chat_by_id(current_user.id, chat_id)
    house_data = {'Gryffindor': ['Harry', 'Ron'], 'Hufflepuff': [''], 'Ravenclaw': [''], 'Slytherin': ['Draco']}

    if chat:
        return render_template('chat.html', user_logged_in = True, house_data = house_data, user_avatar = current_user.get_avatar(), chat=chat, current_user=current_user)
    else:
        return "Chat not found", 404
