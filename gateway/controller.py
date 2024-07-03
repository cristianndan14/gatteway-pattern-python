import os
from flask import jsonify
from flask.views import MethodView
from request_proxy import RequestProxy
from helpers import handle_error

request_proxy = RequestProxy()


class HelloController(MethodView):

    url = os.environ.get("URL_API", "http://api:5055")
    headers = {
        "x-secret-key": os.environ.get('SECRET_API_KEY', None),
    }

    def proxy_services(self, path):
        try:
            response = request_proxy.execute(
                url=self.url,
                path=path,
                headers=self.headers
            )
            return response

        except Exception as e:
            return handle_error(e)
