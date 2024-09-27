# create a flask app
from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/')
def index():
    return "Hey there! Welcome to the Flask app."

if __name__ == '__main__':
    app.run()

