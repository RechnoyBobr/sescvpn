from flask import Flask, request


def gen_string():
    with open('/to.txt') as f:
        arr = [i for i in f]
        templ = "vless://{uuid}@{ip}?security=reality&sni=www.microsoft.com&allowInsecure=1&fp=chrome&pbk={pbk}&sid={sid}&type=tcp&flow=xtls-rprx-vision&encryption=none#SESCVPN"\
            .format(pbk=arr[0],sid=arr[1], uuid=arr[2], ip=arr[3])
        return templ
app = Flask(__name__)

@app.route("/", methods=["POST"])
def  Config():
    return gen_string()
