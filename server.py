from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open('database.json', 'r') as file:
        data = json.load(file)
    return f"{data}"