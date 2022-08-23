from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return """<h1>Hello. I am alive! I am a friendly robot.</h1>
    <h1>Add me to your discord server by <a href="https://discord.com/api/oauth2/authorize?client_id=853320347368423425&permissions=259846043712&scope=bot">clicking me<a></h1>"""

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
