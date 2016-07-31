#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask import request
import names_db

app = Flask(__name__)
GET_text = 'Welcome to test web-service. Please use POST request to get json with full user name'

@app.route('/', methods=['POST', 'GET'])
def returnUser():

    if request.method == 'POST':
        id = request.form['id']
    else:
        return GET_text

    if not id.isdigit() or int(id) < 1:
        return 'Invalid "id" value'

    return getUserName(int(id))

def getUserName(id):
    all_names = names_db.names().getFullNameById(id)
    try:
        user_data = all_names[0]
    except IndexError:
        return 'User with "id" = %i not exist' % id
    full_name = formJson(user_data[0], user_data[1], user_data[2])
    return full_name

def formJson(*args):
    user_data = {
        'first_name':args[0],
        'last_name':args[1],
        'patronymic':args[2],
    }
    return jsonify(user_data)

if __name__ == '__main__':
    names_db.names()
    app.debug = True
    app.run()