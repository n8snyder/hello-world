from flask import Flask

app = Flask(__name__)


@app.get("/")
def homepage():
    return "Hello World"
