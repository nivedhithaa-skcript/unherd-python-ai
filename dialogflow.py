from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<h1>Hello, Arindam!</h1>"

@app.route("/json")
def json_world():
    # print(request.args);
    return jsonify(name="Swaathi", day="Saturday");

@app.route("/df", methods=['POST'])
def df_world():
    print(request);
    print(request.args);
    print(request.json);
    
    response = {
      "conversationToken": "abc"
    }
    return jsonify(response);
