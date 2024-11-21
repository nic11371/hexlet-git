from wsgiref.simple_server import make_server
from example import app

def server(wsgi_app):
    servered = make_server('', 8000, wsgi_app)
    print("Serving HTTP on port 8000...")
    servered.serve_forever()

if __name__ == '__main__':
    server(app)