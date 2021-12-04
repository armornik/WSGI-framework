from wsgiref.simple_server import make_server
from framework.main import Framework
from version_as_flask.views_as_flask import routes
from components_common import settings

# Create object WSGI-framework
application = Framework(settings, routes)

with make_server('', 8080, application) as httpd:
    print('Run server on port 8080...')
    httpd.serve_forever()
