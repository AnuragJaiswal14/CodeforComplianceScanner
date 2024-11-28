# app.py
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 8000

class Handler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        return  # Suppress logging for simplicity
print("hello world")

# Start the server
with TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving HTTP on port {PORT}")
    httpd.serve_forever()