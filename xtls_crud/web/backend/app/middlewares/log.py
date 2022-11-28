import typing as t
import time


from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp

from nice_tools import NiceLogger


class RouteLoggerMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app: ASGIApp,
        *,
        logger: t.Optional[t.Any] = None,
        skip_routes: t.List[str] = None,  # noqa
    ):
        self._logger = logger if logger else NiceLogger('RouteLoggerMiddleware')
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: t.Callable) -> Response:
        return await self._execute_request_with_logging(request, call_next)

    @staticmethod
    def _time() -> float:
        return time.perf_counter()

    @staticmethod
    def _took(start_time: float, finish_time: float) -> float:
        return finish_time - start_time

    @staticmethod
    async def _collect_data(request: Request) -> t.Dict[str, t.Any]:
        return {
            'client_ip': request.client.host + ':' + str(request.client.port),
            'user_agent': request.headers.get('User-Agent', 'unknown'),
            'method': request.method,
            'path': request.url.path,
            'query': request.url.query,
            'headers': request.headers,
            'form': await request.form(),
            'body': await request.body(),
            'authorization': request.get('Authorization'),
        }

    async def _execute_request_with_logging(
        self, request: Request, call_next: t.Callable
    ) -> Response:
        start_time = self._time()
        response = await self._execute_request(call_next, request)

        finish_time = self._time()
        took = self._took(start_time, finish_time)

        # data = await self._collect_data(request)

        # print(data)

        self._logger.info(
            self._generate_success_log(request, response, took)
        )

        return response

    async def _execute_request(self, call_next: t.Callable, request: Request) -> Response:
        try:
            return await call_next(request)
        except Exception:
            self._logger.exception(
                f"Request failed with exception {request.url.path}, method={request.method}"
            )
            raise

    @staticmethod
    def _generate_success_log(
        request: Request, response: Response, execution_time: float
    ):
        overall_status = "successful" if response.status_code < 400 else "failed"
        return f"Request {overall_status}, " \
               f"{request.method} {request.url.path}, " \
               f"status code={response.status_code}, " \
               f"took={execution_time:0.4f}s"
