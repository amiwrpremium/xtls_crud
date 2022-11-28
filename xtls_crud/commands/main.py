from typer import Typer

from .web.main import app as cachers_app

app = Typer(
    name='XTLS_CRUD',
    help='XTLS_CRUD Commands',
)

app.add_typer(cachers_app, name='web')

if __name__ == '__main__':
    app()
