
from src.lab02.collection import AthleteCollection
from src.lab01.model import Athlete


class FunctionalAthleteCollection(AthleteCollection):

    def sort_by(self, key_func, reverse=False):

        self._items.sort(key=key_func, reverse=reverse)
        return self

    def filter_by(self, predicate):

        new_collection = FunctionalAthleteCollection()
        for item in self._items:
            if predicate(item):
                new_collection.add(item)
        return new_collection

    def apply(self, func):

        new_collection = FunctionalAthleteCollection()
        for item in self._items:
            result = func(item)
            if isinstance(result, Athlete):
                new_collection.add(result)
        return new_collection

    def __str__(self):
        return f"FunctionalAthleteCollection({[a.name for a in self._items]})"