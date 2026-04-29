import json
import os
import sys
import tempfile
from pathlib import Path
from typing import List, Optional

from src.models.task import Task


class TaskManager:
    def __init__(self, filepath: Optional[str] = None):
        # FR-008: usar CWD, no el directorio del script
        self.filepath = Path(filepath) if filepath else Path.cwd() / "tasks.json"

    def _load(self) -> dict:
        """Carga el archivo tasks.json. Si no existe, retorna estructura vacía."""
        if not self.filepath.exists():
            return {"metadata": {"next_id": 1}, "tasks": []}
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            # Validar estructura mínima
            if "metadata" not in data or "tasks" not in data:
                raise ValueError("Schema inválido: faltan claves 'metadata' o 'tasks'")
            return data
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Error: tasks.json está corrupto o tiene un schema inválido: {e}", file=sys.stderr)
            sys.exit(1)

    def _save(self, data: dict) -> None:
        """SC-005: escritura atómica via tempfile + os.replace()."""
        dir_ = self.filepath.parent
        dir_.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile("w", dir=dir_, delete=False,
                                         suffix=".tmp", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            tmp_path = f.name
        os.replace(tmp_path, self.filepath)  # atómico en mismo filesystem

    def add_task(self, description: str) -> Task:
        if not description or not description.strip():
            print("Error: la descripción no puede estar vacía.", file=sys.stderr)
            sys.exit(1)
        data = self._load()
        # FR-002: usar metadata.next_id, NUNCA max(id)+1
        new_id = data["metadata"]["next_id"]
        data["metadata"]["next_id"] = new_id + 1
        new_task = Task.create(new_id, description.strip())
        data["tasks"].append(new_task.to_dict())
        self._save(data)
        return new_task

    def list_tasks(self, status: Optional[str] = None) -> List[Task]:
        data = self._load()
        tasks = [Task.from_dict(t) for t in data["tasks"]]
        if status:
            tasks = [t for t in tasks if t.status == status]
        return tasks

    def update_task_description(self, task_id: int, description: str) -> Optional[Task]:
        if not description or not description.strip():
            print("Error: la descripción no puede estar vacía.", file=sys.stderr)
            sys.exit(1)
        data = self._load()
        for t in data["tasks"]:
            if t["id"] == task_id:
                t["description"] = description.strip()
                from datetime import datetime, timezone
                t["updatedAt"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
                self._save(data)
                return Task.from_dict(t)
        return None  # ID no encontrado — la CLI maneja el exit(1)

    def update_task_status(self, task_id: int, status: str) -> Optional[Task]:
        data = self._load()
        for t in data["tasks"]:
            if t["id"] == task_id:
                t["status"] = status
                from datetime import datetime, timezone
                t["updatedAt"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
                self._save(data)
                return Task.from_dict(t)
        return None

    def delete_task(self, task_id: int) -> bool:
        data = self._load()
        original_count = len(data["tasks"])
        data["tasks"] = [t for t in data["tasks"] if t["id"] != task_id]
        if len(data["tasks"]) < original_count:
            self._save(data)
            return True
        return False
