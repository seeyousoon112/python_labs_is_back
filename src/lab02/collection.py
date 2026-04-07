

import sys
import os

# Добавляем корневую директорию проекта в путь поиска модулей
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

"""
Контейнерный класс AthleteCollection для хранения объектов Athlete.
Реализует требования ЛР-2
"""

from src.lab01.model import Athlete


class AthleteCollection:
    """Коллекция спортсменов с возможностью добавления, удаления, поиска, сортировки и фильтрации."""

    def __init__(self):
        """Инициализация пустой коллекции."""
        self._items = []

    # ------------------- Основные методы (оценка 3) -------------------
    def add(self, athlete):
        """
        Добавить спортсмена в коллекцию.
        Проверяет тип и отсутствие дубликата (по __eq__ Athlete).
        """
        if not isinstance(athlete, Athlete):
            raise TypeError(f"Only Athlete objects can be added, got {type(athlete).__name__}")
        if athlete in self._items:
            raise ValueError(f"Athlete {athlete.name} already exists in the collection (duplicate by name, weight, height, record).")
        self._items.append(athlete)

    def remove(self, athlete):
        """Удалить спортсмена из коллекции."""
        if athlete not in self._items:
            raise ValueError("Athlete not found in collection")
        self._items.remove(athlete)

    def get_all(self):
        """Вернуть копию списка всех спортсменов."""
        return self._items.copy()

    # ------------------- Методы для оценки 4 -------------------
    def find_by_name(self, name):
        """Найти всех спортсменов с точным совпадением имени (регистр учитывается)."""
        return [a for a in self._items if a.name == name]

    def find_by_record(self, min_record=None, max_record=None):
        """Найти спортсменов по диапазону личного рекорда."""
        result = self._items
        if min_record is not None:
            result = [a for a in result if a.personal_record >= min_record]
        if max_record is not None:
            result = [a for a in result if a.personal_record <= max_record]
        return result

    def find_by_health_status(self, status):
        """Найти спортсменов по состоянию здоровья."""
        return [a for a in self._items if a.health_status == status]

    def find_by_training_level(self, level):
        """Найти спортсменов по уровню подготовки."""
        return [a for a in self._items if a.training_level == level]

    def find_by_active(self, active=True):
        """Найти активных или неактивных спортсменов."""
        return [a for a in self._items if a.is_active == active]

    def __len__(self):
        """Вернуть количество элементов в коллекции."""
        return len(self._items)

    def __iter__(self):
        """Итератор по коллекции."""
        return iter(self._items)

    # ------------------- Методы для оценки 5 -------------------
    def __getitem__(self, index):
        """
        Поддержка индексации (collection[i]), включая отрицательные индексы.
        collection[-1] – последний элемент.
        """
        if not isinstance(index, int):
            raise TypeError("Index must be integer")
        n = len(self._items)
        if index < 0:
            index = n + index          # преобразуем -1 в последний индекс
        if index < 0 or index >= n:
            raise IndexError("Index out of range")
        return self._items[index]

    def remove_at(self, index):
        """Удалить элемент по индексу (также с поддержкой отрицательных индексов)."""
        if not isinstance(index, int):
            raise TypeError("Index must be integer")
        n = len(self._items)
        if index < 0:
            index = n + index
        if index < 0 or index >= n:
            raise IndexError("Index out of range")
        del self._items[index]

    def sort(self, key=None, reverse=False):
        """
        Сортировка коллекции на месте.
        key – функция, возвращающая значение для сравнения (например, lambda a: a.weight).
        reverse – если True, сортировка по убыванию.
        """
        self._items.sort(key=key, reverse=reverse)

    # Фильтрующие методы, возвращающие новую коллекцию (логические операции)
    def filter_active(self):
        """Вернуть новую коллекцию только с активными спортсменами."""
        new_col = AthleteCollection()
        for a in self._items:
            if a.is_active:
                new_col.add(a)
        return new_col

    def filter_health_status(self, status):
        """Вернуть новую коллекцию спортсменов с заданным статусом здоровья."""
        new_col = AthleteCollection()
        for a in self._items:
            if a.health_status == status:
                new_col.add(a)
        return new_col

    def filter_training_level(self, level):
        """Вернуть новую коллекцию спортсменов с заданным уровнем подготовки."""
        new_col = AthleteCollection()
        for a in self._items:
            if a.training_level == level:
                new_col.add(a)
        return new_col

    def filter_min_record(self, min_record):
        """Вернуть новую коллекцию спортсменов, чей рекорд не меньше min_record."""
        new_col = AthleteCollection()
        for a in self._items:
            if a.personal_record >= min_record:
                new_col.add(a)
        return new_col

    def __str__(self):
        return f"AthleteCollection with {len(self)} items: {[a.name for a in self._items]}"