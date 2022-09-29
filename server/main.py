from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

import os


class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write('<html><head><meta charset="utf-8">'.encode())
            self.wfile.write(
                '<title>Простой HTTP-сервер.</title></head>'.encode())
            self.wfile.write(
                '<body>Был получен GET-запрос.</body></html>'.encode())
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write('<html><head><meta charset="utf-8">'.encode())
            self.wfile.write('<title>404</title></head>'.encode())
            self.wfile.write(
                '<body>Не найдено</body></html>'.encode())


def run(server_class=HTTPServer, handler_class=HttpGetHandler):
    port = os.environ.get("SERVER_PORT")
    if len(port) == 0:
        print("port hasn't been specified")
        return

    server_address = ("", int(port))
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


if __name__ == "__main__":
    run()
