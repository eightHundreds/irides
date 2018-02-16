'''
from flask import render_template, flash, redirect, url_for, request, \
    current_app, abort, make_response, jsonify
from flask.ext.login import login_required, current_user
from flask.ext.sqlalchemy import get_debug_queries


@app.route('/api/users', methods = ['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400) # missing arguments
    if User.query.filter_by(username = username).first() is not None:
        abort(400) # existing user
    user = User(username = username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({ 'username': user.username }), 201, {'Location': url_for('get_user', id = user.id, _external = True)}
'''
from app import InitDataGenerator
from . import blueprint as main

@main.route('/alive')
def alive():
    return 'Ok'

@main.route('/seed')
def seedDb():
    generator = InitDataGenerator()
    generator.init_all()
    return 'Db seeded'