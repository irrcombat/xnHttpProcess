from functools import wraps
import json
from routes import Mapper

from .network import Request, Response


class HttpProcess:
    routing = Mapper()
    middlewares = []
    exception_handlers = {}

    async def run(self, req: Request) -> Response:
        tRouter = self.routing.match(req.path)
        tResult = Response()
        tResult.body = json.dumps(tRouter)
        return tResult

    def get(self, path: str):
        def _wrap(func):
            @wraps(func)
            def wrap_func():
                func()
            self.routing.connect(path, callback=wrap_func)
            return wrap_func
        return _wrap
