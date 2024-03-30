from flask import Flask, request, jsonify
import sqlite3

# Database connection (replace with your connection details)
conn = sqlite3.connect('users.db')  # Change database filename

app = Flask(__name__)

# Define your business information as a dictionary
business_info = {
    "name": "AK-IMPORTS",
    "address": "123 Cat Street, Madina, GA",
    "phone": "(233) 555-1212",
    "email": "info@akimports.com",
    "website": "https://www.akimports.com",
    "social_media": {
        "facebook": "https://www.facebook.com/yourbusiness",
        "twitter": "https://twitter.com/yourbusiness",
    },
    # Add other relevant information if needed
}

@app.route('/api/business_info')
def get_business_info():
  """Returns business information as JSON"""
  return jsonify(business_info)

@app.route('/api/users', methods=['POST'])
def insert_user():
  # Extract user data from request body (assuming JSON format)
  data = request.get_json()
  username = data.get('username')
  email = data.get('email')

  # Prepare SQL statement
  sql = "INSERT INTO users (username, email) VALUES (?, ?)"

  try:
    # Execute the statement with data
    conn.execute(sql, (username, email))
    conn.commit()
    return jsonify({'message': 'User created successfully'}), 201
  except Exception as e:
    # Handle errors (e.g., database errors, duplicate entries)
    return jsonify({'error': str(e)}), 400

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
  # Prepare SQL statement
  sql = "DELETE FROM users WHERE id = ?"

  try:
    # Execute the statement with user ID
    conn.execute(sql, (user_id,))
    conn.commit()
    return jsonify({'message': 'User deleted successfully'}), 204
  except Exception as e:
    # Handle errors (e.g

if __name__ == '__main__':
  app.run(debug=True)
