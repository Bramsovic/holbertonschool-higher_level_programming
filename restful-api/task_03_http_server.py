#!/usr/bin/python3
"""
Module implementing a simple HTTP server.

This module sets up a basic HTTP server using the `http.server` module.
It handles GET requests and provides responses for different endpoints:
- `/` : Returns a simple text message.
- `/data` : Returns a JSON object with sample user data.
- `/status` : Returns a JSON response indicating the API status.
- Other routes return a 404 Not Found error.

The server listens on `localhost:8000` and runs indefinitely.
"""

from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class Server(BaseHTTPRequestHandler):
    """
    Custom HTTP request handler for handling GET requests.

    This class defines how the server responds to different GET requests:
    - `/` returns a plain text message.
    - `/data` returns JSON-formatted user information.
    - `/status` returns a JSON-formatted status message.
    - Undefined routes return a 404 Not Found error.
    """

    def do_GET(self):
        """
        Handle GET requests and send appropriate responses.

        Depending on the request path, the function sends:
        - A plain text response for `/`.
        - A JSON response for `/data` and `/status`.
        - A 404 error for any undefined endpoints.
        """
        path = self.path
        if path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode("utf-8"))

        elif path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            dataj = json.dumps(data)
            self.wfile.write(dataj.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            message = "Endpoint not found".encode("utf-8")
            self.wfile.write(message)


def run(server_class=HTTPServer, handler_class=Server):
    """
    Start the HTTP server on localhost:8000.

    This function initializes and runs the server indefinitely,
    handling requests using the `Server` class.
    """
    server_address = ('localhost', 8000)
    httpd = server_class(server_address, handler_class)
    print("Server started at http://localhost:8000")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
