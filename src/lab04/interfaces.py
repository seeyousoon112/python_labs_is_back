

from abc import ABC, abstractmethod


class Printable(ABC):
    """Интерфейс для объектов, которые можно преобразовать в строку (особое представление)."""
    
    @abstractmethod
    def to_string(self) -> str:
        """Вернуть строковое представление объекта (может отличаться от __str__)."""
        pass


class Comparable(ABC):
    """Интерфейс для объектов, которые можно сравнивать между собой."""
    
    @abstractmethod
    def compare_to(self, other) -> int:
        """
        Сравнить текущий объект с другим.
        Возвращает:
          - отрицательное число, если self < other
          - 0, если self == other
          - положительное число, если self > other
        """
        pass