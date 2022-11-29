import time

import uvicorn

from fastapi import FastAPI, Request
from fastapi.openapi.utils import get_openapi
from starlette.concurrency import iterate_in_threadpool
from starlette.middleware.cors import CORSMiddleware

from .api.api_v1.api import api_router
from .core.settings import settings
from .open_api.code_samples.samples import inbound__get, builders__post


app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    # custom settings
    openapi_schema = get_openapi(
        title="Xtls Crud",
        version="0.1.0",
        description="Xtls Crud",
        routes=app.routes,
    )
    # setting new logo to docs

    openapi_schema["paths"][inbound__get.path][
        inbound__get.method]["x-codeSamples"] = inbound__get.samples_dict_list
    openapi_schema["paths"][builders__post.path][
        builders__post.method]["x-codeSamples"] = builders__post.samples_dict_list

    app.openapi_schema = openapi_schema

    return app.openapi_schema


app.openapi = custom_openapi

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
