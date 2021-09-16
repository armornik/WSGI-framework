from wsgiref.simple_server import make_server
from framework.main import Framework
from urls import routes

# Create object WSGI-framework
application = Framework(routes)

with make_server('', 8080, application) as httpd:
    print('Run server on port 8080...')
    httpd.serve_forever()
