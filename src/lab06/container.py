# src/lab06/container.py
from typing import TypeVar, Generic, Callable, Optional, List, Iterator, Any, Protocol

# ---------- Протоколы (оценка 5) ----------
class Displayable(Protocol):
    def display(self) -> str:
        ...

class Scorable(Protocol):
    def score(self) -> float:
        ...

# ---------- Типовые переменные ----------
T = TypeVar('T')
R = TypeVar('R')
D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)

class TypedCollection(Generic[T]):
    """Generic-контейнер, хранящий элементы типа T."""

    def __init__(self) -> None:
        self._items: List[T] = []

    # ----- Базовые методы (как в AthleteCollection) -----
    def add(self, item: T) -> None:
        """Добавляет элемент в коллекцию."""
        if item in self._items:
            raise ValueError("Duplicate item")
        self._items.append(item)

    def remove(self, item: T) -> None:
        """Удаляет элемент из коллекции."""
        if item not in self._items:
            raise ValueError("Item not found")
        self._items.remove(item)

    def get_all(self) -> List[T]:
        """Возвращает копию списка элементов."""
        return self._items.copy()

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)

    def __getitem__(self, index: int) -> T:
        if not isinstance(index, int):
            raise TypeError("Index must be integer")
        n = len(self._items)
        if index < 0:
            index = n + index
        if index < 0 or index >= n:
            raise IndexError("Index out of range")
        return self._items[index]

    def remove_at(self, index: int) -> None:
        if not isinstance(index, int):
            raise TypeError("Index must be integer")
        n = len(self._items)
        if index < 0:
            index = n + index
        if index < 0 or index >= n:
            raise IndexError("Index out of range")
        del self._items[index]

    def sort(self, key: Optional[Callable[[T], Any]] = None, reverse: bool = False) -> None:
        """Сортирует коллекцию на месте."""
        self._items.sort(key=key, reverse=reverse)

    # ----- Методы оценки 4 -----
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """Возвращает первый элемент, удовлетворяющий предикату, или None."""
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        """Возвращает список всех элементов, удовлетворяющих предикату."""
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> List[R]:
        """Применяет функцию преобразования к каждому элементу и возвращает список результатов."""
        return [transform(item) for item in self._items]

    # ----- Для удобства -----
    def __str__(self) -> str:
        return f"TypedCollection[{len(self)} items]"