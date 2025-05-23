# app.py – Web version of Stratos

from flask import Flask, request, jsonify
from flask_cors import CORS
from stratos_phi import StratosBrain  # ✅ Fixed this line

app = Flask(__name__)
CORS(app)

stratos = StratosBrain()

@app.route('/')
def home():
    return "✅ STRATOS is online."

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message', '')
        if not user_input:
            return jsonify({'response': "⚠️ You didn't say anything."}), 400

        response = stratos.respond(user_input)
        return jsonify({'response': response}), 200
    except Exception as e:
        return jsonify({'response': f"⚠️ Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
