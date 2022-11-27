from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
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
