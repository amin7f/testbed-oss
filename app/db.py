import sqlite3

from flask import Blueprint, jsonify, request

from app import config

db_bp = Blueprint("users", __name__)


def get_connection():
    return sqlite3.connect(config.DATABASE_PATH)


def init_db():
    with get_connection() as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
        if conn.execute("SELECT COUNT(*) FROM users").fetchone()[0] == 0:
            conn.executemany(
                "INSERT INTO users (name, email) VALUES (?, ?)",
                [("alice", "alice@example.org"), ("bob", "bob@example.org")],
            )


# ID: C-01
@db_bp.get("/users/search")
def search_users():
    name = request.args.get("name", "")
    with get_connection() as conn:
        rows = conn.execute(f"SELECT id, name FROM users WHERE name = '{name}'").fetchall()
    return jsonify(rows)


# ID: C-07
@db_bp.get("/users/lookup")
def lookup_user():
    email = request.args.get("email", "")
    with get_connection() as conn:
        rows = conn.execute("SELECT id, name FROM users WHERE email = ?", (email,)).fetchall()
    return jsonify(rows)
