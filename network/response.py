from typing import Any


class Response:
    code: int = 200
    headers: dict = {}
    body: Any
