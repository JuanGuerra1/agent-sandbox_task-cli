# Feature Specification: task-cli-sandbox

**Feature Branch**: `001-task-cli-python`  
**Created**: 2026-04-29  
**Status**: Draft  
**Input**: User description: "Implementar un CLI en Python para gestión de tareas que persista en un archivo JSON local, ejecutado end-to-end con Spec Kit para validar la arquitectura de capas y la oscilación de modelos en Antigravity."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Gestión Básica de Tareas (Priority: P1)

Como usuario, quiero poder añadir, listar, actualizar y eliminar tareas desde la línea de comandos para gestionar mi flujo de trabajo diario.

**Why this priority**: Es la funcionalidad core del MVP que permite validar el flujo end-to-end de persistencia y CLI.

**Independent Test**: Se puede probar añadiendo una tarea con `add "comprar pan"` y verificando que aparece al ejecutar `list`.

**Acceptance Scenarios**:

1. **Given** un estado inicial sin tareas, **When** ejecuto `task-cli add "Tarea 1"`, **Then** el sistema confirma la creación con un ID.
2. **Given** una tarea existente, **When** ejecuto `task-cli list`, **Then** veo la tarea en la lista con su estado actual.

---

### User Story 2 - Filtrado por Estado (Priority: P1)

Como usuario, quiero poder filtrar las tareas por su estado (todo, in-progress, done) para enfocarme en lo pendiente.

**Why this priority**: Crucial para la usabilidad cuando el número de tareas crece.

**Independent Test**: Añadir tareas en diferentes estados y ejecutar `list done` para ver solo las completadas.

**Acceptance Scenarios**:

1. **Given** tareas en varios estados, **When** ejecuto `task-cli list in-progress`, **Then** solo se muestran las tareas marcadas como "in-progress".

---

### User Story 3 - Persistencia en JSON (Priority: P1)

Como usuario, quiero que mis tareas se guarden en un archivo local para no perderlas al cerrar la aplicación.

**Why this priority**: Requisito técnico fundamental para la validación del sandbox.

**Independent Test**: Añadir una tarea, cerrar la terminal, abrirla de nuevo y ejecutar `list`.

**Acceptance Scenarios**:

1. **Given** el archivo `tasks.json` existe, **When** añado una tarea, **Then** el archivo se actualiza con la nueva entrada en formato JSON válido.

---

### Edge Cases

- ¿Qué pasa cuando se intenta eliminar un ID que no existe? -> El sistema debe informar que el ID no se encontró.
- ¿Cómo maneja el sistema una descripción de tarea vacía? -> Debe rechazarla con un mensaje de error.
- ¿Qué sucede si el archivo JSON está corrupto? -> El sistema debe informar y opcionalmente ofrecer resetearlo.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: El sistema DEBE permitir añadir tareas con una descripción textual. Una descripción vacía o en blanco DEBE ser rechazada con un error.
- **FR-002**: El sistema DEBE asignar un ID único incremental a cada tarea. Los IDs NUNCA se reutilizan aunque se eliminen tareas. El valor del próximo ID debe persistir en una clave `metadata.next_id` dentro del mismo `tasks.json`.
- **FR-003**: El sistema DEBE permitir listar todas las tareas.
- **FR-004**: El sistema DEBE permitir filtrar la lista por estado: `todo`, `in-progress`, `done`.
- **FR-005**: El sistema DEBE permitir actualizar la descripción de una tarea por su ID. Si el ID no existe, el sistema DEBE informar el error.
- **FR-006**: El sistema DEBE permitir cambiar el estado de una tarea por su ID. Si el ID no existe, el sistema DEBE informar el error.
- **FR-007**: El sistema DEBE permitir eliminar una tarea por su ID. Si el ID no existe, el sistema DEBE informar el error.
- **FR-008**: El sistema DEBE persistir los datos en un archivo llamado `tasks.json` en el **Current Working Directory (CWD)** desde donde se invoca el comando (no el directorio del script/binario).
- **FR-009**: El CLI DEBE retornar código de salida `0` en operaciones exitosas y un código `non-zero` (≥1) en cualquier error, enviando el mensaje de error a `stderr`.

### Key Entities

- **Task**:
  - `id`: Entero único, nunca reutilizado.
  - `description`: String no vacío.
  - `status`: Enum (`todo`, `in-progress`, `done`).
  - `createdAt`: Timestamp ISO 8601.
  - `updatedAt`: Timestamp ISO 8601.
- **Estructura `tasks.json`**:
  ```json
  {
    "metadata": { "next_id": 5 },
    "tasks": [ { "id": 1, "description": "...", ... } ]
  }
  ```

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Las operaciones de escritura (add, update, delete) se completan en menos de 500ms.
- **SC-002**: El 100% de las tareas añadidas persisten correctamente tras reiniciar la aplicación.
- **SC-003**: El archivo `tasks.json` generado es un JSON válido según el estándar RFC 8259.
- **SC-004**: El sistema informa claramente al usuario del éxito o fallo de cada comando.
- **SC-005**: La escritura en `tasks.json` DEBE ser atómica: escribir en archivo temporal y hacer `os.replace()` al destino final para evitar corrupción en caso de fallo del proceso.
- **SC-006**: La lógica de negocio (TaskManager) DEBE estar en un módulo separado e importable independientemente de la interfaz CLI para permitir tests unitarios sin invocar subprocesos.

## Assumptions

- El usuario tiene permisos de escritura en el directorio donde ejecuta el CLI.
- No se requiere concurrencia (un solo usuario a la vez).
- La interfaz es puramente CLI, sin GUI.
