from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/lignes')
def get_lignes():
    return jsonify([
        {"id": 1, "numero": "1", "depart": "Parcelles", "arrivee": "Pompiers", "arrets": 5},
        {"id": 2, "numero": "2", "depart": "Dakar", "arrivee": "Thiès", "arrets": 8},
     {"id": 3, "numero": "3", "depart": "Guédiawaye", "arrivee": "Plateau", "arrets": 6},
        {"id": 4, "numero": "4", "depart": "Pikine", "arrivee": "Université", "arrets": 7},
        {"id": 5, "numero": "5", "depart": "Rufisque", "arrivee": "Dakar", "arrets": 10},
        {"id": 6, "numero": "6", "depart": "Mbao", "arrivee": "HLM", "arrets": 9},
    ])

if __name__ == '__main__':
    app.run(debug=True)