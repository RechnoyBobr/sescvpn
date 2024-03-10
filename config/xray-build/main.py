from flask import Flask, request
import os
users = 0

def loadCount():
    with open('/users') as f:
        return int(f.readline())

def updateCount():
    global users
    with open('/users', 'w') as f:
        if users != 0:
            f.write(str(users))

templ = "vless://{uuid}@127.0.0.1?security=reality&sni=www.microsoft.com&allowInsecure=1&fp=chrome&pbk={pbk}&sid={sid}&type=tcp&flow=xtls-rprx-vision&encryption=none#SESCVPN"

def gen_string():
    global templ
    if users == 1:
        with open('/to.txt') as f:
            arr = [i for i in f]
            a =templ.format(pbk=arr[0],sid=arr[1], uuid=arr[2])
            templ = templ.format(pbk=arr[0], sid=arr[1])
            return a
    else: 
        with open('/uuid') as f:
            return templ.format(uuid=f.readline())


app = Flask(__name__)

@app.route("/", methods=["POST"])
def  Config():
    global users
    users= request.form.get('userCount')
    if users == 1:
        os.system("/build.sh -n > /etc/xray/config.json && /addUser.sh  && xray run")
    else:
        os.system("/kill.sh && /addUser.sh  && xray run")
    return gen_string()

if __name__ == "__main__":
    app.run(port=6000)
        
