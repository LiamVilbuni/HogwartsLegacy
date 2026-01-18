from flask import Blueprint, jsonify, redirect, request, render_template
from flask_login import login_required, current_user
from uuid import uuid4

from db.db import *

chats = Blueprint('chats', __name__, template_folder='templates')

@chats.route('/chats/analyse', methods=['POST'])
@login_required
def addChat():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not file.filename.endswith('.txt'):
        return jsonify({'error': 'Invalid file type'}), 400
    
    chat_name = file.filename
    chat_data = file.read().decode('utf-8')
    chat_id = str(uuid4())
    chat_analysis = "Test Result" 
    
    add_chat(current_user.id, chat_id, chat_name, chat_data, chat_analysis)
    print("Chat added successfully")
    return jsonify({'message': 'Chat uploaded successfully', 'chat_id': chat_id}), 200

@chats.route('/chats/delete/<chat_id>')
@login_required
def delChat(chat_id):
    delete_chat(current_user.id, chat_id)
    return redirect('/chats')

@chats.route('/chats')
@login_required
def listChat():
    chats = get_chats(current_user.id)
    return render_template('chats.html', user_logged_in=True, user_avatar = current_user.get_avatar(), chats=chats, current_user=current_user, house_data = {})
