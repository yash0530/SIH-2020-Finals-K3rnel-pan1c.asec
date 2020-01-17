import json
import requests

from flask import Flask
from flask import request
from engine.chatbot import engine
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print("behwbehwehwjvdewvewjvh")
        user_query = request.form["user_query"]
        parsing = engine.parse(user_query)
        json_response = json.dumps(parsing, indent=2)
        url = ""
        requests.post(url, json_response)
        return json_response
    else:
        return "<h1>CHATBOT RUNNING....</h1>"

if __name__=="__main__":
    app.run(debug=True)