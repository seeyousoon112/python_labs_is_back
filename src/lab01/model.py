# src/lab01/model.py
from src.lab01 import validate

class Athlete:
    # Атрибуты класса (с аннотациями)
    total_athletes: int = 0
    sport_type: str = "running"
    default_training_level: str = "beginner"
    max_morale: int = 10
    min_morale: int = 0
    weight_unit: str = "kg"
    height_unit: str = "cm"
    record_unit: str = "kg"

    def __init__(self, name: str, weight: float, height: float, record: float = 0.0) -> None:
        validate.validate_name(name)
        validate.validate_weight(weight)
        validate.validate_height(height)
        validate.validate_record(record)

        self._name: str = name.strip()
        self._weight: float = weight
        self._height: float = height
        self._personal_record: float = record
        self._is_active: bool = True
        self._health_status: str = "healthy"
        self._training_level: str = Athlete.default_training_level
        self._morale: int = Athlete.max_morale

        Athlete.total_athletes += 1

    @property
    def name(self) -> str:
        return self._name

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, value: float) -> None:
        validate.validate_weight(value)
        self._weight = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        validate.validate_height(value)
        self._height = value

    @property
    def personal_record(self) -> float:
        return self._personal_record

    @personal_record.setter
    def personal_record(self, value: float) -> None:
        if not self._is_active:
            raise RuntimeError("Cannot change record of inactive athlete")
        if self._health_status == "injured":
            raise RuntimeError("Cannot change record while injured")
        if self._health_status == "recovering":
            print("Warning: Athlete is recovering, setting record may be risky.")
        max_record = self._max_record_for_level()
        if value > max_record:
            raise ValueError(f"Record {value} exceeds maximum allowed for level {self._training_level} ({max_record})")
        validate.validate_record(value)
        self._personal_record = value

    @property
    def is_active(self) -> bool:
        return self._is_active

    @property
    def health_status(self) -> str:
        return self._health_status

    @property
    def training_level(self) -> str:
        return self._training_level

    @property
    def morale(self) -> int:
        return self._morale

    @morale.setter
    def morale(self, value: int) -> None:
        if value < Athlete.min_morale or value > Athlete.max_morale:
            raise ValueError(f"Morale must be between {Athlete.min_morale} and {Athlete.max_morale}")
        self._morale = value

    def activate(self) -> None:
        self._is_active = True

    def deactivate(self) -> None:
        self._is_active = False

    def injure(self) -> None:
        self._health_status = "injured"

    def recover(self) -> None:
        self._health_status = "recovering"

    def heal(self) -> None:
        self._health_status = "healthy"

    def set_training_level(self, level: str) -> None:
        validate.validate_training_level(level)
        self._training_level = level

    def _max_record_for_level(self) -> float:
        limits = {
            "beginner": 100,
            "intermediate": 200,
            "advanced": 350,
            "professional": float('inf')
        }
        return limits[self._training_level]

    def set_record(self, new_record: float) -> None:
        self.personal_record = new_record

    def bmi(self) -> float:
        height_m = self._height / 100
        return round(self._weight / (height_m ** 2), 2)

    # Для протоколов (оценка 5)
    def display(self) -> str:
        """Реализует протокол Displayable."""
        return f"{self.name}: {self.weight}{self.weight_unit}, record {self.personal_record}{self.record_unit}"

    def score(self) -> float:
        """Реализует протокол Scorable. Используем личный рекорд как оценку."""
        return self.personal_record

    def __str__(self) -> str:
        status = "active" if self._is_active else "inactive"
        return (f"Athlete: {self._name}, weight: {self._weight}{Athlete.weight_unit}, "
                f"height: {self._height}{Athlete.height_unit}, "
                f"record: {self._personal_record}{Athlete.record_unit}, BMI: {self.bmi()}, "
                f"health: {self._health_status}, level: {self._training_level}, "
                f"morale: {self._morale}/{Athlete.max_morale}, status: {status}")

    def __repr__(self) -> str:
        return (f"Athlete(name='{self._name}', weight={self._weight}, "
                f"height={self._height}, record={self._personal_record})")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Athlete):
            return False
        return (self._name == other._name and
                self._weight == other._weight and
                self._height == other._height and
                self._personal_record == other._personal_record)