from abc import ABC, abstractmethod


class Builder(ABC):
    @abstractmethod
    def build(self):
        ...

    def check(self):
        for k, v in self.__dict__.items():
            if v is None:
                raise ValueError(f"{k} is None")
