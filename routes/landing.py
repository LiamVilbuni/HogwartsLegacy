from flask import Blueprint, render_template, session
from flask_login import current_user

from db.db import get_chats

landing = Blueprint('landing', __name__, template_folder='templates')

@landing.route('/')
def landingPage():
    if current_user.is_authenticated:
        chats = get_chats(current_user.id)
        print(current_user.get_avatar())
        session['user_logged_in'] = True
        print(session.get('user_logged_in'))
        session['user_avatar'] = current_user.get_avatar()
        return render_template('index.html', user_logged_in=True, user_avatar=current_user.get_avatar())
    else:
        session['user_logged_in'] = False
        session['user_avatar'] = None
        return render_template('index.html', user_logged_in=False)