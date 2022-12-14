"""
## Time Constants, Types and Enums for xtls_crud

This module contains constants, types and enums for byte sizes.

Like: 1d = 1 day | 1w = 1 week | 1mo = 1 month | 1y = 1 year
"""

from enum import Enum

from pydantic import BaseModel
from pydantic import root_validator


class Time(BaseModel):
    """
    Time Model
    """

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
        return f"Time('{self.name}', '{self.symbol}', {self.seconds})"

    def __repr__(self):
        return f"Time('{self.name}', '{self.symbol}', {self.seconds})"

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
    """
    Enum for time units
    """

    SECOND = SECOND
    MINUTE = MINUTE
    HOUR = HOUR
    DAY = DAY
    WEEK = WEEK
    MONTH = MONTH
    YEAR = YEAR

    @property
    def name(self) -> str:
        """
        Get the name of the time unit

        Returns:
            str: The name of the time unit
        """

        return self.value.name

    @property
    def symbol(self) -> str:
        """
        Get the symbol of the time unit

        Returns:
            str: The symbol of the time unit
        """

        return self.value.symbol

    @property
    def seconds(self) -> int:
        """
        Get the number of seconds in the time unit

        Returns:
            int: The number of seconds in the time unit
        """

        return self.value.seconds

    @classmethod
    def all_names(cls) -> list[str]:
        """
        Get all the names of the time units

        Returns:
            list[str]: All the names of the time units
        """

        return [unit.name for unit in cls]

    @classmethod
    def all_symbols(cls) -> list[str]:
        """
        Get all the symbols of the time units

        Returns:
            list[str]: All the symbols of the time units
        """

        return [unit.symbol for unit in cls]

    @classmethod
    def all_seconds(cls) -> list[int]:
        """
        Get all the number of seconds in the time units

        Returns:
            list[int]: All the number of seconds in the time units
        """

        return [unit.seconds for unit in cls]

    @classmethod
    def map_symbols_by_name(cls) -> dict[str, str]:
        """
        Map the symbols of the time units by their names

        Returns:
            dict[str, str]: A dictionary mapping the symbols of the time units by their names
        """

        return {name: symbol for name, symbol in zip(cls.all_names(), cls.all_symbols())}

    @classmethod
    def map_names_by_symbol(cls) -> dict[str, str]:
        """
        Map the names of the time units by their symbols

        Returns:
            dict[str, str]: A dictionary mapping the names of the time units by their symbols
        """

        return {symbol: name for name, symbol in zip(cls.all_names(), cls.all_symbols())}

    @classmethod
    def map_seconds_by_name(cls) -> dict[str, int]:
        """
        Map the number of seconds in the time units by their names

        Returns:
            dict[str, int]: A dictionary mapping the number of seconds in the time units by their names
        """

        return {name: seconds for name, seconds in zip(cls.all_names(), cls.all_seconds())}

    @classmethod
    def map_seconds_by_symbol(cls) -> dict[str, int]:
        """
        Map the number of seconds in the time units by their symbols

        Returns:
            dict[str, int]: A dictionary mapping the number of seconds in the time units by their symbols
        """

        return {symbol: seconds for symbol, seconds in zip(cls.all_symbols(), cls.all_seconds())}


def from_string(string: str) -> Time:
    """
    Create a time from a string

    Args:
        string (str): The string to create the time from

    Returns:
        Time: The time

    Raises:
        ValueError: If the string is not a valid time
        TypeError: If the string is not a string
        KeyError: If the string is not a valid time unit

    Examples:
        >>> from_string('1s')
        Time('S', 'SECOND', 1)
    """

    if not isinstance(string, str):
        raise TypeError(f'Expected str, got {type(string)}')

    if not string:
        raise ValueError('Cannot convert empty string to Time')

    string = string.upper()

    digits = int(''.join(filter(str.isdigit, string)))
    unit = ''.join(filter(str.isalpha, string))

    if not digits:
        raise ValueError('Cannot convert string to Time')

    if not unit:
        raise ValueError('Cannot convert string to Time')

    if (unit not in TimeUnit.all_symbols()) and (unit not in TimeUnit.all_names()):
        raise ValueError(f'Cannot convert string to Time: {unit=} | {TimeUnit.all_symbols()} | {TimeUnit.all_names()}')

    symbol = TimeUnit.map_names_by_symbol()[unit]
    seconds = TimeUnit.map_seconds_by_symbol()[unit]

    return Time(name=unit, symbol=symbol, seconds=seconds * digits)
