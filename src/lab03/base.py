
import os 
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.lab01.model import Athlete as BaseAthlete


class Athlete(BaseAthlete):
   

    def perform_action(self) -> str:
        return f"{self.name} проводит обычную тренировку."
