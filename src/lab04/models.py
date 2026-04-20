

from src.lab03.base import Athlete
from src.lab03.models import CompetitiveAthlete as BaseCompetitiveAthlete
from src.lab03.models import RecreationalAthlete as BaseRecreationalAthlete
from src.lab04.interfaces import Printable, Comparable


class PrintableAthlete(Athlete, Printable):
    """Athlete с поддержкой интерфейса Printable."""
    
    def to_string(self) -> str:
        # Кастомное строковое представление для интерфейса
        return f"[Athlete] {self.name}: weight={self.weight}kg, record={self.personal_record}kg"


class ComparableCompetitiveAthlete(BaseCompetitiveAthlete, Comparable):
    """CompetitiveAthlete с поддержкой интерфейса Comparable (сравнение по рейтингу)."""
    
    def compare_to(self, other) -> int:
        if not isinstance(other, ComparableCompetitiveAthlete):
            raise TypeError("Can only compare with ComparableCompetitiveAthlete")
        # Сравниваем по рейтингу
        if self.rating > other.rating:
            return 1
        elif self.rating < other.rating:
            return -1
        else:
            return 0


class MultiInterfaceAthlete(BaseRecreationalAthlete, Printable, Comparable):
    """
    RecreationalAthlete, реализующий оба интерфейса: Printable и Comparable.
    Сравнение по уровню удовольствия (enjoyment_level).
    """
    
    def to_string(self) -> str:
        return f"[Recreational] {self.name} enjoys {self.favorite_activity}, level={self.enjoyment_level}"
    
    def compare_to(self, other) -> int:
        if not isinstance(other, MultiInterfaceAthlete):
            raise TypeError("Can only compare with MultiInterfaceAthlete")
        if self.enjoyment_level > other.enjoyment_level:
            return 1
        elif self.enjoyment_level < other.enjoyment_level:
            return -1
        else:
            return 0