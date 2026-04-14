
import sys 
import os 
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.lab03.base import Athlete
from src.lab03.models import CompetitiveAthlete, RecreationalAthlete
from src.lab02.collection import AthleteCollection   # коллекция из ЛР-2


def demo_inheritance():
    print("=" * 60)
    print("СЦЕНАРИЙ 1: Создание объектов производных классов")
    print("=" * 60)

    a1 = Athlete("Обычный", 70, 175, 100)
    a2 = CompetitiveAthlete("Чемпион", 85, 185, 200, wins=5, rating=1200)
    a3 = RecreationalAthlete("Любитель", 65, 170, 80, favorite_activity="swimming", enjoyment_level=7)

    print(a1)
    print(a2)
    print(a3)

    print("\n--- Использование новых методов ---")
    a2.compete(is_win=True)
    print(f"После победы: {a2.name}, wins={a2.wins}, rating={a2.rating}")
    a3.have_fun(hours=2)
    print(f"После отдыха: {a3.name}, enjoyment={a3.enjoyment_level}")
    print()


def demo_polymorphism():
    print("=" * 60)
    print("СЦЕНАРИЙ 2: Полиморфизм – общий интерфейс с разной реализацией")
    print("=" * 60)

    athletes = [
        Athlete("Просто", 70, 175),
        CompetitiveAthlete("Профи", 80, 180, wins=3),
        RecreationalAthlete("Кайф", 60, 165, favorite_activity="yoga")
    ]

    for a in athletes:
        print(a.perform_action())
    print()


def demo_collection_with_inheritance():
    print("=" * 60)
    print("СЦЕНАРИЙ 3: Коллекция AthleteCollection с разными типами")
    print("=" * 60)

    col = AthleteCollection()
    col.add(Athlete("Алекс", 75, 180, 120))
    col.add(CompetitiveAthlete("Мария", 65, 170, 150, wins=2))
    col.add(RecreationalAthlete("Олег", 80, 175, 90, favorite_activity="cycling"))

    print(f"Всего в коллекции: {len(col)}")
    for a in col:
        print(a)

    print("\n--- Фильтрация по типу CompetitiveAthlete (isinstance) ---")
    competitive_list = [a for a in col if isinstance(a, CompetitiveAthlete)]
    for a in competitive_list:
        print(f"  {a.name} (рейтинг: {a.rating})")

    print("\n--- Фильтрация по типу RecreationalAthlete ---")
    rec_list = [a for a in col if isinstance(a, RecreationalAthlete)]
    for a in rec_list:
        print(f"  {a.name} (активность: {a.favorite_activity})")
    print()


def demo_polymorphic_calls():
    print("=" * 60)
    print("СЦЕНАРИЙ 4: Полиморфизм – вызов perform_action() без проверки типов")
    print("=" * 60)

    col = AthleteCollection()
    col.add(CompetitiveAthlete("Иван", 80, 180, wins=1))
    col.add(RecreationalAthlete("Петр", 70, 175, favorite_activity="running"))
    col.add(CompetitiveAthlete("Сергей", 85, 185, wins=0))

    for a in col:
        print(a.perform_action())


if __name__ == "__main__":
    demo_inheritance()
    demo_polymorphism()
    demo_collection_with_inheritance()
    demo_polymorphic_calls()