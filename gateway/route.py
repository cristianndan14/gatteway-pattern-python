from flask import Blueprint
from controller import HelloController


api_hello = Blueprint('api_hello', __name__, url_prefix='/api/v1/hello-api')

hello_controller = HelloController()

all_methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS']


def api():
    api_hello.add_url_rule('/<path>',
                           view_func=hello_controller.proxy_services, methods=all_methods)


api()
