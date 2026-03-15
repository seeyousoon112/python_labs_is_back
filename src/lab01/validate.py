

def validate_name(name: str) -> None:
    """Проверяет, что имя - непустая строка."""
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name must be a non-empty string")

def validate_weight(weight: float) -> None:
    """Проверяет, что вес - положительное число."""
    if not isinstance(weight, (int, float)) or weight <= 0:
        raise ValueError("Weight must be a positive number")

def validate_height(height: float) -> None:
    """Проверяет, что рост - положительное число."""
    if not isinstance(height, (int, float)) or height <= 0:
        raise ValueError("Height must be a positive number")

def validate_record(record: float) -> None:
    """Проверяет, что личный рекорд - неотрицательное число."""
    if not isinstance(record, (int, float)) or record < 0:
        raise ValueError("Personal record must be a non-negative number")

def validate_health_status(status: str) -> None:
    """Проверяет, что статус здоровья допустим."""
    allowed = ("healthy", "injured", "recovering")
    if status not in allowed:
        raise ValueError(f"Health status must be one of {allowed}")

def validate_training_level(level: str) -> None:
    """Проверяет, что уровень подготовки допустим."""
    allowed = ("beginner", "intermediate", "advanced", "professional")
    if level not in allowed:
        raise ValueError(f"Training level must be one of {allowed}")

def validate_morale(morale: int) -> None:
    """Проверяет, что мораль - целое число от 0 до 10."""
    if not isinstance(morale, int) or morale < 0 or morale > 10:
        raise ValueError("Morale must be an integer between 0 and 10")