from flask import Flask, make_response
app = Flask(__name__)

@app.route("/")
def index():
    resp = make_response("Hello yeye")
    resp.set_cookie("sessionid", "12345")  # inseguro: sem HttpOnly/Secure
    return resp

