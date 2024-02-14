from flask import Flask, jsonify
import json

app = Flask(__name__)
@app.route('/', methods=['GET'])
def get_provinces():
    with open('../data/provinces_data.json', 'r') as file:
        provinces_data = json.load(file)
    return jsonify(provinces_data)

if __name__ == '__main__':
    app.run(debug=True)
