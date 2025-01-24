from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from flask_cors import CORS

app = Flask(__name__)

# MySQL konfigureerimine
app.config['MYSQL_HOST'] = 'host'
app.config['MYSQL_USER'] = 'username'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'database name'
mysql = MySQL(app)

CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})  # Lubab ligipääsu ainult 8080 pordile

@app.route('/signup', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    
    if not username or not password or not email:
        return jsonify({"error": "Palun täitke kõik väljad!"}), 400
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM users WHERE username = %s OR email = %s', (username, email))
    account = cursor.fetchone()
    
    if account:
        return jsonify({"error": "Konto sellise kasutajanime või e-postiga juba eksisteerib!"}), 400
    
    if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        return jsonify({"error": "Kehtetu e-posti aadress!"}), 400
    
    if not re.match(r'[A-Za-z0-9]+', username):
        return jsonify({"error": "Kasutajanimi võib sisaldada ainult tähti ja numbreid!"}), 400
    
    cursor.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)', (username, email, password))
    mysql.connection.commit()
    
    return jsonify({"message": "Konto on edukalt loodud!"}), 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)