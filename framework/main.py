import inspect
import quopri
from framework.framework_requests import GetRequest, PostRequest


class PageNotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not found'


class Framework:

    """Basis class WSGI-framework"""

    def __init__(self, routes_obj):
        self.routes_lst = routes_obj

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
        else:
            view = PageNotFound404()

        # Run controller
        print(f'inspect={inspect.getfullargspec(view)}')
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace('+', ' '), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data
