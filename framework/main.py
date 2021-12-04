import inspect
import quopri
from os import path

from framework.framework_requests import GetRequest, PostRequest
from components_common.content_types import CONTENT_TYPES_MAP


class PageNotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not found'


class Framework:

    """Basis class WSGI-framework"""

    def __init__(self, settings, routes_obj):
        self.routes_lst = routes_obj
        self.settings = settings

    def __call__(self, environ: dict, start_response):
        # Get the address to which the user made the transition
        path = environ['PATH_INFO']

        # Add end slash
        if not path.endswith('/'):
            path = f'{path}/'

        request = {}
        # Give data request
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequest().get_request_params(environ)
            request['data'] = data
            print(f'We get POST-request: {Framework.decode_value(data)}')
        if method == 'GET':
            request_params = GetRequest().get_request_params(environ)
            request['request_params'] = request_params
            print(f'We get GET-params: {request_params}')

        # Find the required controller
        if path in self.routes_lst:
            view = self.routes_lst[path]
            content_type = self.get_content_type(path)
            code, body = view(request)
            body = body.encode('utf-8')

        elif path.startswith(self.settings.STATIC_URL):
            # /static/images/ -> /images/
            file_path = path[len(self.settings.STATIC_URL):len(path) - 1]
            print(file_path)
            content_type = self.get_content_type(file_path)
            print(content_type)
            code, body = self.get_static(self.settings.STATIC_FILES_DIR, file_path)
        else:
            view = PageNotFound404()
            content_type = self.get_content_type(path)
            code, body = view(request)
            body = body.encode('utf-8')

        # Run controller
        # print(f'inspect={inspect.getfullargspec(view)}')
        start_response(code, [('Content-Type', content_type)])
        return [body]

    @staticmethod
    def get_content_type(file_path, content_types_map=CONTENT_TYPES_MAP):
        file_name = path.basename(file_path).lower() # styles.css
        extention = path.splitext(file_name)[1] # .css
        print(extention)
        return content_types_map.get(extention, 'text/html')

    @staticmethod
    def get_static(static_dir, file_path):
        path_to_file = path.join(static_dir, file_path)
        with open(path_to_file, 'rb') as f:
            file_content = f.read()
        status_code = '200 OK'
        return status_code, file_content

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace('+', ' '), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data
