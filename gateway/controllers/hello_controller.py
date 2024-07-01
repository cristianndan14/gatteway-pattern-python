from flask import jsonify
from flask.views import MethodView
from request_proxy import RequestProxy
from controllers.base_controller import BaseController


class HelloController(MethodView, BaseController):

    request_proxy = RequestProxy()

    def proxy_services(self, path):
        try:
            response = self.request_proxy.execute(
                url=self.url,
                path=path,
                headers=self.headers
            )
            return jsonify(response), 200

        except Exception as e:
            return self._handle_error(e)
