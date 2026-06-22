from flask import Flask,request,render_template,jsonify,abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
    return "<p>Hello World</p>"