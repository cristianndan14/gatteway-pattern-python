from flask import current_app, jsonify


def handle_error(error):
    """Maneja errores y los registra adecuadamente."""
    current_app.logger.error(f"Error en la solicitud: {error}")
    return jsonify({"code": 500, "message": str(error), "data": []}), 500


def check_db_initialized():
    if not current_app.config.get("DB_INITIALIZED", False):
        return jsonify({"error": "Database not available"}), 503
    return None
