import datetime
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class Task:
    id: int
    description: str
    status: str
    createdAt: str
    updatedAt: str

    @classmethod
    def create(cls, id: int, description: str) -> "Task":
        now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        return cls(
            id=id,
            description=description,
            status="todo",
            createdAt=now,
            updatedAt=now
        )

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(**data)
