import typing as t
from typer import Typer, Option

from ... import (
    web_main
)
from ...web.backend.app.core.settings import settings


app = Typer(
    name='web',
    help='XTLS_CRUD Web Commands',
)


@app.command()
def serve(
        host: t.Optional[str] = Option(
            settings.SERVER_HOST, help='Server host', envvar='SERVER_HOST', metavar='HOST'),
        port: t.Optional[int] = Option(
            settings.SERVER_PORT, help='Server port', envvar='SERVER_PORT', metavar='PORT'),
        reload: t.Optional[bool] = Option(
            False, help='Reload', envvar='RELOAD', metavar='RELOAD'),
        log_level: t.Optional[str] = Option(
            None, help='Log level', envvar='LOG_LEVEL', metavar='LOG_LEVEL'),
        from_shell: t.Optional[bool] = Option(
            False, help='From shell', metavar='FROM_SHELL'),
):
    if from_shell:
        import subprocess

        # run uvicorn xtls_crud:web_app --reload --port=5001 --host=0.0.0.0:
        text = "uvicorn xtls_crud:web_app"
        if reload:
            text += " --reload"
        if port:
            text += f" --port={port}"
        if host:
            text += f" --host={host}"
        if log_level:
            text += f" --log-level={log_level}"

        subprocess.Popen(text, shell=True)

    else:
        web_main(
            host=host,
            port=port,
            reload=reload,
            log_level=log_level,
        )
