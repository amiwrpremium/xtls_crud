"""
ByteSize Constants, Types and Enums for xtls_crud

This module contains constants, types and enums for byte sizes.
Like: 1GB = 1 Gigabyte | 1TB = 1 Terabyte | 1PB = 1 Petabyte | 1EB = 1 Exabyte
"""

from enum import Enum
from pydantic import BaseModel
from pydantic import root_validator


class Size(BaseModel):
    """
    Size Model
    """

    name: str
    symbol: str
    bytes: int

    @root_validator()
    def upper_case_name(cls, values):
        """
        Upper case the name

        :param values: values from the model
        :type values: dict

        :return: values
        :rtype: dict
        """

        values['name'] = values['name'].upper()
        return values

    @root_validator()
    def upper_case_symbol(cls, values):
        """
        Upper case the symbol

        :param values: values from the model
        :type values: dict

        :return: values
        :rtype: dict
        """

        values['symbol'] = values['symbol'].upper()
        return values

    @root_validator()
    def positive_bytes(cls, values):
        """
        Validate that bytes is positive

        :param values: values from the model
        :type values: dict

        :return: values
        :rtype: dict
        """

        if values['bytes'] < 0:
            raise ValueError('bytes must be positive')
        return values

    def __str__(self):
        return f'{self.name} ({self.symbol})'

    def __repr__(self):
        return f'{self.name} ({self.symbol})'

    def __eq__(self, other):
        if isinstance(other, Size):
            return self.bytes == other.bytes
        if isinstance(other, int) or isinstance(other, float):
            return self.bytes == other
        if isinstance(other, str):
            return self.symbol == other

        raise TypeError(f'Cannot compare {type(self)} with {type(other)}')

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Size):
            return self.bytes < other.bytes
        if isinstance(other, int) or isinstance(other, float):
            return self.bytes < other
        if isinstance(other, str):
            raise TypeError(f'Cannot compare {type(self)} with {type(other)}')

        raise TypeError(f'Cannot compare {type(self)} with {type(other)}')

    def __le__(self, other):
        if isinstance(other, Size):
            return self.bytes <= other.bytes
        if isinstance(other, int) or isinstance(other, float):
            return self.bytes <= other

        raise TypeError(f'Cannot compare {type(self)} with {type(other)}')

    def __gt__(self, other):
        if isinstance(other, Size):
            return self.bytes > other.bytes
        if isinstance(other, int) or isinstance(other, float):
            return self.bytes > other

        raise TypeError(f'Cannot compare {type(self)} with {type(other)}')

    def __ge__(self, other):
        if isinstance(other, Size):
            return self.bytes >= other.bytes
        if isinstance(other, int) or isinstance(other, float):
            return self.bytes >= other

        raise TypeError(f'Cannot compare {type(self)} with {type(other)}')

    def __add__(self, other):
        if isinstance(other, Size):
            return self.bytes + other.bytes
        if isinstance(other, int) or isinstance(other, float):
            return self.bytes + other

        raise TypeError(f'Cannot add {type(self)} with {type(other)}')

    def __sub__(self, other):
        if isinstance(other, Size):
            return self.bytes - other.bytes
        if isinstance(other, int) or isinstance(other, float):
            return self.bytes - other

        raise TypeError(f'Cannot subtract {type(self)} with {type(other)}')

    def __mul__(self, other):
        if isinstance(other, Size):
            return self.bytes * other.bytes
        if isinstance(other, int) or isinstance(other, float):
            return self.bytes * other

        raise TypeError(f'Cannot multiply {type(self)} with {type(other)}')

    def __truediv__(self, other):
        if isinstance(other, Size):
            return self.bytes / other.bytes
        if isinstance(other, int) or isinstance(other, float):
            return self.bytes / other

        raise TypeError(f'Cannot divide {type(self)} with {type(other)}')

    def __floordiv__(self, other):
        if isinstance(other, Size):
            return self.bytes // other.bytes
        if isinstance(other, int) or isinstance(other, float):
            return self.bytes // other

        raise TypeError(f'Cannot divide {type(self)} with {type(other)}')

    def __mod__(self, other):
        if isinstance(other, Size):
            return self.bytes % other.bytes
        if isinstance(other, int) or isinstance(other, float):
            return self.bytes % other

        raise TypeError(f'Cannot mod {type(self)} with {type(other)}')

    def __divmod__(self, other):
        if isinstance(other, Size):
            return divmod(self.bytes, other.bytes)
        if isinstance(other, int) or isinstance(other, float):
            return divmod(self.bytes, other)

        raise TypeError(f'Cannot mod {type(self)} with {type(other)}')

    def __pow__(self, other):
        if isinstance(other, Size):
            return self.bytes ** other.bytes
        if isinstance(other, int) or isinstance(other, float):
            return self.bytes ** other

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
        if isinstance(other, Size):
            self.bytes += other.bytes
        if isinstance(other, int) or isinstance(other, float):
            self.bytes += other

        raise TypeError(f'Cannot add {type(self)} with {type(other)}')

    def __isub__(self, other):
        if isinstance(other, Size):
            self.bytes -= other.bytes
        if isinstance(other, int) or isinstance(other, float):
            self.bytes -= other

        raise TypeError(f'Cannot subtract {type(self)} with {type(other)}')

    def __imul__(self, other):
        if isinstance(other, Size):
            self.bytes *= other.bytes
        if isinstance(other, int) or isinstance(other, float):
            self.bytes *= other

        raise TypeError(f'Cannot multiply {type(self)} with {type(other)}')

    def __itruediv__(self, other):
        if isinstance(other, Size):
            self.bytes /= other.bytes
        if isinstance(other, int) or isinstance(other, float):
            self.bytes /= other

        raise TypeError(f'Cannot divide {type(self)} with {type(other)}')


