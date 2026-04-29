# Research & Decisions: task-cli-sandbox

## Decision 1: CLI Framework
- **Decision**: Uso de la librería estándar `argparse`.
- **Rationale**: El CLI es muy simple (4 comandos básicos). Introducir dependencias externas como `click` o `typer` añade complejidad y carga de instalación innecesaria para un MVP que debe mantenerse ligero y rápido (< 500ms).
- **Alternatives considered**: 
  - `click`: Descartado por requerir instalación adicional.
  - `typer`: Descartado por requerir instalación adicional, aunque ofrece mejor tipado.

## Decision 2: Almacenamiento JSON y Escritura Atómica
- **Decision**: Archivo `tasks.json` en el CWD. Carga total en memoria y escritura atómica mediante archivo temporal + `os.replace()` al guardar (SC-005).
- **Rationale**: El MVP asume uso monousuario y baja volumetría. La escritura atómica vía `os.replace()` es mandatoria por spec (SC-005) para evitar corrupción del JSON si el proceso falla durante la escritura. Costo adicional: cero dependencias externas.
- **Alternatives considered**:
  - Sobreescritura directa: Descartada — viola SC-005 (spec exige atomicidad).
  - Manejo de bloqueos (locks) de archivo: No necesario por asunción de monousuario.

## Decision 3: Gestión de IDs
- **Decision**: Los IDs se gestionan mediante `metadata.next_id` persistido en el mismo `tasks.json`. Al crear una tarea: asignar `next_id`, luego incrementar y guardar.
- **Rationale**: La spec (FR-002) prohíbe explícitamente la reutilización de IDs y exige `metadata.next_id`. Usar `max(id)+1` falla cuando la lista está vacía y no garantiza la no-reutilización tras eliminaciones.
- **Alternatives considered**: Calcular `max(id)+1` en runtime — descartado porque viola FR-002 directamente.

## Decision 4: Formato de Timestamps
- **Decision**: Uso de ISO 8601 (`YYYY-MM-DDTHH:MM:SSZ` via `datetime.utcnow().isoformat() + "Z"`).
- **Rationale**: Ratificado en spec. Permite lectura humana y ordenamiento léxico.

## Decision 5: Exit Codes y stderr (FR-009)
- **Decision**: `sys.exit(0)` en éxito. `sys.exit(1)` en cualquier error, con el mensaje enviado a `sys.stderr`.
- **Rationale**: FR-009 es mandatorio. El CLI debe ser scriptable — los scripts de automatización dependen de exit codes non-zero para detectar fallos.
