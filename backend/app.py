from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route("/enjambre", methods=["GET"])
def obtener_enjambre():
    ruta = os.path.join(os.path.dirname(__file__), 'enjambre.json')
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
        return jsonify(datos)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/")
def home():
    return "🧠 iURi Sentienza Backend Activo – Modo Enjambre 🌐"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
