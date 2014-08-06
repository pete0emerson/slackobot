slackobot
=========

A proof of concept Slack bot

This bot does two things:

1. Responds to "image me ________" with an appropriate google image search, returning a random image
1. Responds to "8ball _________" with a random reply

This code is ready to deploy to Heroku.

# plugin architecture

All .py files in the plugins directory will be loaded. The plugin's function name must match the plugin's file name (without the `.py`). It is the plugin's responsibility to check the text for a desired match. The bot will use the first response that is not None. Here's the `eightball.py` code:

    import random

    def eightball(text):
      if text.startswith('8ball '):
        responses = ["Definitely.", "Not likely.", "Outlook uncertain.", "Are you kidding me? Absolutely not."]
        return random.choice(responses)
      else:
        return None
