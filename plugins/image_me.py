import requests
import random

def image_me(text):
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

    if len(results) > 0:
      return random.choice(results)["unescapedUrl"]
    else:
      return None
  return None
