class PageNotFound404:
    def __call__(self):
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

        # Find the required controller
        if path in self.routes_lst:
            view = self.routes_lst[path]
        else:
            view = PageNotFound404()

        # Run controller
        code, body = view()
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
