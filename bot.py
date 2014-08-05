import os
from flask import Flask, request
import requests
import json
app = Flask(__name__)
from time import sleep
import random

@app.route('/', methods=['GET', 'POST'])
def hello():
  # Make sure we don't infinite loop
  if 'user_name' not in request.form or request.form['user_name'] == 'slackbot':
    return ''
  text = request.form['text']
  # This should move to a plugin architecture, but for now ... conditionals!
  if text.startswith('image me '):
    search = text.strip('image me ')
    data = {
      "q": search,
      "v": "1.0",
      "safe": "active",
      "rsz": "8"
    }
    r = requests.get("http://ajax.googleapis.com/ajax/services/search/images", params=data)
    results = r.json()["responseData"]["results"]
    d = {}
    if len(results) > 0:
      d['text'] = random.choice(results)["unescapedUrl"]
    else:
      d['text'] = 'Nothing'
    return json.dumps(d)
  elif text.startswith('8ball '):
    responses = ["Definitely.", "Not likely.", "Outlook uncertain.", "Are you kidding me? Absolutely not."]
    d = {}
    d['text'] = random.choice(responses)
    return json.dumps(d)
  else:
    return ''

if __name__ == "__main__":
    app.run(debug = True, use_reloader=True, port = 5000)
