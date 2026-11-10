import ipaddress
import os
import subprocess

from flask import Blueprint, abort, jsonify, request, send_file

from app import config

files_bp = Blueprint("files", __name__)


# ID: C-02
@files_bp.get("/tools/ping")
def ping_host():
    host = request.args.get("host", "")
    result = subprocess.run(f"ping -c 1 {host}", shell=True, capture_output=True, text=True, timeout=10)
    return jsonify(returncode=result.returncode, output=result.stdout)


# ID: C-03
@files_bp.get("/files/download")
def download_file():
    name = request.args.get("name", "")
    path = os.path.join(config.DOWNLOAD_DIR, name)
    return send_file(path)


# ID: C-08
@files_bp.get("/tools/trace")
def trace_host():
    try:
        addr = ipaddress.ip_address(request.args.get("host", ""))
    except ValueError:
        abort(400)
    result = subprocess.run(["ping", "-c", "1", str(addr)], capture_output=True, text=True, timeout=10)
    return jsonify(returncode=result.returncode, output=result.stdout)
