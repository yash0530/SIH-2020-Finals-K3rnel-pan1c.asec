import json
import requests

from flask import Flask, render_template
from flask import request
from engine.chatbot import engine
from flask_cors import CORS

from giveHTMLFromIntents import giveHTMLFromIntents

import smtplib, ssl, sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(you, html):
  me = "kernelpanic.asec@gmail.com"
  # Create message container - the correct MIME type is multipart/alternative.
  msg = MIMEMultipart('alternative')
  msg['Subject'] = "Response from chatbot"
  msg['From'] = me
  msg['To'] = you
  part2 = MIMEText(html, 'html')
  # Attach parts into message container.
  msg.attach(part2)

  # sendmail function takes 3 arguments: sender's address, recipient's address
  # and message to send - here it is sent as one string.
  s = smtplib.SMTP('smtp.gmail.com', 587)

  s.ehlo()
  s.starttls()
  print("before login")
  s.login('kernelpanic.asec@gmail.com', 'k3rnel-pan1c.asec')
  print("after")
  s.sendmail(me, you, msg.as_string())
  s.quit()

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/chatbot/", methods=["GET", "POST"])
def index():
    # parsing = engine.parse("How are you?")
    # print(parsing['intent'])
    if request.method == "POST":
        # print(request.form)
        # print("behwbehwehwjvdewvewjvh")
        user_query = request.form["user_query"]
        parsing = engine.parse(user_query)
        # print(parsing)
        # print(parsing.intent)
        # json_response = json.dumps(parsing, indent=2)
        # url = ""
        # requests.post(url, json_response)
        return giveHTMLFromIntents(parsing)
    else:
        return "<h1>CHATBOT RUNNING....</h1>"

@app.route("/email/", methods=["POST"])
def email():
    if request.method == "POST":
        print(request.form['content'])
        print('inside email route.')
        sendEmail("divy9881@gmail.com", request.form["content"])
    return "Hopefully done"


@app.route("/stt/", methods=["POST"])
def stt():
    if request.method == "POST":
        file = request.files["file"]
        file.save("./audio.wav")

    return request.data


if __name__=="__main__":
    app.run(debug=True)