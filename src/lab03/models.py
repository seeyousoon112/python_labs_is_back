
import sys 
import os 
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.lab03.base import Athlete


class CompetitiveAthlete(Athlete):
    """Соревновательный спортсмен."""

    def __init__(self, name: str, weight: float, height: float, record: float = 0.0,
                 wins: int = 0, rating: float = 1000.0):
        super().__init__(name, weight, height, record)
        self._wins = wins
        self._rating = rating

    @property
    def wins(self):
        return self._wins

    @property
    def rating(self):
        return self._rating

    def compete(self, is_win: bool = True):
        if is_win:
            self._wins += 1
            self._rating += 50
        else:
            self._rating -= 30
            if self._rating < 0:
                self._rating = 0

    def __str__(self):
        base = super().__str__()
        return f"{base}\n  Competitive: wins={self._wins}, rating={self._rating:.1f}"

    def perform_action(self) -> str:
        return f"{self.name} тренируется к соревнованиям и участвует в турнирах."


class RecreationalAthlete(Athlete):
    """Спортсмен-любитель."""

    def __init__(self, name: str, weight: float, height: float, record: float = 0.0,
                 favorite_activity: str = "running", enjoyment_level: int = 5):
        super().__init__(name, weight, height, record)
        self._favorite_activity = favorite_activity
        self._enjoyment_level = enjoyment_level

    @property
    def favorite_activity(self):
        return self._favorite_activity

    @property
    def enjoyment_level(self):
        return self._enjoyment_level

    def have_fun(self, hours: int = 1):
        self._enjoyment_level += hours
        if self._enjoyment_level > 10:
            self._enjoyment_level = 10

    def __str__(self):
        base = super().__str__()
        return f"{base}\n  Recreational: fav={self._favorite_activity}, enjoyment={self._enjoyment_level}/10"

    def perform_action(self) -> str:
        return f"{self.name} занимается {self._favorite_activity} для удовольствия."