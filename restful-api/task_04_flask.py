#!/usr/bin/python3

"""
Simple API using Flask

This API allows users to:
- Retrieve a welcome message (`/`)
- Check the server status (`/status`)
- Get a list of usernames (`/data`)
- Retrieve details of a specific user (`/users/<username>`)
- Add a new user (`/add_user`)

The users are stored in memory and manipulated through Flask routes.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    }
}


@app.route("/")
def home():
    """
    Home endpoint.

    Returns:
        str: A welcome message.
    """
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """
    Status endpoint.

    Returns:
        str: "OK" indicating that the server is running.
    """
    return "OK"


@app.route("/data")
def data():
    """
    Retrieve a list of all usernames stored in the API.

    Returns:
        JSON: A list of usernames.
    """
    usernames_list = [user["username"] for user in users.values()]
    return jsonify(usernames_list)


@app.route("/users/<username>")
def get_user(username):
    """
    Retrieve details of a specific user.

    Args:
        username (str): The username to look up.

    Returns:
        JSON: User details if found, otherwise an error message.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user to the API.

    Request:
        JSON containing "username", "name", "age", and "city".

    Returns:
        JSON: Confirmation message and added user details.
        If "username" is missing, returns an error message.
    """
    global users
    data = request.json

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
