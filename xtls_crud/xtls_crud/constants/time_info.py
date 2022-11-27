from enum import Enum

from pydantic import BaseModel
from pydantic import root_validator


class Time(BaseModel):
    name: str
    symbol: str
    seconds: int

    @root_validator()
    def upper_case_name(cls, values):
        values['name'] = values['name'].upper()
        return values

    @root_validator()
    def upper_case_symbol(cls, values):
        values['symbol'] = values['symbol'].upper()
        return values

    @root_validator()
    def positive_seconds(cls, values):
        if values['seconds'] < 0:
            raise ValueError('seconds must be positive')
        return values

    def __str__(self):
        return f'{self.name} ({self.symbol})'

    def __repr__(self):
        return f'{self.name} ({self.symbol})'

    def __eq__(self, other):
        if isinstance(other, Time):
            return self.seconds == other.seconds
        if isinstance(other, int) or isinstance(other, float):
            return self.seconds == other
        if isinstance(other, str):
            return self.symbol == other

        raise TypeError(f'Cannot compare {type(self)} with {type(other)}')

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Time):
            return self.seconds < other.seconds
        if isinstance(other, int) or isinstance(other, float):
            return self.seconds < other
        if isinstance(other, str):
            raise TypeError(f'Cannot compare {type(self)} with {type(other)}')

        raise TypeError(f'Cannot compare {type(self)} with {type(other)}')

    def __le__(self, other):
        if isinstance(other, Time):
            return self.seconds <= other.seconds
        if isinstance(other, int) or isinstance(other, float):
            return self.seconds <= other

        raise TypeError(f'Cannot compare {type(self)} with {type(other)}')

    def __gt__(self, other):
        if isinstance(other, Time):
            return self.seconds > other.seconds
        if isinstance(other, int) or isinstance(other, float):
            return self.seconds > other

        raise TypeError(f'Cannot compare {type(self)} with {type(other)}')

    def __ge__(self, other):
        if isinstance(other, Time):
            return self.seconds >= other.seconds
        if isinstance(other, int) or isinstance(other, float):
            return self.seconds >= other

        raise TypeError(f'Cannot compare {type(self)} with {type(other)}')

    def __add__(self, other):
        if isinstance(other, Time):
            return self.seconds + other.seconds
        if isinstance(other, int) or isinstance(other, float):
            return self.seconds + other

        raise TypeError(f'Cannot add {type(self)} with {type(other)}')

    def __sub__(self, other):
        if isinstance(other, Time):
            return self.seconds - other.seconds
        if isinstance(other, int) or isinstance(other, float):
            return self.seconds - other

        raise TypeError(f'Cannot subtract {type(self)} with {type(other)}')

    def __mul__(self, other):
        if isinstance(other, Time):
            return self.seconds * other.seconds
        if isinstance(other, int) or isinstance(other, float):
            return self.seconds * other

        raise TypeError(f'Cannot multiply {type(self)} with {type(other)}')

    def __truediv__(self, other):
        if isinstance(other, Time):
            return self.seconds / other.seconds
        if isinstance(other, int) or isinstance(other, float):
            return self.seconds / other

        raise TypeError(f'Cannot divide {type(self)} with {type(other)}')

    def __floordiv__(self, other):
        if isinstance(other, Time):
            return self.seconds // other.seconds
        if isinstance(other, int) or isinstance(other, float):
            return self.seconds // other

        raise TypeError(f'Cannot divide {type(self)} with {type(other)}')

    def __mod__(self, other):
        if isinstance(other, Time):
            return self.seconds % other.seconds
        if isinstance(other, int) or isinstance(other, float):
            return self.seconds % other

        raise TypeError(f'Cannot mod {type(self)} with {type(other)}')

    def __divmod__(self, other):
        if isinstance(other, Time):
            return divmod(self.seconds, other.seconds)
        if isinstance(other, int) or isinstance(other, float):
            return divmod(self.seconds, other)

        raise TypeError(f'Cannot mod {type(self)} with {type(other)}')

    def __pow__(self, other):
        if isinstance(other, Time):
            return self.seconds ** other.seconds
        if isinstance(other, int) or isinstance(other, float):
            return self.seconds ** other

        raise TypeError(f'Cannot mod {type(self)} with {type(other)}')

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __rfloordiv__(self, other):
        return self.__floordiv__(other)

    def __rmod__(self, other):
        return self.__mod__(other)

    def __rdivmod__(self, other):
        return self.__divmod__(other)

    def __rpow__(self, other):
        return self.__pow__(other)

    def __iadd__(self, other):
        if isinstance(other, Time):
            self.seconds += other.seconds
        if isinstance(other, int) or isinstance(other, float):
            self.seconds += other

        raise TypeError(f'Cannot add {type(self)} with {type(other)}')

    def __isub__(self, other):
        if isinstance(other, Time):
            self.seconds -= other.seconds
        if isinstance(other, int) or isinstance(other, float):
            self.seconds -= other

        raise TypeError(f'Cannot subtract {type(self)} with {type(other)}')

    def __imul__(self, other):
        if isinstance(other, Time):
            self.seconds *= other.seconds
        if isinstance(other, int) or isinstance(other, float):
            self.seconds *= other

        raise TypeError(f'Cannot multiply {type(self)} with {type(other)}')

    def __itruediv__(self, other):
        if isinstance(other, Time):
            self.seconds /= other.seconds
        if isinstance(other, int) or isinstance(other, float):
            self.seconds /= other

        raise TypeError(f'Cannot divide {type(self)} with {type(other)}')


SECOND = Time(name='second', symbol='s', seconds=1)
MINUTE = Time(name='minute', symbol='m', seconds=60)
HOUR = Time(name='hour', symbol='h', seconds=3600)
DAY = Time(name='day', symbol='d', seconds=86400)
WEEK = Time(name='week', symbol='w', seconds=604800)
MONTH = Time(name='month', symbol='mo', seconds=2629746)
YEAR = Time(name='year', symbol='y', seconds=31556952)


class TimeUnit(Enum):
    SECOND = SECOND
    MINUTE = MINUTE
    HOUR = HOUR
    DAY = DAY
    WEEK = WEEK
    MONTH = MONTH
    YEAR = YEAR

    @property
    def name(self) -> str:
        return self.value.name

    @property
    def symbol(self) -> str:
        return self.value.symbol

    @property
    def seconds(self) -> int:
        return self.value.seconds

    @classmethod
    def all_names(cls) -> list[str]:
        return [unit.name for unit in cls]

    @classmethod
    def all_symbols(cls) -> list[str]:
        return [unit.symbol for unit in cls]

    @classmethod
    def map_symbols_by_name(cls) -> dict[str, str]:
        _ = {}
        for name, symbol in zip(cls.all_names(), cls.all_symbols()):
            _[name] = symbol
        return _

    @classmethod
    def map_names_by_symbol(cls) -> dict[str, str]:
        _ = {}
        for name, symbol in zip(cls.all_names(), cls.all_symbols()):
            _[symbol] = name
        return _
