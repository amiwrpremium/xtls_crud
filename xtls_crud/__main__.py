try:
    from .commands.main import app as main_app
except (ModuleNotFoundError, ImportError):
    import sys
    from pathlib import Path

    for path in Path(__file__).absolute().parents:
        sys.path.append(str(path.parent))

    from xtls_crud.commands.main import app as main_app  # noqa


if __name__ == '__main__':
    main_app()
