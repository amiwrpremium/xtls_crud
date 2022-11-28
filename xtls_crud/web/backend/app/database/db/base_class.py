from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically

    @declared_attr
    def __tablename__(cls) -> str:  # noqa
        return cls.__name__.lower()

    def __repr__(self) -> str:
        _ = f'{self.__class__.__name__}('
        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                _ += f'{key}={value}, '
        _ = _.rstrip(', ')
        _ += ')'
        return _

    def __str__(self) -> str:
        return self.__repr__()
