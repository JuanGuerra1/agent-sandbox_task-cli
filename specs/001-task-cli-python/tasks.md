# Implementation Tasks: task-cli-sandbox

**Feature**: `001-task-cli-python`

This document outlines the actionable, dependency-ordered tasks required to implement the feature, organized by User Story to support independent delivery.

## Dependencies

- **US3 (Persistencia en JSON)**: Foundational. Must be implemented first to support adding and listing.
- **US1 (Gestión Básica)**: Depends on US3.
- **US2 (Filtrado por Estado)**: Depends on US1 (list command).

## Phase 1: Setup

Goal: Initialize project structure and test harness.

- [x] T001 Create project directory structure (`src/core`, `src/cli`, `src/models`, `tests/unit`, `tests/integration`)
- [x] T002 [P] Create `tests/__init__.py`, `src/__init__.py`, and configuration for pytest

## Phase 2: Foundational (US3 - Persistencia en JSON)

Goal: Establecer el modelo de datos y el mecanismo de lectura/escritura en el archivo `tasks.json`.

**Independent Test**: Poder instanciar el manager, guardar datos simulados y recuperarlos del archivo.

- [x] T003 [US3] Create `src/models/task.py` representing the Task entity (dataclass or dict-based)
- [x] T004 [US3] Create `src/core/task_manager.py` with `_load_tasks` and `_save_tasks` methods using `json`
- [x] T005 [P] [US3] Write unit tests in `tests/unit/test_task_manager.py` for JSON persistence and error handling

## Phase 3: User Story 1 (Gestión Básica)

Goal: Implementar operaciones CRUD (add, list, update, delete) en el core y conectarlas a la CLI.

**Independent Test**: Ejecutar `task-cli add "test"`, verificar que se genera ID, y ejecutar `task-cli list` para verlo.

- [x] T006 [US1] Implement `add_task` in `src/core/task_manager.py` (auto-increment ID, ISO timestamps)
- [x] T007 [US1] Implement `list_tasks`, `update_task_description`, `update_task_status`, and `delete_task` in `src/core/task_manager.py`
- [x] T008 [P] [US1] Update unit tests in `tests/unit/test_task_manager.py` for CRUD operations
- [x] T009 [US1] Create `src/cli/main.py` with `argparse` for commands: `add`, `update`, `delete`, `mark-in-progress`, `mark-done`, `list`.
- [x] T010 [US1] Wire `src/cli/main.py` to `TaskManager`. **Contrato de errores obligatorio:** toda excepción del manager debe capturarse, imprimirse en `sys.stderr`, y terminar con `sys.exit(1)`. Éxito → `sys.exit(0)` implícito (FR-009).
- [x] T011 [P] [US1] Write integration tests in `tests/integration/test_cli.py` for basic workflows

## Phase 4: User Story 2 (Filtrado por Estado)

Goal: Permitir filtrar la lista de tareas en base a su estado desde la CLI.

**Independent Test**: Añadir tareas mixtas, ejecutar `task-cli list done` y confirmar que solo salen las completadas.

- [x] T012 [US2] Update `list_tasks` in `src/core/task_manager.py` to accept a `status` filter
- [x] T013 [US2] Update `src/cli/main.py`'s `list` command to parse the optional `status` argument
- [x] T014 [P] [US2] Update unit and integration tests to verify filtering logic

## Phase 5: Polish & Cross-Cutting Concerns

Goal: Asegurar el manejo correcto de edge cases y limpieza final.

- [x] T015 Verify error handling for non-existent IDs in `update` and `delete` flows
- [x] T016 Add user-friendly stdout formatting (e.g. tabular output) in `src/cli/main.py` for the `list` command

## Implementation Strategy

1. Mínimo Producto Viable (MVP): Phases 1 y 2 establecen la base técnica. Phase 3 entrega el 90% del valor.
2. Desarrollo Incremental: Probar persistencia pura (US3), luego lógica de negocio y finalmente CLI (US1).
