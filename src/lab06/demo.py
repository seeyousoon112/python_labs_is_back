# src/lab06/demo.py
from src.lab01.model import Athlete
from src.lab03.models import CompetitiveAthlete, RecreationalAthlete
from src.lab06.container import TypedCollection, Displayable, Scorable

def demo_grade3():
    """Оценка 3: базовая типизированная коллекция."""
    print("=" * 60)
    print("СЦЕНАРИЙ 1 (оценка 3): TypedCollection[Athlete]")
    print("=" * 60)

    col: TypedCollection[Athlete] = TypedCollection[Athlete]()
    a1 = Athlete("Иван", 75, 180, 120)
    a2 = CompetitiveAthlete("Мария", 65, 170, 150, wins=2, rating=1250)
    a3 = RecreationalAthlete("Олег", 82, 175, 90, favorite_activity="cycling", enjoyment_level=7)

    col.add(a1)
    col.add(a2)
    col.add(a3)

    print("Добавлены три спортсмена.")
    print(f"Всего элементов: {len(col)}")
    print("Содержимое (через __iter__):")
    for item in col:
        print(f"  {item}")

    # Проверка на добавление некорректного типа (будет ошибка во время выполнения)
    try:
        col.add("не спортсмен")  # type: ignore
    except TypeError as e:
        print(f"Ожидаемая ошибка типа: {e}")

def demo_grade4():
    """Оценка 4: методы find, filter, map."""
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 2 (оценка 4): find, filter, map")
    print("=" * 60)

    col = TypedCollection[Athlete]()
    col.add(Athlete("Анна", 60, 165, 80))
    col.add(CompetitiveAthlete("Борис", 85, 185, 160, wins=3, rating=1300))
    col.add(RecreationalAthlete("Виктор", 70, 172, 100, favorite_activity="running", enjoyment_level=5))

    # find
    found = col.find(lambda a: a.name == "Борис")
    print(f"find('Борис'): {found.name if found else None}")
    not_found = col.find(lambda a: a.name == "Максим")
    print(f"find('Максим'): {not_found}")

    # filter
    heavy = col.filter(lambda a: a.weight > 70)
    print(f"filter (вес > 70): {[a.name for a in heavy]}")

    # map – тип результата str
    names: list[str] = col.map(lambda a: a.name)
    print(f"map (имена): {names}")

    # map – тип результата float
    records: list[float] = col.map(lambda a: a.personal_record)
    print(f"map (рекорды): {records}")

def demo_grade5():
    """Оценка 5: протоколы и ограниченные TypeVar."""
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 3 (оценка 5): TypedCollection с ограничениями (Displayable, Scorable)")
    print("=" * 60)

    # Коллекция объектов, поддерживающих Displayable
    col_display: TypedCollection[Displayable] = TypedCollection[Displayable]()
    # Объекты разных типов, но все имеют метод display (унаследован от Athlete)
    col_display.add(Athlete("Алексей", 80, 180, 140))
    col_display.add(CompetitiveAthlete("Сергей", 90, 185, 200, wins=5, rating=1500))
    col_display.add(RecreationalAthlete("Дмитрий", 75, 178, 110, favorite_activity="swimming", enjoyment_level=8))

    print("Коллекция Displayable (вызов display):")
    for obj in col_display:
        print(f"  {obj.display()}")

    # Коллекция объектов, поддерживающих Scorable
    col_score: TypedCollection[Scorable] = TypedCollection[Scorable]()
    col_score.add(Athlete("Елена", 55, 162, 90))
    col_score.add(CompetitiveAthlete("Игорь", 88, 183, 170, wins=4, rating=1450))
    # Даже если у объекта нет явного наследования от Scorable, но метод score есть – он подходит
    print("\nКоллекция Scorable (вызов score – личный рекорд):")
    for obj in col_score:
        print(f"  {obj.name}: score = {obj.score()}")

    # Проверка, что нельзя добавить объект без метода score (например, строку) – IDE подскажет,
    # но во время выполнения также будет ошибка, если тип не совпадает.
    # Для демонстрации закомментировано:
    # col_score.add("не спортсмен")  # Ошибка типа

if __name__ == "__main__":
    demo_grade3()
    demo_grade4()
    demo_grade5()