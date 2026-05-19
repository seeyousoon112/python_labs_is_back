

from typing import List
from src.lab01.model import Athlete
from src.lab03.models import CompetitiveAthlete, RecreationalAthlete
from src.lab05.strategies import by_name, by_weight, by_record, by_rating
from src.lab07.app import App
from src.lab07.exceptions import DuplicateItemError, ItemNotFoundException, ValidationError

def print_table(athletes: List[Athlete]) -> None:
    if not athletes:
        print("  Нет данных.")
        return
    # Заголовок
    print(f"{'Имя':<15} {'Вес(кг)':<8} {'Рост(см)':<8} {'Рекорд(кг)':<10} {'Активен':<8} {'Здоровье':<12} {'Уровень':<12}")
    print("-" * 80)
    for a in athletes:
        print(f"{a.name:<15} {a.weight:<8.1f} {a.height:<8.1f} {a.personal_record:<10.1f} "
              f"{'Да' if a.is_active else 'Нет':<8} {a.health_status:<12} {a.training_level:<12}")
    if any(isinstance(a, (CompetitiveAthlete, RecreationalAthlete)) for a in athletes):
        print("\nДополнительная информация для специальных типов:")
        for a in athletes:
            if isinstance(a, CompetitiveAthlete):
                print(f"  {a.name}: соревновательный, побед={a.wins}, рейтинг={a.rating}")
            elif isinstance(a, RecreationalAthlete):
                print(f"  {a.name}: любитель, активность={a.favorite_activity}, удовольствие={a.enjoyment_level}")

def input_athlete() -> Athlete:
    print("\n--- Добавление спортсмена ---")
    name = input("Имя: ").strip()
    if not name:
        raise ValidationError("Имя не может быть пустым")
    try:
        weight = float(input("Вес (кг): "))
        height = float(input("Рост (см): "))
        record = float(input("Личный рекорд (кг): "))
    except ValueError:
        raise ValidationError("Вес, рост и рекорд должны быть числами")
    
    print("Тип спортсмена: 1 - обычный, 2 - соревновательный, 3 - любитель")
    type_choice = input("Выберите тип: ")
    if type_choice == "2":
        try:
            wins = int(input("Количество побед: "))
            rating = float(input("Рейтинг: "))
        except ValueError:
            raise ValidationError("Победы и рейтинг должны быть числами")
        return CompetitiveAthlete(name, weight, height, record, wins, rating)
    elif type_choice == "3":
        activity = input("Любимое занятие: ")
        try:
            enjoyment = int(input("Уровень удовольствия (1-10): "))
        except ValueError:
            raise ValidationError("Уровень удовольствия должен быть числом")
        return RecreationalAthlete(name, weight, height, record, activity, enjoyment)
    else:
        return Athlete(name, weight, height, record)

def run() -> None:
    app = App("athletes.json")
    while True:
        print("\n" + "=" * 50)
        print("МЕНЮ СПОРТСМЕНОВ")
        print("1. Добавить спортсмена")
        print("2. Показать всех спортсменов")
        print("3. Найти спортсмена по имени")
        print("4. Фильтрация")
        print("5. Сортировка")
        print("6. Удалить спортсмена")
        print("0. Выход")
        choice = input("Выберите пункт: ")
        
        if choice == "0":
            print("Сохраняем данные...")
            app.exit()
            print("До свидания!")
            break
        
        elif choice == "1":
            try:
                athlete = input_athlete()
                app.add_athlete(athlete)
                print(f"Спортсмен '{athlete.name}' добавлен.")
            except (DuplicateItemError, ValidationError) as e:
                print(f"Ошибка: {e}")
            except Exception as e:
                print(f"Непредвиденная ошибка: {e}")
        
        elif choice == "2":
            athletes = app.get_all()
            print_table(athletes)
        
        elif choice == "3":
            name = input("Введите имя для поиска: ")
            athlete = app.find_by_name(name)
            if athlete:
                print_table([athlete])
            else:
                print(f"Спортсмен '{name}' не найден.")
        
        elif choice == "4":
            print("\n--- Фильтрация ---")
            print("1. Только активные")
            print("2. Только здоровые")
            print("3. Только соревновательные")
            print("4. Только любители")
            print("5. Рекорд выше заданного значения")
            sub = input("Выберите фильтр: ")
            if sub == "1":
                result = app.filter_athletes(lambda a: a.is_active)
            elif sub == "2":
                result = app.filter_athletes(lambda a: a.health_status == "healthy")
            elif sub == "3":
                from src.lab03.models import CompetitiveAthlete
                result = app.filter_athletes(lambda a: isinstance(a, CompetitiveAthlete))
            elif sub == "4":
                from src.lab03.models import RecreationalAthlete
                result = app.filter_athletes(lambda a: isinstance(a, RecreationalAthlete))
            elif sub == "5":
                try:
                    threshold = float(input("Минимальный рекорд: "))
                    result = app.filter_athletes(lambda a: a.personal_record > threshold)
                except ValueError:
                    print("Ошибка: нужно ввести число.")
                    continue
            else:
                print("Неверный пункт.")
                continue
            print_table(result)
        
        elif choice == "5":
            print("\n--- Сортировка ---")
            print("1. По имени")
            print("2. По весу")
            print("3. По рекорду")
            print("4. По рейтингу (для соревновательных)")
            sub = input("Выберите критерий: ")
            reverse = input("По убыванию? (y/n): ").lower() == "y"
            if sub == "1":
                app.sort_athletes(by_name, reverse)
            elif sub == "2":
                app.sort_athletes(by_weight, reverse)
            elif sub == "3":
                app.sort_athletes(by_record, reverse)
            elif sub == "4":
                app.sort_athletes(by_rating, reverse)
            else:
                print("Неверный пункт.")
                continue
            print("Сортировка выполнена.")
        
        elif choice == "6":
            name = input("Введите имя спортсмена для удаления: ")
            confirm = input(f"Удалить '{name}'? (y/n): ").lower()
            if confirm != 'y':
                print("Удаление отменено.")
                continue
            try:
                app.remove_athlete(name)
                print(f"Спортсмен '{name}' удалён.")
            except ItemNotFoundException as e:
                print(f"Ошибка: {e}")
        
        else:
            print("Неверный пункт. Попробуйте снова.")