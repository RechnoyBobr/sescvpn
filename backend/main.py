from flask import Flask, request
import requests
import psycopg2

app = Flask(__name__)

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
def create():
    login = request.form.get('login')
    email = request.form.get('email')
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
    for r in results:
        number = r
    json_data = {'users_total': number}
    res = requests.post('https://x-ray:6000', json=json_data)
    return server + '&'.join([key + '=' + config[key] for key in config])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
