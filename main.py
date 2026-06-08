from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)  # 🔥 allows your 5500 frontend to connect

MODEL = "llama3.2:1b"

@app.route("/")
def home():
    return "AI Server Running"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": user_message}]
    )

    return jsonify({
        "reply": response["message"]["content"]
    })

if __name__ == "__main__":
    app.run(debug=True)