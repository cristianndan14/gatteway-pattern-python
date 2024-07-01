from flask import request, jsonify, current_app
from flask.views import MethodView
from request_helper import RequestHelper
from controllers.base_controller import BaseController


class HelloController(MethodView, BaseController):

    request_helper = RequestHelper()

    def get_services(self):
        try:
            response = self.request_helper.execute(
                method='GET',
                url=self.url,
                headers=self.headers
            )
            return jsonify(response), 200

        except Exception as e:
            return self._handle_error(e)

    def get_services_path(self, path):
        try:
            response = self.request_helper.execute(
                method='GET',
                url=self.url,
                path=path,
                headers=self.headers
            )
            return jsonify(response), 200

        except Exception as e:
            return self._handle_error(e)

    def post_services(self, path):
        try:
            response = self.request_helper.execute(
                method='POST',
                url=self.url,
                path=path,
                headers=self.headers,
                json_data=request.json
            )
            return jsonify(response), 200

        except Exception as e:
            return self._handle_error(e)
