import logging

import azure.functions as func
from flask import Flask


def main(req: func.HttpRequest) -> func.HttpResponse:
    app = Flask(__name__)
    logging.info(f'Flask is loaded with app name {app.name}')

    return func.HttpResponse(
        f"Hello Functions World!",
        status_code=200
    )
