from flask import Flask
from werkzeug.urls import url_quote

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, people!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

