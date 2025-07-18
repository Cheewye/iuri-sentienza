from flask import Flask, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)
DATA_PATH = 'sessions.json'

@app.route('/api/save_session', methods=['POST'])
def save_session():
    data = request.json
    data['timestamp'] = datetime.utcnow().isoformat()
    try:
        with open(DATA_PATH, 'a') as f:
            json.dump(data, f)
            f.write('\n')
        return jsonify({'status': 'ok'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/api/stats', methods=['GET'])
def stats():
    try:
        with open(DATA_PATH, 'r') as f:
            lines = f.readlines()
        return jsonify({'count': len(lines)})
    except Exception:
        return jsonify({'count': 0})

if __name__ == '__main__':
    app.run(debug=True)