BYTE = Size(name='byte', symbol='B', bytes=1)
KILOBYTE = Size(name='kilobyte', symbol='KB', bytes=1024)
MEGABYTE = Size(name='megabyte', symbol='MB', bytes=1048576)
GIGABYTE = Size(name='gigabyte', symbol='GB', bytes=1073741824)
TERABYTE = Size(name='terabyte', symbol='TB', bytes=1099511627776)
PETABYTE = Size(name='petabyte', symbol='PB', bytes=1125899906842624)
EXABYTE = Size(name='exabyte', symbol='EB', bytes=1152921504606846976)


class SizeUnit(Enum):
    """
    Enum for size units
    """

    BYTE = BYTE
    KILOBYTE = KILOBYTE
    MEGABYTE = MEGABYTE
    GIGABYTE = GIGABYTE
    TERABYTE = TERABYTE
    PETABYTE = PETABYTE
    EXABYTE = EXABYTE

    @property
    def name(self) -> str:
        """
        Get the name of the unit

        :return: The name of the unit
        :rtype: str
        """

        return self.value.name

    @property
    def symbol(self) -> str:
        """
        Get the symbol of the unit

        :return: The symbol of the unit
        :rtype: str
        """

        return self.value.symbol

    @property
    def bytes(self) -> int:
        """
        Get the number of bytes in the unit

        :return: The number of bytes in the unit
        :rtype: int
        """

        return self.value.bytes

    @classmethod
    def all_names(cls) -> list[str]:
        """
        Get all the names of the units

        :return: All the names of the units
        :rtype: list[str]
        """

        return [unit.name for unit in cls]

    @classmethod
    def all_symbols(cls) -> list[str]:
        """
        Get all the symbols of the units

        :return: All the symbols of the units
        :rtype: list[str]
        """

        return [unit.symbol for unit in cls]

    @classmethod
    def all_bytes(cls) -> list[int]:
        """
        Get all the number of bytes in the units

        :return: All the number of bytes in the units
        :rtype: list[int]
        """

        return [unit.bytes for unit in cls]

    @classmethod
    def map_symbols_by_name(cls) -> dict[str, str]:
        """
        Map the symbols of the units by their names

        :return: A dictionary mapping the symbols of the units by their names
        :rtype: dict[str, str]
        """

        return {name: symbol for name, symbol in zip(cls.all_names(), cls.all_symbols())}

    @classmethod
    def map_names_by_symbol(cls) -> dict[str, str]:
        """
        Map the names of the units by their symbols

        :return: A dictionary mapping the names of the units by their symbols
        :rtype: dict[str, str]
        """

        return {symbol: name for name, symbol in zip(cls.all_names(), cls.all_symbols())}

    @classmethod
    def map_bytes_by_name(cls) -> dict[str, int]:
        """
        Map the number of bytes in the units by their names

        :return: A dictionary mapping the number of bytes in the units by their names
        :rtype: dict[str, int]
        """

        return {name: bytes for name, bytes in zip(cls.all_names(), cls.all_bytes())}  # noqa

    @classmethod
    def map_bytes_by_symbol(cls) -> dict[str, int]:
        """
        Map the number of bytes in the units by their symbols

        :return: A dictionary mapping the number of bytes in the units by their symbols
        :rtype: dict[str, int]
        """

        return {symbol: bytes for symbol, bytes in zip(cls.all_symbols(), cls.all_bytes())}  # noqa


def from_string(string: str) -> Size:
    """
    Create a size from a string

    :param string: The string to create the size from
    :type string: str

    :return: The size (e.g. 100 MB)
    :rtype: Size

    :raises ValueError: If the string is not a valid size
    """

    if not isinstance(string, str):
        raise TypeError(f'Expected str, got {type(string)}')

    if not string:
        raise ValueError('Cannot convert empty string to Size')

    string = string.upper()

    digits = int(''.join(filter(str.isdigit, string)))
    unit = ''.join(filter(str.isalpha, string))

    if not digits:
        raise ValueError('Cannot convert string to Size')

    if not unit:
        raise ValueError('Cannot convert string to Size')

    if (unit not in SizeUnit.all_symbols()) and (unit not in SizeUnit.all_names()):
        raise ValueError(f'Cannot convert string to Size: {unit=} | {SizeUnit.all_symbols()} | {SizeUnit.all_names()}')

    symbol = SizeUnit.map_names_by_symbol()[unit]
    bytes = SizeUnit.map_bytes_by_symbol()[unit]  # noqa

    return Size(name=unit, symbol=symbol, bytes=bytes * digits)
