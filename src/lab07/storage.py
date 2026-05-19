
import json
from typing import List, Dict, Any
from src.lab01.model import Athlete
from src.lab03.models import CompetitiveAthlete, RecreationalAthlete

def _serialize_athlete(athlete: Athlete) -> Dict[str, Any]:
    data = {
        "_class": athlete.__class__.__name__,
        "name": athlete.name,
        "weight": athlete.weight,
        "height": athlete.height,
        "personal_record": athlete.personal_record,
        "is_active": athlete.is_active,
        "health_status": athlete.health_status,
        "training_level": athlete.training_level,
        "morale": athlete.morale,
    }
    if isinstance(athlete, CompetitiveAthlete):
        data["wins"] = athlete.wins
        data["rating"] = athlete.rating
    elif isinstance(athlete, RecreationalAthlete):
        data["favorite_activity"] = athlete.favorite_activity
        data["enjoyment_level"] = athlete.enjoyment_level
    return data

def _deserialize_athlete(data: Dict[str, Any]) -> Athlete:
    class_name = data.pop("_class")
    if class_name == "Athlete":
        return Athlete(
            data["name"], data["weight"], data["height"], data["personal_record"]
        )
    elif class_name == "CompetitiveAthlete":
        return CompetitiveAthlete(
            data["name"], data["weight"], data["height"], data["personal_record"],
            wins=data.get("wins", 0), rating=data.get("rating", 1000.0)
        )
    elif class_name == "RecreationalAthlete":
        return RecreationalAthlete(
            data["name"], data["weight"], data["height"], data["personal_record"],
            favorite_activity=data.get("favorite_activity", "running"),
            enjoyment_level=data.get("enjoyment_level", 5)
        )
    else:
        raise ValueError(f"Unknown class: {class_name}")

def save(collection: List[Athlete], filepath: str) -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump([_serialize_athlete(a) for a in collection], f, indent=4, ensure_ascii=False)

def load(filepath: str) -> List[Athlete]:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [_deserialize_athlete(item) for item in data]
    except FileNotFoundError:
        return []