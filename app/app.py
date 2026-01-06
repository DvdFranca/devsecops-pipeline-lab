from flask import Flask, request
import sqlite3

app = Flask(__name__)

# ❌ VULNERABILIDADE 1: Secret hardcoded
API_KEY = "sk_test_1234567890"

def get_db():
    return sqlite3.connect("users.db")

@app.route("/")
def home():
    return "DevSecOps Vulnerable App"

@app.route("/login", methods=["GET"])
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    # ❌ VULNERABILIDADE 2: SQL Injection
    query = f"""
        SELECT * FROM users
        WHERE username = '{username}'
        AND password = '{password}'
    """

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        return "Login successful"
    else:
        return "Login failed"

if __name__ == "__main__":
    # ❌ VULNERABILIDADE 3: Debug habilitado
    app.run(host="0.0.0.0", port=5000, debug=True)
