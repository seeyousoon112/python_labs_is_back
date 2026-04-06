
import sys
import os

# Добавляем корневую директорию проекта в путь поиска модулей
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.lab01.model import Athlete

def demo_validation():
    """Сценарий 1: базовая валидация."""
    print("=== Сценарий 1: Валидация данных ===")
    try:
        a = Athlete("", 70, 175)
    except ValueError as e:
        print(f"Ошибка при создании: {e}")

    try:
        a = Athlete("Иван", -70, 175)
    except ValueError as e:
        print(f"Ошибка при создании: {e}")

    a = Athlete("Иван", 70, 175, 100)
    print(f"Создан спортсмен: {a}")

    try:
        a.weight = -80
    except ValueError as e:
        print(f"Ошибка при изменении веса: {e}")
    print()

def demo_state_changes():
    """Сценарий 2: базовое состояние is_active."""
    print("=== Сценарий 2: Логическое состояние (is_active) ===")
    a = Athlete("Мария", 65, 170, 80)
    print(f"Начальное состояние: {a}")

    a.deactivate()
    try:
        a.set_record(85)
    except RuntimeError as e:
        print(f"Ошибка при установке рекорда (неактивен): {e}")

    a.activate()
    a.set_record(85)
    print(f"После активации: {a}")
    print()

def demo_equality():
    """Сценарий 3: сравнение объектов."""
    print("=== Сценарий 3: Сравнение и независимость ===")
    a1 = Athlete("Петр", 80, 180, 120)
    a2 = Athlete("Петр", 80, 180, 120)
    a3 = Athlete("Петр", 80, 180, 130)

    print(f"a1: {repr(a1)}")
    print(f"a2: {repr(a2)}")
    print(f"a3: {repr(a3)}")
    print(f"a1 == a2 ? {a1 == a2}")
    print(f"a1 == a3 ? {a1 == a3}")

    a2.deactivate()
    print(f"a2 деактивирован, но сравнение a1 == a2 всё ещё {a1 == a2}")
    print()

def demo_class_attribute():
    """Сценарий 4: атрибуты класса (минимум 4)."""
    print("=== Сценарий 4: Атрибуты класса ===")
    # Доступ через класс
    print(f"Athlete.total_athletes = {Athlete.total_athletes}")
    print(f"Athlete.sport_type = {Athlete.sport_type}")
    print(f"Athlete.default_training_level = {Athlete.default_training_level}")
    print(f"Athlete.max_morale = {Athlete.max_morale}")
    print(f"Athlete.min_morale = {Athlete.min_morale}")
    print(f"Athlete.weight_unit = {Athlete.weight_unit}")
    print(f"Athlete.height_unit = {Athlete.height_unit}")
    print(f"Athlete.record_unit = {Athlete.record_unit}")

    # Создаём экземпляры и показываем доступ через них
    a1 = Athlete("Олег", 75, 182, 110)
    a2 = Athlete("Анна", 62, 168, 95)
    print(f"\nСоздано два спортсмена: {a1.name} и {a2.name}")
    print(f"Через экземпляр a1: a1.sport_type = {a1.sport_type}")
    print(f"Через экземпляр a2: a2.max_morale = {a2.max_morale}")
    print(f"Теперь Athlete.total_athletes = {Athlete.total_athletes}")
    print()

def demo_multiple_states():
    """Сценарий 5: множественные состояния (здоровье, уровень, мораль)."""
    print("=== Сценарий 5: Множественные состояния ===")
    a = Athlete("Алексей", 78, 185, 140)
    a.set_training_level("intermediate")
    print(f"Исходный спортсмен:\n{a}")

    # Пробуем установить рекорд выше допустимого для intermediate (200)
    try:
        a.set_record(220)
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Повышаем уровень до advanced
    a.set_training_level("advanced")
    a.set_record(220)
    print(f"После повышения уровня и установки рекорда 220:\n{a}")

    # Травмируем спортсмена человека прям тут
    a.injure()
    print(f"Травма: {a.health_status}")
    try:
        a.set_record(230)
    except RuntimeError as e:
        print(f"Ошибка при попытке установить рекорд в состоянии injured: {e}")

    # Переводим в состояние восстановления ( как поколечили так и починили)
    a.recover()
    print(f"Переход в recovering:")
    a.set_record(230)  # теперь можно, но с предупреждением
    print(f"После установки рекорда в recovering:\n{a}")

    # Полное излечение
    a.heal()
    print(f"После излечения (healthy): {a.health_status}")

    # Изменение морали с проверкой через атрибуты класса
    try:
        a.morale = 15  # превышает max_morale
    except ValueError as e:
        print(f"Ошибка при установке морали: {e}")
    a.morale = 5
    print(f"Мораль понижена до {a.morale}")
    print()

if __name__ == "__main__":
    demo_validation()
    demo_state_changes()
    demo_equality()
    demo_class_attribute()
    demo_multiple_states()