import sys
from flask import Flask, request
import os

templ = "vless://{uuid}@{ip}?security=reality&sni=www.microsoft.com&allowInsecure=1&fp=chrome&pbk={pbk}&sid={sid}&type=tcp&flow=xtls-rprx-vision&encryption=none#SESCVPN"
f = open("/ip.txt")
ip = f.readline()
f.close()
def gen_string(users):
    global templ
    with open('/uuid') as f , open('/to.txt') as f1:
        arr =[i for i in f1]
        return templ.format(uuid=f.readline()[:-1], pbk=arr[0][:-1], sid=arr[1][:-1], ip=ip[:-1])


app = Flask(__name__)

@app.route("/", methods=["POST"])
def config():
    users= request.get_json(force=True).get('users_total')
    app.logger.info(users)
    if users is None:
        users = 1
    if users == 1:
        os.system("/bin/bash -c \"/build.sh -n > /etc/xray/config.json; /addUser.sh;\"") 
    else:
        os.system("/bin/bash -c \"/kill.sh; /addUser.sh;\"")
    os.system(" /bin/bash -c \"xray run -c /etc/xray/config.json & disown\"")
    r = gen_string(users)
    app.logger.info(r)
    return r
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7070, debug=True)
