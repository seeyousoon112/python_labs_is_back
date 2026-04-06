#!/usr/bin/env python3
"""
Демонстрация работы контейнера AthleteCollection.
Показывает все требуемые сценарии: добавление, удаление, поиск, len, итерацию,
индексацию, сортировку, фильтрацию и проверку дубликатов.
"""
import sys
import os

# Добавляем корневую директорию проекта в путь поиска модулей
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.lab01.model import Athlete
from src.lab02.collection import AthleteCollection


def demo_basic_operations():
    """Сценарий 1: базовые операции (оценка 3) и проверка дубликатов (оценка 4)."""
    print("=" * 60)
    print("СЦЕНАРИЙ 1: Базовые операции и контроль дубликатов")
    print("=" * 60)

    col = AthleteCollection()

    # Создаём спортсменов
    a1 = Athlete("Иван", 75, 180, 120)
    a2 = Athlete("Мария", 65, 170, 95)
    a3 = Athlete("Петр", 80, 175, 110)

    # Добавляем
    col.add(a1)
    col.add(a2)
    col.add(a3)
    print(f"Добавлено 3 спортсмена. Размер коллекции: {len(col)}")

    # Попытка добавить дубликат (равный a1 по name, weight, height, record)
    try:
        col.add(Athlete("Иван", 75, 180, 120))
    except ValueError as e:
        print(f"Ошибка при добавлении дубликата: {e}")

    # Попытка добавить объект не Athlete
    try:
        col.add("не спортсмен")  # type: ignore
    except TypeError as e:
        print(f"Ошибка типа: {e}")

    # Вывод всех
    print("Все спортсмены:")
    for athlete in col.get_all():
        print(f"  - {athlete.name} (рекорд: {athlete.personal_record} кг)")

    # Удаление
    col.remove(a2)
    print(f"\nПосле удаления Марии. Размер: {len(col)}")
    for athlete in col:
        print(f"  - {athlete.name}")

    print()


def demo_find_and_iter():
    """Сценарий 2: поиск, __len__, __iter__ (оценка 4)."""
    print("=" * 60)
    print("СЦЕНАРИЙ 2: Поиск по атрибутам, длина, итерация")
    print("=" * 60)

    col = AthleteCollection()
    athletes = [
        Athlete("Анна", 55, 165, 80),
        Athlete("Анна", 58, 168, 85),   # тоже Анна, но другие параметры
        Athlete("Сергей", 85, 185, 150),
        Athlete("Ольга", 60, 172, 100)
    ]
    for a in athletes:
        col.add(a)

    # Поиск по имени
    anna_list = col.find_by_name("Анна")
    print(f"Найдено спортсменов с именем 'Анна': {len(anna_list)}")
    for a in anna_list:
        print(f"  - {a.name}, вес {a.weight} кг, рекорд {a.personal_record}")

    # Поиск по диапазону рекорда
    strong = col.find_by_record(min_record=100)
    print(f"\nСпортсмены с рекордом >= 100 кг: {len(strong)}")
    for a in strong:
        print(f"  - {a.name}: {a.personal_record} кг")

    # Итерация через for (__iter__)
    print("\nПеребор всех через for item in collection:")
    for a in col:
        print(f"  {a.name} (активен: {a.is_active})")

    print()


def demo_indexing_and_remove_at():
    """Сценарий 3: индексация и удаление по индексу (оценка 5)."""
    print("=" * 60)
    print("СЦЕНАРИЙ 3: Индексация и удаление по индексу")
    print("=" * 60)

    col = AthleteCollection()
    names = ["Алексей", "Дмитрий", "Елена", "Татьяна"]
    for name in names:
        col.add(Athlete(name, 70, 170, 90))

    print(f"Коллекция: {[col[i].name for i in range(len(col))]}")
    print(f"Первый элемент: {col[0].name}")
    print(f"Последний элемент: {col[-1].name}")

    # Удаление по индексу
    col.remove_at(1)  # удаляем Дмитрия
    print(f"После удаления индекса 1: {[col[i].name for i in range(len(col))]}")

    # Ошибка при выходе за границы
    try:
        col[10]
    except IndexError as e:
        print(f"Ошибка индексации: {e}")

    print()


def demo_sorting():
    """Сценарий 4: сортировка коллекции."""
    print("=" * 60)
    print("СЦЕНАРИЙ 4: Сортировка по разным ключам")
    print("=" * 60)

    col = AthleteCollection()
    raw = [
        ("Максим", 90, 185, 160),
        ("Алина", 52, 162, 70),
        ("Виктор", 78, 178, 130),
        ("Борис", 82, 180, 145),
    ]
    for name, w, h, r in raw:
        col.add(Athlete(name, w, h, r))

    print("Исходный порядок:", [a.name for a in col])

    # Сортировка по имени
    col.sort(key=lambda a: a.name)
    print("По имени:      ", [a.name for a in col])

    # Сортировка по весу (по убыванию)
    col.sort(key=lambda a: a.weight, reverse=True)
    print("По весу (убыв):", [f"{a.name} ({a.weight} кг)" for a in col])

    # Сортировка по рекорду
    col.sort(key=lambda a: a.personal_record)
    print("По рекорду:    ", [f"{a.name} ({a.personal_record} кг)" for a in col])

    print()


def demo_filtering():
    """Сценарий 5: логические операции, возвращающие новые коллекции."""
    print("=" * 60)
    print("СЦЕНАРИЙ 5: Фильтрация с созданием новых коллекций")
    print("=" * 60)

    col = AthleteCollection()
    # Создаём спортсменов с разными состояниями
    a1 = Athlete("Активный_здоровый", 70, 175, 120)
    a2 = Athlete("Травмированный", 68, 172, 100)
    a2.injure()
    a3 = Athlete("Восстанавливающийся", 72, 180, 110)
    a3.recover()
    a4 = Athlete("Неактивный", 65, 168, 90)
    a4.deactivate()
    a5 = Athlete("Профи_здоровый", 85, 185, 200)
    a5.set_training_level("professional")

    for a in [a1, a2, a3, a4, a5]:
        col.add(a)

    print(f"Исходная коллекция ({len(col)}):")
    for a in col:
        print(f"  - {a.name}: здоровье={a.health_status}, активен={a.is_active}, уровень={a.training_level}")

    # Фильтрация активных
    active_col = col.filter_active()
    print(f"\nАктивные спортсмены (новая коллекция, {len(active_col)}):")
    for a in active_col:
        print(f"  - {a.name}")

    # Фильтрация по здоровью
    healthy_col = col.filter_health_status("healthy")
    print(f"\nЗдоровые спортсмены ({len(healthy_col)}):")
    for a in healthy_col:
        print(f"  - {a.name}")

    # Фильтрация по уровню подготовки
    pro_col = col.filter_training_level("professional")
    print(f"\nПрофессионалы ({len(pro_col)}):")
    for a in pro_col:
        print(f"  - {a.name} (рекорд {a.personal_record} кг)")

    # Фильтрация по минимальному рекорду
    strong_col = col.filter_min_record(110)
    print(f"\nСпортсмены с рекордом >= 110 кг ({len(strong_col)}):")
    for a in strong_col:
        print(f"  - {a.name}: {a.personal_record} кг")

    # Проверка, что исходная коллекция не изменилась
    print(f"\nИсходная коллекция всё ещё содержит {len(col)} элементов.")
    print()


def main():
    demo_basic_operations()
    demo_find_and_iter()
    demo_indexing_and_remove_at()
    demo_sorting()
    demo_filtering()


if __name__ == "__main__":
    main()