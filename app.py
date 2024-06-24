import os
from flask import Flask, jsonify, request
from cfenv import AppEnv
from hdbcli import dbapi
from sap import xssec

app = Flask(__name__)
env = AppEnv()

hana = env.get_service(name='my-hana')
port = int(os.environ.get('PORT', 3000))

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/time')
def time():
    conn = dbapi.connect(
        address=hana.credentials['host'],
        port=int(hana.credentials['port']),
        user=hana.credentials['user'],
        password=hana.credentials['password'],
        encrypt='true',
        sslTrustStore=hana.credentials['certificate']
    )
    cursor = conn.cursor()
    cursor.execute("SELECT CURRENT_UTCTIMESTAMP FROM DUMMY")
    current_time = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(current_time)

@app.route('/user')
def user():
    jwt_token = request.headers.get('Authorization').split(' ')[1]
    uaa_service = env.get_service(name='my-xsuaa')
    token_info = xssec.create_security_context(jwt_token, uaa_service.credentials)
    return jsonify({
        'user_name': token_info.get_logon_name(),
        'email': token_info.get_email(),
        'family_name': token_info.get_family_name(),
        'given_name': token_info.get_given_name(),
        'scopes': token_info.get_granted_scopes()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
