# Data Model: task-cli-sandbox

> **Enmienda post-Gate 2 (2026-04-29):** schema corregido de array plano a objeto `{metadata, tasks}` para alinear con spec.md FR-002 y SC-005.

## Entities

### `Task`

Representa una tarea individual en el sistema.

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `id` | Integer | Identificador único de la tarea. | Autoincremental, > 0. **Nunca se reutiliza.** |
| `description` | String | Descripción textual. | No vacío, no en blanco. |
| `status` | String | Estado actual. | Enum: `"todo"`, `"in-progress"`, `"done"`. |
| `createdAt` | String | Fecha y hora de creación. | ISO 8601. |
| `updatedAt` | String | Fecha y hora de última modificación. | ISO 8601. |

### `Metadata`

| Field | Type | Description |
|-------|------|-------------|
| `next_id` | Integer | Próximo ID a asignar. Persiste entre ejecuciones. **Nunca decrece.** |

## Storage Schema

El archivo `tasks.json` es un **objeto JSON** con dos claves raíz. **NO es un array plano.**

```json
{
  "metadata": {
    "next_id": 3
  },
  "tasks": [
    {
      "id": 1,
      "description": "Comprar pan",
      "status": "done",
      "createdAt": "2026-04-29T10:00:00Z",
      "updatedAt": "2026-04-29T10:30:00Z"
    },
    {
      "id": 2,
      "description": "Aprender Python",
      "status": "in-progress",
      "createdAt": "2026-04-29T11:00:00Z",
      "updatedAt": "2026-04-29T11:00:00Z"
    }
  ]
}
```

> **Invariante:** `metadata.next_id` es siempre mayor que cualquier `id` en `tasks`. Al crear una tarea: asignar `next_id` actual, luego incrementar `next_id` en 1 y guardar.

## Escritura Atómica (SC-005)

Toda escritura a `tasks.json` DEBE seguir este patrón (`os.replace` es atómico en el mismo filesystem):

```python
import os, json, tempfile

def _save(data: dict, path: str):
    dir_ = os.path.dirname(os.path.abspath(path))
    with tempfile.NamedTemporaryFile("w", dir=dir_, delete=False, suffix=".tmp") as f:
        json.dump(data, f, indent=2)
        tmp_path = f.name
    os.replace(tmp_path, path)
```
