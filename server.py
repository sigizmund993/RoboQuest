from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import subprocess
import os
import sys
app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)

TARGET_SCRIPT = "../strategy/main.py"

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/run')
def run_script():
    if os.path.exists(TARGET_SCRIPT):
        try:
            subprocess.Popen([sys.executable, TARGET_SCRIPT])
            return jsonify({"status": "Success"})
        except Exception as e:
            return jsonify({"status": "Error", "message": str(e)}), 500
    return jsonify({"status": "Error", "message": "File not found"}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)