"""
Task 3.
Implements a server that receives string messages and sends them back in uppercase. Simultaneous processing of
requests from multiple clients is possible. To receive a response from the server, open your browser and enter
the following text in the address bar:
    http://host:port/your_message
        host - server host or server IP-address;
        port - server port;
        your_message - your string message.
"""

from socketserver import ThreadingMixIn
from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.close_connection = True
        request_str = self.path[1:]
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes(f'{request_str.upper()}', 'utf-8'))


class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True


def stop_server(server):
    server.shutdown()
    server.server_close()


def run_server():
    HOST = "0.0.0.0"
    PORT = 8686

    with ThreadingHTTPServer((HOST, PORT), Handler) as httpd:
        print(f'Serving at port {PORT}')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('Server stopped by user')
            stop_server(httpd)
        finally:
            print('Server is going down, run it again manually...')
            if httpd:
                stop_server(httpd)


if __name__ == "__main__":
    run_server()
