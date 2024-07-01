import time
import requests
from flask import current_app, request


class RequestHelper:
    VALID_METHODS = ['GET', 'POST', 'PUT',
                     'DELETE', 'PATCH', 'HEAD', 'OPTIONS']

    def __init__(self):
        pass

    def execute(
            self,
            method: str,
            url: str,
            path: str = "",
            headers: dict = None,
            json_data: dict = None,
            params: dict = None
    ):
        start_request = time.time()

        try:
            request_url = url + path
            request_header = self.build_headers(headers)
            print(request_header)
            request_method = self.validate_method(method)
            print(request_method)
            current_app.logger.info(
                f"Enviando solicitud con método: {request_method}, URL: {request_url}, Header: {request_header}, Body: {json_data}, Params: {params}")

            response = request_method(
                url=request_url,
                headers=request_header or {},
                json=json_data,
                params=params
            )
            response.raise_for_status()
            return response.json()

        except ValueError as value_err:
            current_app.logger.error(
                f"Valor no válido: {value_err}. URL: {request_url}, Headers: {request_header}, Params: {params}")
            return {"code": 400, "message": str(value_err), "data": []}

        except requests.exceptions.HTTPError as http_err:
            current_app.logger.error(
                f"HTTP error occurred: {http_err}. URL: {request_url}, Headers: {request_header}, Params: {params}")
            return {"code": response.status_code, "message": str(http_err), "data": []}

        except requests.exceptions.RequestException as req_err:
            current_app.logger.error(
                f"Request error occurred: {req_err}. URL: {request_url}, Headers: {request_header}, Params: {params}")
            return {"code": 500, "message": str(req_err), "data": []}

        finally:
            end_request = time.time()
            elapsed_time = end_request - start_request
            current_app.logger.info(
                f"Solicitud ejecutada con método: {request_method}, URL: {request_url}, Header: {request_header}, Body: {json_data}, Params: {params}. Tiempo transcurrido: {elapsed_time:.2f} segundos.")

    def validate_method(self, method: str):
        if method.upper() not in self.VALID_METHODS:
            raise ValueError(
                f"Método no válido. Métodos válidos: {', '.join(self.VALID_METHODS)}")
        request_method = getattr(requests, method.lower())
        return request_method

    def build_headers(self, base_header):
        """Construye los encabezados para la solicitud."""
        headers = base_header if base_header is not None else {}
        if request.method["METHOD"] != "GET" and "Content-Type" in headers:
            if request.headers["Content-Type"] == "application/json":
                headers["Content-Type"] = request.headers["Content-Type"]
        return headers
