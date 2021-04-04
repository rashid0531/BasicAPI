from flask import Flask, jsonify, request
from http import HTTPStatus
app = Flask(__name__)

recipes = [
    {'id': 1,
    'name': 'Egg Salad',
    'description': 'This is a lovely egg salad recipe.'},

    {'id': 2, 
    'name': 'Tomato Pasta',
    'description': 'This is a lovely tomato pasta recipe.'}
]

@app.route("/")
def hello():
    return 'Hello World'

if __name__ == "__main__":
    app.run()
