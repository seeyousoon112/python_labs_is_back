


from src.lab01.model import Athlete
from src.lab03.models import CompetitiveAthlete, RecreationalAthlete




def by_name(athlete):
    """Ключ сортировки по имени."""
    return athlete.name

def by_weight(athlete):
    """Ключ сортировки по весу."""
    return athlete.weight

def by_record(athlete):
    """Ключ сортировки по личному рекорду."""
    return athlete.personal_record

def by_rating(athlete):
    """Ключ сортировки по рейтингу (для CompetitiveAthlete)."""
    if isinstance(athlete, CompetitiveAthlete):
        return athlete.rating
    return 0.0

def by_enjoyment(athlete):
    """Ключ сортировки по уровню удовольствия (для RecreationalAthlete)."""
    if isinstance(athlete, RecreationalAthlete):
        return athlete.enjoyment_level
    return 0



def is_active(athlete):

    return athlete.is_active

def is_healthy(athlete):

    return athlete.health_status == "healthy"

def is_competitive(athlete):

    return isinstance(athlete, CompetitiveAthlete)

def is_recreational(athlete):

    return isinstance(athlete, RecreationalAthlete)

def has_record_above(threshold):

    def predicate(athlete):
        return athlete.personal_record > threshold
    return predicate

def make_weight_filter(max_weight):

    def filter_fn(athlete):
        return athlete.weight <= max_weight
    return filter_fn




def to_string(athlete):

    return str(athlete)

def extract_name(athlete):

    return athlete.name

def apply_discountпшк(discount):

    def discount_func(athlete):
        new_record = athlete.personal_record * (1 - discount)
        try:
            athlete.personal_record = new_record
        except (RuntimeError, ValueError) as e:
            print(f"Не удалось применить скидку к {athlete.name}: {e}")
        return athlete
    return discount_func

def increase_morale(delta):
    def func(athlete):
        new_morale = athlete.morale + delta
        try:
            athlete.morale = new_morale
        except ValueError:
            pass
        return athlete
    return func