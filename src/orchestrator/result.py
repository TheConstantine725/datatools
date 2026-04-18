from dataclasses import dataclass
from typing import TypeVar, Generic


T = TypeVar("T")


class Result(Generic[T]):
    def is_success(self):
        if isinstance(self, Success):
            return True

    def is_failure(self):
        if isinstance(self, Failure):
            return True

    def unwrap(self) -> T | None:
        if self.is_success():
            return self.value
        raise ValueError(self.error)

    def unwrap_or(self, default: T) -> T:
        if self.is_success():
            return self.value
        return default


@dataclass
class Success(Result[T]):
    value: T


@dataclass
class Failure(Result):
    error: str
