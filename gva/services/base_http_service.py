"""
This is a basic HTTP Server
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import abc

class BaseHTTPService(abc.ABC, BaseHTTPRequestHandler):

    def _extract_query_string(self, path):
        return parse_qs(path[2:])

    def do_GET(self):
        path = self.path.split('/')[0].lower()
        try:
            self.on_request(path, self._extract_query_string(self.path))
        except Exception as err:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(F"{type(err).__name__}\n{err}")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Okay!")

    def do_POST(self):
        path = self.path.split('/')[0].lower()
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)

        try:
            self.on_request(path, parse_qs(post_body))
        except Exception as err:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(F"{type(err).__name__}\n{err}")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Okay!")

    @abc.abstractmethod
    def on_request(self, path, command):
        raise NotImplementedError()
