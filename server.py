from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import subprocess
import os
import sys

app = Flask(__name__)
CORS(app)

# Файл, который будет перезаписываться из Blockly
TARGET_SCRIPT = "main_engine.py"

# Раздача статических файлов (index.html) из текущей папки
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/run')
def run_script():
    print(f"--- Команда на запуск: {TARGET_SCRIPT} ---")
    if os.path.exists(TARGET_SCRIPT):
        try:
            # Запуск скрипта в новом процессе
            subprocess.Popen([sys.executable, TARGET_SCRIPT])
            return jsonify({"status": "Success"})
        except Exception as e:
            return jsonify({"status": "Error", "message": str(e)}), 500
    return jsonify({"status": "Error", "message": "File not found"}), 100

if __name__ == '__main__':
    print("\n" + "="*50)
    print("ПРИЛОЖЕНИЕ ЗАПУЩЕНО!")
    print(f"Адрес в браузере: http://localhost:5000")
    print("="*50 + "\n")
    app.run(port=7000)