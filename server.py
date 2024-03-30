from http.server import HTTPServer, SimpleHTTPRequestHandler

handler = SimpleHTTPRequestHandler

server_address = ('localhost', 8000)
httpd = HTTPServer(server_address, handler)

print('Running server on port:', server_address[1])

httpd.serve_forever()
