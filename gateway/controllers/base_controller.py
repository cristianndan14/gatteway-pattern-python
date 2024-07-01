import os
from flask import current_app, jsonify


class BaseController():

    url = os.environ.get("URL_API", "http://api:5055")
    headers = {
        "x-secret-key": os.environ.get('SECRET_API_KEY', None),
    }

    def _handle_error(self, error):
        """Maneja errores y los registra adecuadamente."""
        current_app.logger.error(f"Error en la solicitud: {error}")
        return jsonify({"code": 500, "message": str(error), "data": []}), 500
