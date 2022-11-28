import time

import uvicorn

from fastapi import FastAPI, Request
from starlette.concurrency import iterate_in_threadpool
from starlette.middleware.cors import CORSMiddleware

from .api.api_v1.api import api_router
from .core.settings import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next, *args, **kwargs):
    start_time = time.time()
    _response = await call_next(request)
    process_time = time.time() - start_time
    _response.headers["X-Process-Time"] = str(process_time)
    return _response


@app.middleware("http")
async def add_cors_headers(request: Request, call_next, *args, **kwargs):
    _response = await call_next(request)
    _response.headers["Access-Control-Allow-Origin"] = "*"
    return _response


@app.middleware("http")
async def add_content_length(request: Request, call_next, *args, **kwargs):
    _response = await call_next(request)
    try:
        response_body = [chunk async for chunk in _response.body_iterator]
        _response.body_iterator = iterate_in_threadpool(iter(response_body))
        resp_body = response_body[0].decode()
    except Exception as e:
        print(e)
        resp_body = ''
    _response.headers["Content-Length"] = str(len(resp_body))
    return _response


def main(host: str = None, port: int = None, reload: bool = False, log_level: str = None):
    host = host or settings.SERVER_HOST
    port = port or settings.SERVER_PORT
    reload = reload
    log_level = log_level
    uvicorn.run("xtls_crud:web_app", host=host, port=port, reload=reload, log_level=log_level)


if __name__ == "__main__":
    main()
