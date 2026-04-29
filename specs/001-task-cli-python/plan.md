# Implementation Plan: task-cli-sandbox

**Branch**: `001-task-cli-python` | **Date**: 2026-04-29 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-task-cli-python/spec.md`

**Note**: This template is filled in by the `/speckit-plan` command. See `.specify/templates/plan-template.md` for the execution workflow.

## Summary

Implementar un CLI en Python para gestión de tareas (add, list, update, delete) que persista los datos en un archivo JSON local, cumpliendo con la arquitectura de capas y los criterios de éxito definidos.

## Technical Context

**Language/Version**: Python 3.x
**Primary Dependencies**: Standard Library (`argparse`, `json`, `datetime`, `os`)
**Storage**: `tasks.json` (Local file in execution directory)
**Testing**: `pytest`
**Target Platform**: Local OS (Windows/Linux/macOS)
**Project Type**: CLI
**Performance Goals**: < 500ms for read/write operations
**Constraints**: Pure CLI, no external dependencies if possible to keep it lightweight.
**Scale/Scope**: MVP (Single user, local)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **I. Disciplina de Gates**: Plan generado automáticamente vía Capa 3.
- [x] **II. Arquitectura de Capas y Persistencia**: Se utilizará Python y un archivo JSON (`tasks.json`).
- [x] **III. Validación de Modelos**: Planificado considerando la eficiencia de tokens.
- [x] **IV. Trazabilidad**: El diseño se apoya en `spec.md` y produce artefactos estándar.
- [x] **V. Economía de Tokens**: Decisiones simples, sin librerías pesadas para minimizar la complejidad.

## Project Structure

### Documentation (this feature)

```text
specs/001-task-cli-python/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
└── contracts/
    └── cli-contract.md
```

### Source Code (repository root)

```text
src/
├── core/
│   └── task_manager.py     # Lógica de negocio y persistencia
├── cli/
│   └── main.py             # Interfaz argparse y entrada principal
└── models/
    └── task.py             # Definición de la entidad Task (opcional, dataclass)

tests/
├── unit/
│   └── test_task_manager.py
└── integration/
    └── test_cli.py
```

**Structure Decision**: Opción de proyecto único (Single project) con separación clara entre la interfaz CLI y la lógica core (Task Manager) para facilitar el testing independiente.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

Ninguna violación.

---

## Decisiones Técnicas Mandatorias (enmienda post-Gate 2)

Los siguientes contratos de implementación son **mandatorios** y deben reflejarse en `tasks.md`:

### 1. Schema JSON — `{metadata, tasks}` (FR-002)
El archivo `tasks.json` NO es un array plano. Ver `data-model.md` para el schema completo.
`metadata.next_id` es el único mecanismo válido de generación de IDs — nunca `max(id)+1`.

### 2. Escritura Atómica (SC-005)
Toda escritura a `tasks.json` usa archivo temporal + `os.replace()`. Ver patrón en `data-model.md §Escritura Atómica`.

### 3. Exit Codes y stderr (FR-009)
- Éxito → `sys.exit(0)`
- Cualquier error → mensaje a `sys.stderr` + `sys.exit(1)`

### 4. Filtrado por estado (FR-004)
El subcomando `list` acepta un argumento opcional posicional: `task-cli list [status]` donde `status` ∈ `{todo, in-progress, done}`. Si se omite, lista todas. Si es inválido, error + `sys.exit(1)`.

