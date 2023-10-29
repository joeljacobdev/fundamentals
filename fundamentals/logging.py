import asyncio
import logging
import uuid
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response


class ObservabilityMiddleware(BaseHTTPMiddleware):
    async def dispatch(
            self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        request.state.request_id = uuid.uuid4()
        response = await call_next(request)
        return response


class PrefixAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        return f"{self.extra['request_id']} {msg}", kwargs


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()
app.add_middleware(ObservabilityMiddleware)


@app.get('/', status_code=200)
async def logger_view(request: Request):
    logger_adapter = PrefixAdapter(logger, {'request_id': request.state.request_id})
    logger_adapter.info('Hello')
    await asyncio.sleep(1)
    logger_adapter.info('bye!!!!!!!')
