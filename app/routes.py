from flask import Flask, jsonify, request, Blueprint
from .services import db_connect, create_security_context

# create blueprint for routes
routes = Blueprint('routes', __name__)

@routes.route('/')
def hello():
    return 'Hello World!'

@routes.route('/time')
def time():
    hana_conn = db_connect()
    cursor = hana_conn.cursor()
    cursor.execute("SELECT CURRENT_UTCTIMESTAMP FROM DUMMY")
    current_time = cursor.fetchone()
    cursor.close()
    hana_conn.close()
    return jsonify(current_time)

@routes.route('/user')
def user():
    jwt_token = request.headers.get('Authorization').split(' ')[1]
    security_context = create_security_context(jwt_token)
    return jsonify({
        'user_name': security_context.get_logon_name(),
        'email': security_context.get_email(),
        'family_name': security_context.get_family_name(),
        'given_name': security_context.get_given_name(),
        'scopes': security_context.get_granted_scopes()
    })
