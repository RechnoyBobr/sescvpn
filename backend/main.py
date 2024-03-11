from flask import Flask, request
from flask_cors import CORS, cross_origin
import requests
import sys
import psycopg2

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS']='Content-type'

conn = psycopg2.connect(
    host="postgres",
    database="db",
    user="postgres",
    password="password1"
)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Good VPN service'


@app.route('/create', methods=['POST'])
@cross_origin()
def create():
    login = request.get_json(force=True).get('login')
    email = request.get_json(force=True).get('email')
    app.logger.info(login)
    # is_reverse = request.form.getlist('is_reverse')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s;", (email,))
    count = 0
    for row in cur:
        count += 1
    if count == 0:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (login, email) VALUES (%s, %s)", (login, email))
        conn.commit()
    else:
        return 'User already exists!'

    config = {'allowInsecure': 'false', 'flow': 'xtls-rprx-vision', 'fp': 'chrome', 'headerType': 'none',
              'pbk': 'ioo8tRKnTcQYCSjFvBRjKu3M_bzRhS0oYZznqhn52Fo', 'security': 'reality',
              'sid': '1', 'sni': 'www.microsoft.com', 'type': 'tcp#Deutschland'}

    server = 'vless://cb47b11c-220f-4be6-bad3-2613957829dc@94.131.120.53:443?'
    sql = 'SELECT count(*) FROM users;'
    data = []
    cur.execute(sql, data)
    results = cur.fetchone()

    number = 0
    app.logger.info(results)
    for r in results:
        number = r
    if number < 1:
        number = 1
    json_data = {'users_total': number}
    cur.close()
    app.logger.info(json_data)
    res = requests.post('http://xray:7070', json=json_data)
    result = app.response_class(
        response = res,
        status=200,
        mimetype='application/json'
    )
    app.logger.info(res)
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
