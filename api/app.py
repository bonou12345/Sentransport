from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/lignes')
def get_lignes():
    with open('lignes_ddd.json', 'r', encoding='utf-8') as f:
        lignes = json.load(f)
    return jsonify(lignes)

@app.route('/lignes/<int:id>')
def get_ligne(id):
    with open('lignes_ddd.json', 'r', encoding='utf-8') as f:
        lignes = json.load(f)
    ligne = next((l for l in lignes if l['id'] == id), None)
    if ligne is None:
        return jsonify({"erreur": "Ligne non trouvée"}), 404
    return jsonify(ligne)

with open("arrets.json", "r") as f:
    arrets = json.load(f)

@app.route("/arrets")
def get_arrets():
    return jsonify(arrets)
if __name__ == '__main__':
    app.run(debug=True)