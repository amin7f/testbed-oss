import base64
import pickle

from flask import Blueprint, jsonify, request

crypto_bp = Blueprint("session", __name__)


# ID: C-05
@crypto_bp.post("/session/restore")
def restore_session():
    raw = base64.b64decode(request.form.get("state", ""))
    state = pickle.loads(raw)
    return jsonify(sorted(state))
