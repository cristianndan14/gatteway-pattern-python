from flask import jsonify, request
from flask.views import MethodView
from helpers import handle_error, check_db_initialized
from model import Client


class ServicesController(MethodView):

    def custom_hello_world(self):
        try:
            custom_msg = request.json.get("message", None)
            if custom_msg is None:
                return jsonify(
                    {"message": "Porfavor, ingrese su mensaje dentro del campo 'message'."}), 400
            return jsonify(
                {"message": custom_msg}), 200
        except Exception as e:
            return handle_error(e)

    def choose_language(self, language):
        EN = "Hello World!"
        ES = "Hola Mundo!"
        JA = "こんにちは、世界！ (Konnichiwa, sekai!)"
        FR = "Bonjour, le monde!"
        PT = "Olá, mundo!"

        LANGUAGES = {"en": EN, "es": ES, "ja": JA, "fr": FR, "pt": PT}

        try:
            if language.lower() not in LANGUAGES.keys():
                return jsonify(
                    {"message": "Please, input a valid language: en/es/ja/fr/pt"}), 400

            return jsonify({"message": LANGUAGES[language]}), 200
        except Exception as e:
            return handle_error(e)


class AutorizationController(MethodView):

    def check_client(self, id):
        db_check = check_db_initialized()
        if db_check:
            return db_check
        try:
            client = Client.query.get(id)
            if not client:
                return jsonify({"message": "Client not found"}), 404
            return jsonify({"message": "Client found"}), 200
        except Exception as e:
            return handle_error(e)
