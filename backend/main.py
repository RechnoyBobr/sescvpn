from flask import Flask, request
import psycopg2

app = Flask(__name__)


conn = psycopg2.connect(
    host="postgres_container",
    database="db",
    user="user1",
    password="password1"
)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'


@app.route('/create', methods=['POST'])
def create():
    username = request.form.get('username')
    email = request.form.get('email')

    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s;", (email,))
    count = 0
    for row in cur:
        count += 1
    if count == 0:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (username, email, sid) VALUES (%s, %s, %s)", (username, email, '1'))
        conn.commit()
    else:
        return 'User already exists!'

    config = {'allowInsecure': 'false', 'flow': 'xtls-rprx-vision', 'fp': 'chrome', 'headerType': 'none',
              'pbk': 'ioo8tRKnTcQYCSjFvBRjKu3M_bzRhS0oYZznqhn52Fo', 'security': 'reality',
              'sid': '1', 'sni': 'www.microsoft.com', 'type': 'tcp#Deutschland'}

    server = 'vless://cb47b11c-220f-4be6-bad3-2613957829dc@94.131.120.53:443?'
    return server + '&'.join([key + '=' + config[key] for key in config])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
