from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "ok", "message": "Flask está funcionando!"})

@app.route("/api/test")
def test():
    database_url = os.environ.get('DATABASE_URL', 'Não configurada')
    return jsonify({
        "status": "ok",
        "database_url_exists": bool(os.environ.get('DATABASE_URL')),
        "python_version": "3.x",
        "message": "API básica funcionando"
    })

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)