"""Собственные исключения для предметной области."""

class DuplicateItemError(Exception):
    """Объект с таким именем уже существует в коллекции."""
    pass

class ItemNotFoundException(Exception):
    """Объект не найден в коллекции."""
    pass

class ValidationError(Exception):
    """Ошибка валидации пользовательского ввода."""
    pass