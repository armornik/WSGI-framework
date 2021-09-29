# Processing GET-request with params
class GetRequest:

    @staticmethod
    def parse_input_data(data: str) -> dict:
        result = {}
        if data:
            # Split params from &
            params = data.split('&')
            for item in params:
                # Split key and value from =
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_request_params(environ: dict) -> dict:
        # Get params request
        query_string = environ['QUERY_STRING']
        # Transform params in dict
        request_params = GetRequest.parse_input_data(query_string)
        return request_params


# Processing POST-request with params
class PostRequest:

    @staticmethod
    def parse_input_data(data: str) -> dict:
        result = {}
        if data:
            # Split params from &
            params = data.split('&')
            for item in params:
                # Split key and value from =
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_wsgi_input_data(environ: dict) -> bytes:
        # Get len content
        content_length_data = environ.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        # Read data
        data = environ['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        result = {}
        if data:
            # Decode data to string
            data_str = data.decode(encoding='utf-8')
            # Transform data in dict
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, environ) -> dict:
        # Get data
        data = self.get_wsgi_input_data(environ)
        # Transform data in dict
        data = self.parse_wsgi_input_data(data)
        return data
