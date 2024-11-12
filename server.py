from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    with open('database.json', 'r') as file:
        data = json.load(file)
    return f"{data}"