from flask import Blueprint
from controller import ServicesController, AutorizationController


api_hello = Blueprint('api_hello', __name__)

service_controller = ServicesController()
autorization_controller = AutorizationController()


def api():
    api_hello.add_url_rule('/custom-message',
                           view_func=service_controller.custom_hello_world, methods=['POST']),
    api_hello.add_url_rule('/<language>',
                           view_func=service_controller.choose_language, methods=['GET'])
    api_hello.add_url_rule('/check-client/<id>',
                           view_func=autorization_controller.check_client, methods=['GET'])


api()
