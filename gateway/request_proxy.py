import time
import requests
from flask import current_app, request


class RequestProxy:
    VALID_METHODS = ['GET', 'POST', 'PUT',
                     'DELETE', 'PATCH', 'HEAD', 'OPTIONS']

    def __init__(self):
        pass

    def execute(
            self,
            url: str,
            path: str = "",
            headers: dict = None
    ):
        start_request = time.time()

        try:
            _url = url + path
            _header = self.build_headers(headers)
            _method = self.validate_method(request.method)
            json_data = request.json if request.json else None
            params = None
            current_app.logger.info(
                f"Enviando solicitud: METHOD '{request.method}' - URL '{_url}' - Header '{_header}' - Body: {json_data} - Params: {params}")

            response = _method(
                url=_url,
                headers=_header or {},
                json=json_data,
                params=params
            )
            response.raise_for_status()
            return response.json()

        except ValueError as value_err:
            current_app.logger.error(
                f"Valor no válido: '{value_err}'. URL '{_url}' - Header '{_header}' - Body: {json_data} - Params: {params}")
            return {"code": 400, "message": str(value_err), "data": []}

        except requests.exceptions.HTTPError as http_err:
            current_app.logger.error(
                f"HTTP error: '{http_err}'. URL '{_url}' - Header '{_header}' - Body: {json_data} - Params: {params}")
            return {"code": response.status_code, "message": str(http_err), "data": []}

        except requests.exceptions.RequestException as req_err:
            current_app.logger.error(
                f"Request error: '{req_err}'. URL '{_url}' - Header '{_header}' - Body: {json_data} - Params: {params}")
            return {"code": 500, "message": str(req_err), "data": []}

        finally:
            end_request = time.time()
            elapsed_time = end_request - start_request
            current_app.logger.info(
                f"Solicitud ejecutada: METHOD '{request.method}' - URL '{_url}' - Header '{_header}' - Body: {json_data} - Params: {params}. Tiempo transcurrido: {elapsed_time:.2f} segundos.")

    def validate_method(self, method: str):
        try:
            if method.upper() not in self.VALID_METHODS:
                raise ValueError(
                    f"Método no válido. Métodos válidos: {', '.join(self.VALID_METHODS)}")
            request_method = getattr(requests, method.lower())
            return request_method
        except Exception as e:
            current_app.logger.error(f"Ocurrio un error en la funcion validate_method: {e}")
            raise

    def build_headers(self, base_header):
        headers = base_header if base_header is not None else {}
        try:
            if request.method != "GET" and "Content-Type" in headers:
                if request.headers["Content-Type"] == "application/json":
                    headers["Content-Type"] = request.headers["Content-Type"]
            return headers
        except Exception as e:
            current_app.logger.error(f"Ocurrio un error en la funcion build_headers: {e}")
            raise
