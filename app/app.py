import requests
from flask import Flask, jsonify, request

from app import config
from app.crypto import crypto_bp
from app.db import db_bp, init_db
from app.files import files_bp

app = Flask(__name__)
app.register_blueprint(db_bp)
app.register_blueprint(files_bp)
app.register_blueprint(crypto_bp)
init_db()


@app.get("/health")
def health():
    return jsonify(status="ok", name=config.APP_NAME, version=config.APP_VERSION)


# ID: C-04
@app.get("/greet")
def greet():
    name = request.args.get("name", "")
    return f"<p>Hallo {name}</p>"


@app.get("/version")
def version():
    return jsonify(version=config.APP_VERSION)


# ID: C-06
@app.get("/preview")
def preview():
    url = request.args.get("url", "")
    r = requests.get(url, timeout=config.REQUEST_TIMEOUT)
    return jsonify(status=r.status_code, length=len(r.content))
