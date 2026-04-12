"""
base.py для ЛР-3.
Базовый класс Athlete – наследник Athlete из ЛР-1.
Добавляет метод perform_action для полиморфизма.
Все остальные атрибуты и методы наследуются без изменений.
"""
import os 
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.lab01.model import Athlete as BaseAthlete


class Athlete(BaseAthlete):
    """
    Расширенный базовый класс для ЛР-3.
    Использует валидацию и всю логику из ЛР-1.
    Добавляет метод perform_action, который будет переопределён в дочерних классах.
    """

    def perform_action(self) -> str:
        """Общий интерфейс для полиморфного поведения."""
        return f"{self.name} проводит обычную тренировку."
