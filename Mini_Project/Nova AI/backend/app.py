from flask import Flask, request, jsonify
from flask_cors import CORS

from ai_client import get_ai_response

app = Flask(__name__)
CORS(app)  # allows frontend (browser) to talk to backend


@app.route("/chat", methods=["POST"])
def chat():
    """
    Receives user message from frontend,
    sends it to AI, and returns AI response.
    """

    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    user_message = data["message"]

    ai_reply = get_ai_response(user_message)

    return jsonify({"reply": ai_reply})


if __name__ == "__main__":
    app.run(debug=True)
