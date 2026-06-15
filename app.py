from flask import Flask, render_template_string, request, redirect, url_count, session, url_for
from flask_bcrypt import Bcrypt
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
bcrypt = Bcrypt(app)

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

BASE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Secure Auth System</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 50px; background-color: #f4f4f9; }
        .container { max-width: 400px; margin: auto; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        input[type="text"], input[type="password"] { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        button { width: 100%; padding: 10px; background-color: #28a745; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background-color: #218838; }
        .error { color: red; margin-bottom: 10px; }
        .success { color: green; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class="container">
        {{ content | safe }}
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    if "username" in session:
        content = f"""
        <h2>Welcome, {session['username']}!</h2>
        <p>You have successfully authenticated via a secure, cryptographically signed session wrapper.</p>
        <a href="/logout"><button style="background-color: #dc3545;">Secure Logout</button></a>
        """
        return render_template_string(BASE_TEMPLATE, content=content)
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    message = ""
    is_error = True
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        
        if not username or not password:
            message = "Username and password cannot be left blank."
        elif len(password) < 8:
            message = "Password must meet policy requirements (Minimum 8 characters)."
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            try:
                conn = sqlite3.connect("users.db")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, hashed_password))
                conn.commit()
                conn.close()
                message = "Registration successful! You may now log in."
                is_error = False
            except sqlite3.IntegrityError:
                message = "Username already exists. Select a unique identifier."
                
    msg_class = "error" if is_error else "success"
    content = f"""
    <h2>User Registration</h2>
    <div class="{msg_class}">{message}</div>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Register Account</button>
    </form>
    <p><a href="/login">Already have an account? Sign in here.</a></p>
    """
    return render_template_string(BASE_TEMPLATE, content=content)

@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        conn.close()
        
        if row and bcrypt.check_password_hash(row[0], password):
            session["username"] = username
            return redirect(url_for("index"))
        else:
            message = "Invalid access credentials supplied."
            
    content = f"""
    <h2>Secure Login Portal</h2>
    <div class="error">{message}</div>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Authenticate</button>
    </form>
    <p><a href="/register">New user? Register an account here.</a></p>
    """
    return render_template_string(BASE_TEMPLATE, content=content)

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
