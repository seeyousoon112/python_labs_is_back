# python_labs_is_back 
Что вообще происходит в этой лабораторной работе и как оно все устроено?

Мной был выбран атлет(спортсмен) для реализации всевозможных характеристик, состояний и всего прочего.

   Начнем с того, что мне удалось придумать:
   
## Сущности предметной области «Фитнес / Спорт»

| Сущность    | Описание    |
| :---        | :---        |
| Athlete     | Спортсмен, обладающий физическими характеристиками и результатами |
| Workout     | Тренировка, включающая набор упражнений |
| Exercise    | Конкретное физическое действие с параметрами |
| Team        | Группа спортсменов для участия в соревнованиях |
| Competition | Мероприятие, где спортсмены или команды соревнуются |

## Характеристики (атрибуты экземпляра)

| Атрибут         | Тип    |
| :---            | :---   |
| name            | str    |
| weight          | float  |
| height          | float  |
| personal_record | float  |
| is_active       | bool   |
| health_status   | str    |
| training_level  | str    |
| morale          | int    |

## Состояния объекта

| Состояние       | Возможные значения                              |
| :---            | :---                                            |
| is_active       | True / False                                    |
| health_status   | "healthy", "injured", "recovering"              |
| training_level  | "beginner", "intermediate", "advanced", "professional" |
| morale          | целое число от 0 до 10                          |

## Атрибуты класса

| Атрибут класса           | Значение              |
| :---                     | :---                  |
| total_athletes           | 0 (счётчик)           |
| sport_type               | "Track and Field"     |
| default_training_level   | "beginner"            |
| max_morale               | 10                    |
| min_morale               | 0                     |
| weight_unit              | "kg"                  |
| height_unit              | "cm"                  |
| record_unit              | "kg"                  |

## Инварианты (ограничения)

| Атрибут         | Инвариант                                    |
| :---            | :---                                         |
| name            | непустая строка                              |
| weight          | положительное число (> 0)                    |
| height          | положительное число (> 0)                    |
| personal_record | неотрицательное число (≥ 0)                  |
| is_active       | булево значение                              |
| health_status   | одно из: "healthy", "injured", "recovering"  |
| training_level  | одно из: "beginner", "intermediate", "advanced", "professional" |
| morale          | целое число от 0 до 10                       |

## Методы (действия)

| Метод                     | Тип       |
| :---                      | :---      |
| set_record(new_record)    | Действие  |
| bmi()                     | Действие  |
| activate()                | Действие  |
| deactivate()              | Действие  |
| injure()                  | Действие  |
| recover()                 | Действие  |
| heal()                    | Действие  |
| set_training_level(level) | Действие  |

## Влияние состояний на поведение

| Состояние                | Условие                                   | Реакция                                      |
| :---                     | :---                                      | :---                                         |
| is_active = False        | Попытка изменить рекорд                   | RuntimeError                                 |
| health_status = "injured"| Попытка изменить рекорд                   | RuntimeError                                 |
| health_status = "recovering" | Попытка изменить рекорд               | Предупреждение (Warning)                     |
| training_level           | Установка рекорда выше допустимого        | ValueError с указанием максимума             |
| morale                   | Установка значения вне [0,10]             | ValueError    

# Итог:

![Картинка1](/src/images/lab01_img/laba.png)


  
