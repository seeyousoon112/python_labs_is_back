"""
demo.py — демонстрация функциональных возможностей для ЛР-5.
"""

from src.lab01.model import Athlete
from src.lab03.models import CompetitiveAthlete, RecreationalAthlete
from src.lab05.collection import FunctionalAthleteCollection
import src.lab05.strategies as strat


def print_collection(title: str, collection: FunctionalAthleteCollection):
    """Утилита для вывода коллекции с заголовком."""
    print(f"\n{title}:")
    for a in collection:
        print(f"  {a}")


# ========== Сценарий 1: цепочка filter -> sort -> apply ==========
def scenario_chain():
    print("=" * 60)
    print("СЦЕНАРИЙ 1: Цепочка filter -> sort -> apply")
    print("=" * 60)

    # Создаём коллекцию с разными спортсменами
    col = FunctionalAthleteCollection()
    col.add(Athlete("Алексей", 75, 180, 120))
    col.add(CompetitiveAthlete("Мария", 65, 170, 150, wins=2, rating=1250))
    col.add(RecreationalAthlete("Олег", 82, 175, 90, favorite_activity="cycling", enjoyment_level=7))
    col.add(CompetitiveAthlete("Иван", 85, 185, 160, wins=3, rating=1180))
    col.add(RecreationalAthlete("Анна", 60, 165, 80, favorite_activity="yoga", enjoyment_level=9))
    col.add(Athlete("Петр", 78, 178, 110))

    print_collection("Исходная коллекция", col)

    # Шаг 1: фильтрация – оставляем только активных и здоровых
    filtered = col.filter_by(lambda a: strat.is_active(a) and strat.is_healthy(a))
    print_collection("После filter_by (активные и здоровые)", filtered)

    # Шаг 2: сортировка по рекорду (по возрастанию)
    sorted_col = filtered.sort_by(key_func=strat.by_record)
    print_collection("После sort_by по рекорду", sorted_col)

    # Шаг 3: apply – скидка 10% на рекорд
    discounted = sorted_col.apply(strat.apply_discount(0.1))
    print_collection("После apply (скидка 10% на рекорд)", discounted)

    # Покажем, что оригинальная коллекция не изменилась (filter создавал новые, sort работал на filtered)
    print_collection("Оригинальная коллекция (не изменилась)", col)


# ========== Сценарий 2: замена стратегии без изменения кода коллекции ==========
def scenario_strategy_replacement():
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 2: Замена стратегии сортировки")
    print("=" * 60)

    col = FunctionalAthleteCollection()
    col.add(CompetitiveAthlete("Глеб", 88, 186, 170, wins=4, rating=1350))
    col.add(CompetitiveAthlete("Борис", 72, 174, 120, wins=1, rating=1050))
    col.add(CompetitiveAthlete("Антон", 80, 180, 140, wins=2, rating=1200))

    print_collection("Исходная (порядок добавления)", col)

    # Сортировка по имени (через стратегию by_name)
    col.sort_by(key_func=strat.by_name)
    print_collection("Сортировка по имени (стратегия by_name)", col)

    # Сортировка по рейтингу (другая стратегия)
    col.sort_by(key_func=strat.by_rating)
    print_collection("Сортировка по рейтингу (стратегия by_rating)", col)

    # Сортировка по весу с помощью lambda (передаём функцию прямо в метод)
    col.sort_by(key_func=lambda a: a.weight)
    print_collection("Сортировка по весу (lambda)", col)


# ========== Сценарий 3: использование callable-объекта как стратегии ==========
def scenario_callable_strategy():
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 3: Callable-объект как стратегия (фабрика фильтров)")
    print("=" * 60)

    col = FunctionalAthleteCollection()
    for w in [70, 85, 62, 78, 91]:
        col.add(Athlete(f"Спортсмен-{w}", w, 175, 100))

    print_collection("Все спортсмены", col)

    # Создаём фильтр через фабрику
    weight_limit = 80
    weight_filter = strat.make_weight_filter(weight_limit)   # возвращает callable

    filtered = col.filter_by(weight_filter)
    print_collection(f"Спортсмены с весом <= {weight_limit} (фильтр из фабрики)", filtered)

    # Другой пример: фабрика has_record_above
    record_filter = strat.has_record_above(120)
    # Предварительно изменим рекорды у некоторых
    for a in col._items:
        if a.name == "Спортсмен-70":
            a.personal_record = 90   # в пределах beginner (≤100)
        if a.name == "Спортсмен-85":
            a.personal_record = 80   # в пределах beginner # обращаемся напрямую к _items для демонстрации
        
    filtered2 = col.filter_by(record_filter)
    print_collection("Спортсмены с рекордом > 120 кг", filtered2)



def demo_builtin_hof():
    print("\n" + "=" * 60)
    print("ДОПОЛНИТЕЛЬНО: встроенные map, filter, sorted")
    print("=" * 60)

    col = FunctionalAthleteCollection()
    col.add(Athlete("Алиса", 54, 162, 95))
    col.add(Athlete("Борис", 82, 180, 130))
    col.add(Athlete("Виктор", 76, 175, 115))


    heavy = list(filter(lambda a: a.weight > 70, col.get_all()))
    print("Фильтр (вес > 70):", [a.name for a in heavy])


    names = list(map(lambda a: a.name, col.get_all()))
    print("Имена через map:", names)


    by_weight_desc = sorted(col.get_all(), key=lambda a: a.weight, reverse=True)
    print("Сортировка sorted по весу убыв.:", [a.name for a in by_weight_desc])


if __name__ == "__main__":
    scenario_chain()
    scenario_strategy_replacement()
    scenario_callable_strategy()
    demo_builtin_hof()