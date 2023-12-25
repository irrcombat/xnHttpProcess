from typing import Any


class Request:
    ip: str
    url: str
    host: str
    path: str
    port: int
    scheme: str
    method: str
    headers: dict
    query: str
    body: str


class Response:
    code: int = 200
    headers: dict = {}
    body: Any
