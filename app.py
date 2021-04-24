from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)

recipes = [
    {
        'id': 1,
        'name': 'Egg Salad',
        'description': 'This is a lovely egg salad recipe.'
    },

    {
        'id': 2,
        'name': 'Tomato Pasta',
        'description': 'This is a lovely tomato pasta recipe.'
    }
]


@app.route('/')
def hello():
    return jsonify({'message': 'Hello Hello'}), HTTPStatus.OK


@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = next((rcp for rcp in recipes if rcp['id'] == recipe_id), None)
    if recipe:
        return jsonify(recipe), HTTPStatus.OK
    else:
        jsonify({'message': 'Not Found'}), HTTPStatus.NOT_FOUND


@app.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.get_json()
    manual_id = len(recipes) + 1

    recipe = {
        'id': manual_id,
        'name': data.get('name'),
        'description': data.get('description'),
    }

    recipes.append(recipe)
    return jsonify(recipe), HTTPStatus.CREATED


@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe_idx = next((idx for idx, rcp in enumerate(
        recipes) if rcp['id'] == recipe_id), None)
    if recipe_idx is not None:
        del recipes[recipe_idx]
        return jsonify({'data': recipes}), HTTPStatus.OK
    else:
        return jsonify({'message': 'Not Found'}), HTTPStatus.NOT_FOUND


if __name__ == '__main__':
    app.run()
