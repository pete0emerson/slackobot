import random

def eightball(text):
  if text.startswith('8ball '):
    responses = ["Definitely.", "Not likely.", "Outlook uncertain.", "Are you kidding me? Absolutely not."]
    return random.choice(responses)
  else:
    return None
