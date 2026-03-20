import os
from http.server import BaseHTTPRequestHandler, HTTPServer
TEXT = "Hello from Effective Mobile!"
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            body = TEXT.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        body = b"Not Found"
        self.send_response(404)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, format, *args):
        pass  # отключаем стандартный лог
def main():
    host = "0.0.0.0"
    port = int(os.getenv("PORT", "8080"))
    httpd = HTTPServer((host, port), Handler)
    print(f"Listening on http://{host}:{port}/")
    httpd.serve_forever()
if __name__ == "__main__":
    main()
