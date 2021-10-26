# Decorator for routing implementation
class AppRoute:
    def __init__(self, routes, url):
        """
        Save the value passed param
        :param routes:
        :param url:
        """
        self.routes = routes
        self.url = url

    def __call__(self, cls):
        """
        The decorator himself - add dict with object class
        :param cls:
        :return:
        """
        self.routes[self.url] = cls()
