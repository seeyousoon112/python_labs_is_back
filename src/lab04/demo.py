"""
Демонстрация работы интерфейсов (ABC) в ЛР-4.
Использует коллекцию AthleteCollection из ЛР-2.
"""

from src.lab02.collection import AthleteCollection
from src.lab04.models import PrintableAthlete, ComparableCompetitiveAthlete, MultiInterfaceAthlete
from src.lab04.interfaces import Printable, Comparable


# ========== Универсальная функция, работающая через интерфейс (оценка 4) ==========
def print_all(items: list):
    """Принимает список объектов, реализующих Printable, и выводит их to_string()."""
    for item in items:
        if isinstance(item, Printable):
            print(item.to_string())
        else:
            print(f"{item} не поддерживает Printable")


# ========== Сценарии ==========
def demo_basic_interfaces():
    """Сценарий 1: создание объектов, вызов интерфейсных методов (оценка 3)."""
    print("=" * 60)
    print("СЦЕНАРИЙ 1: Реализация интерфейсов в разных классах")
    print("=" * 60)
    
    a1 = PrintableAthlete("Иван", 75, 180, 120)
    a2 = ComparableCompetitiveAthlete("Мария", 65, 170, 150, wins=2, rating=1250)
    a3 = MultiInterfaceAthlete("Олег", 80, 175, 90, favorite_activity="cycling", enjoyment_level=7)
    
    print(a1.to_string())          # через интерфейс Printable
    print(a2.to_string() if isinstance(a2, Printable) else "не Printable")
    # Comparable
    a4 = ComparableCompetitiveAthlete("Петр", 70, 172, 130, wins=1, rating=1100)
    print(f"Сравнение Мария и Петр по рейтингу: {a2.compare_to(a4)}")  # 1 (Мария > Петр)
    print(f"to_string от MultiInterfaceAthlete: {a3.to_string()}")
    print()


def demo_interface_as_type():
    """Сценарий 2: использование интерфейса как типа и isinstance (оценка 4)."""
    print("=" * 60)
    print("СЦЕНАРИЙ 2: Интерфейс как тип, универсальная функция, множественная реализация")
    print("=" * 60)
    
    objects = [
        PrintableAthlete("Анна", 60, 165, 80),
        MultiInterfaceAthlete("Сергей", 82, 182, 110, favorite_activity="running", enjoyment_level=9),
        ComparableCompetitiveAthlete("Дмитрий", 78, 178, 140, wins=3, rating=1320),
    ]
    
    print("Проверка isinstance (Printable):")
    for obj in objects:
        print(f"{obj.name}: {isinstance(obj, Printable)}")
    
    print("\nУниверсальная функция print_all (работает только с Printable):")
    print_all(objects)
    
    print("\nМножественная реализация интерфейсов (MultiInterfaceAthlete):")
    a = MultiInterfaceAthlete("Елена", 55, 162, 70, favorite_activity="yoga", enjoyment_level=8)
    print(f"Printable: {a.to_string()}")
    b = MultiInterfaceAthlete("Татьяна", 58, 165, 75, favorite_activity="pilates", enjoyment_level=9)
    print(f"Сравнение (enjoyment): {a.compare_to(b)}")  # -1 (8 < 9)
    print()


def demo_collection_integration():
    """Сценарий 3: интеграция с коллекцией ЛР-2, фильтрация по интерфейсу (оценка 5)."""
    print("=" * 60)
    print("СЦЕНАРИЙ 3: Коллекция AthleteCollection и фильтрация по интерфейсу")
    print("=" * 60)
    
    col = AthleteCollection()
    col.add(PrintableAthlete("Алексей", 72, 176, 105))
    col.add(ComparableCompetitiveAthlete("Владимир", 84, 184, 160, wins=4, rating=1400))
    col.add(MultiInterfaceAthlete("Наталья", 63, 168, 95, favorite_activity="swimming", enjoyment_level=6))
    col.add(PrintableAthlete("Ирина", 68, 170, 100))
    
    print(f"Всего в коллекции: {len(col)}")
    for a in col:
        print(a)
    
    # Фильтрация по интерфейсу Printable
    printable_items = [item for item in col if isinstance(item, Printable)]
    print(f"\nОбъекты, реализующие Printable ({len(printable_items)}):")
    for item in printable_items:
        print(f"  {item.to_string()}")
    
    # Фильтрация по интерфейсу Comparable
    comparable_items = [item for item in col if isinstance(item, Comparable)]
    print(f"\nОбъекты, реализующие Comparable ({len(comparable_items)}):")
    for item in comparable_items:
        # Вызов compare_to требует совместимых типов, просто покажем их имена
        print(f"  {item.name} (реализует Comparable)")
    
    # Демонстрация полиморфизма через интерфейс (без условий)
    print("\nПолиморфизм: вызов to_string() для всех Printable в коллекции:")
    for item in col:
        if isinstance(item, Printable):
            print(f"  {item.to_string()}")
    print()


def demo_sorting_via_interface():
    """Сценарий 4: сортировка через интерфейс Comparable (оценка 5)."""
    print("=" * 60)
    print("СЦЕНАРИЙ 4: Сортировка списка объектов через интерфейс Comparable")
    print("=" * 60)
    
    athletes = [
        ComparableCompetitiveAthlete("Борис", 80, 180, 140, wins=2, rating=1150),
        ComparableCompetitiveAthlete("Антон", 75, 175, 130, wins=1, rating=1080),
        ComparableCompetitiveAthlete("Глеб", 85, 185, 150, wins=3, rating=1220),
    ]
    
    # Сортировка пузырьком с использованием compare_to
    n = len(athletes)
    for i in range(n):
        for j in range(0, n-i-1):
            if athletes[j].compare_to(athletes[j+1]) > 0:
                athletes[j], athletes[j+1] = athletes[j+1], athletes[j]
    
    print("Спортсмены, отсортированные по рейтингу (через compare_to):")
    for a in athletes:
        print(f"  {a.name}: рейтинг {a.rating}")
    print()


if __name__ == "__main__":
    demo_basic_interfaces()
    demo_interface_as_type()
    demo_collection_integration()
    demo_sorting_via_interface()