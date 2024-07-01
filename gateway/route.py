from flask import Blueprint
from controllers.hello_controller import HelloController


api_hello = Blueprint('api_hello', __name__, url_prefix='/hello-api')

hello_controller = HelloController()


def api():
    api_hello.add_url_rule('/',
                           view_func=hello_controller.get_services, methods=['GET'])
    api_hello.add_url_rule('/<path>',
                           view_func=hello_controller.get_services_path, methods=['GET'])
    api_hello.add_url_rule('/<path>',
                           view_func=hello_controller.post_services, methods=['POST'])


api()
