from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def get_connection():
    # Переконайтеся, що ці дані збігаються з налаштуваннями вашого docker-compose.yml
    return psycopg2.connect(
        host="db",
        database="mydb",
        user="root",
        password="toor"
    )

@app.route("/users", methods=["GET"])  
def get_users():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users;")
        users = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(users)
    except Exception as e:
        return str(e), 500

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    name = data.get("name")
    if not name:
        return "Name is required", 400

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (name) VALUES (%s);", (name,)
        )
        conn.commit()
        cur.close()
        conn.close()
        return "User added!", 201
    except Exception as e:
        return str(e), 500

@app.route("/users/<int:user_id>", methods=["DELETE"])  
def delete_user(user_id):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM users WHERE id=%s;",
            (user_id,)
        )
        conn.commit()
        cur.close()
        conn.close()
        return f"User with id {user_id} deleted!"
    except Exception as e:
        return str(e), 500

@app.route("/")
def home():
    return "Hello Vika, this is Flask!"

@app.route("/about")
def about():
    return "This is about page!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
