

from typing import List, Optional, Callable, Any
from src.lab01.model import Athlete
from src.lab03.models import CompetitiveAthlete, RecreationalAthlete
from src.lab06.container import TypedCollection
import src.lab05.strategies as strat
from src.lab07.exceptions import DuplicateItemError, ItemNotFoundException
import src.lab07.storage as storage

class App:

    
    def __init__(self, data_file: str = "athletes.json") -> None:
        self.data_file = data_file
        self.collection: TypedCollection[Athlete] = TypedCollection[Athlete]()
        self._load_data()
    
    def _load_data(self) -> None:

        athletes = storage.load(self.data_file)
        for a in athletes:
            try:
                self.collection.add(a)
            except ValueError:

                pass
    
    def _save_data(self) -> None:

        storage.save(self.collection.get_all(), self.data_file)
    
    def add_athlete(self, athlete: Athlete) -> None:
        try:
            self.collection.add(athlete)
            self._save_data()
        except ValueError as e:
            raise DuplicateItemError(str(e))
    
    def remove_athlete(self, name: str) -> None:
        found = self.collection.find(lambda a: a.name == name)
        if not found:
            raise ItemNotFoundException(f"Спортсмен '{name}' не найден")
        self.collection.remove(found)
        self._save_data()
    
    def find_by_name(self, name: str) -> Optional[Athlete]:
        return self.collection.find(lambda a: a.name == name)
    
    def filter_athletes(self, predicate: Callable[[Athlete], bool]) -> List[Athlete]:
        return self.collection.filter(predicate)
    
    def sort_athletes(self, key_func: Callable[[Athlete], Any], reverse: bool = False) -> None:
        self.collection.sort(key=key_func, reverse=reverse)
        self._save_data()
    
    def get_all(self) -> List[Athlete]:
        return self.collection.get_all()
    
    def apply_to_all(self, func: Callable[[Athlete], Any]) -> List[Any]:

        return self.collection.map(func)
    
    def exit(self) -> None:
        self._save_data()