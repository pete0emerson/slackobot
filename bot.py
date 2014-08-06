import os
from flask import Flask, request
import requests
import json
app = Flask(__name__)
from time import sleep
import random
import imp
import logging

PLUGIN_FOLDER = './plugins'
if 'SLACK_TOKEN' in os.environ:
  SLACK_TOKEN = os.environ['SLACK_TOKEN']
else:
  SLACK_TOKEN = None

def getPlugins():
    plugins = []
    possibleplugins = os.listdir(PLUGIN_FOLDER)
    for file in possibleplugins:
      if file.endswith(".py"):
        module_name = file.replace(".py", "")
        location = os.path.join(PLUGIN_FOLDER, file)
        plugin = imp.load_source(module_name, location)
        plugins.append({"name": module_name, "function": plugin})
    return plugins

plugins = getPlugins()

@app.route('/', methods=['GET', 'POST'])
def hello():
  if 'user_name' not in request.form or request.form['user_name'] == 'slackbot':
    return ''
  if 'text' not in request.form:
    return ''
  if SLACK_TOKEN and ('token' not in request.form or request.form['token'] != SLACK_TOKEN):
    return ''
  text = request.form['text']
  response = None
  for plugin in plugins:
    name = plugin["name"]
    response = getattr(plugin["function"], name)(text)
    if response:
      break
  if response:
    d = {"text":response}
    return json.dumps(d)
  else:
    return ''

if __name__ == "__main__":
  app.run(debug = True, use_reloader=True, port = 5000)
