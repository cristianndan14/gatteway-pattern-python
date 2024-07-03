from flask import current_app, jsonify


def handle_error(error):
    """Maneja errores y los registra adecuadamente."""
    current_app.logger.error(f"Error en la solicitud: {error}")
    return jsonify({"code": 500, "message": str(error), "data": []}), 500
