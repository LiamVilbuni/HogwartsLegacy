from flask import Blueprint, render_template
from flask_login import login_required, current_user
import json

from db.db import *

chat = Blueprint('chat', __name__, template_folder='templates')

@chat.route('/chats/<chat_id>')
@login_required
def viewChat(chat_id):
    chat = get_chat_by_id(current_user.id, chat_id)[0]
    house_data = json.loads(chat[6])

    houses = {
        "Gryffindor": { 'id': 'gryffindor', 'name': 'Gryffindor', 'color': '#740001', 'accent': '#d3a625', 'desc': 'Bravery, daring, nerve, and chivalry.', 'icon': '🦁' },
        "Slytherin": { 'id': 'slytherin', 'name': 'Slytherin', 'color': '#1a472a', 'accent': '#aaaaaa', 'desc': 'Ambition, cunning, leadership, and resourcefulness.', 'icon': '🐍' },
        "Ravenclaw": { 'id': 'ravenclaw', 'name': 'Ravenclaw', 'color': '#0e1a40', 'accent': '#946b2d', 'desc': 'Intelligence, wisdom, creativity, and wit.', 'icon': '🦅' },
        "Hufflepuff": { 	'id':	'hufflepuff',
			'name':'Hufflepuff',
			'color':'#ecb939',
			'accent':'#372e29',
			'desc':'Hard work, patience, justice, and loyalty.',
			'icon':'🦡'
		}
      }

    if chat:
        return render_template('chat.html', user_logged_in = True, house_data = house_data, user_avatar = current_user.get_avatar(), chat=chat, current_user=current_user, houses=houses)
    else:
        return render_template('error.html')
