# CLI Contract: task-cli-sandbox

Este documento define la interfaz pública de línea de comandos (CLI) expuesta a los usuarios.

## Comandos

### 1. `add`
Añade una nueva tarea.
- **Uso**: `python src/cli/main.py add <description>`
- **Argumentos**:
  - `description` (Requerido): Texto de la tarea. Debe ir entre comillas si contiene espacios.
- **Salida de Éxito**: `Tarea añadida exitosamente (ID: <id>)`
- **Errores**: Falla si no se provee la descripción.

### 2. `update`
Actualiza la descripción de una tarea.
- **Uso**: `python src/cli/main.py update <id> <description>`
- **Argumentos**:
  - `id` (Requerido): ID de la tarea a actualizar.
  - `description` (Requerido): Nuevo texto de la tarea.
- **Salida de Éxito**: `Tarea <id> actualizada exitosamente.`
- **Errores**: Falla si el ID no existe o si el formato es incorrecto.

### 3. `delete`
Elimina una tarea por su ID.
- **Uso**: `python src/cli/main.py delete <id>`
- **Argumentos**:
  - `id` (Requerido): ID de la tarea a eliminar.
- **Salida de Éxito**: `Tarea <id> eliminada exitosamente.`
- **Errores**: Falla si el ID no existe.

### 4. `mark-in-progress`
Cambia el estado de una tarea a `in-progress`.
- **Uso**: `python src/cli/main.py mark-in-progress <id>`
- **Argumentos**:
  - `id` (Requerido): ID de la tarea a actualizar.
- **Salida de Éxito**: `Tarea <id> marcada como in-progress.`

### 5. `mark-done`
Cambia el estado de una tarea a `done`.
- **Uso**: `python src/cli/main.py mark-done <id>`
- **Argumentos**:
  - `id` (Requerido): ID de la tarea a actualizar.
- **Salida de Éxito**: `Tarea <id> marcada como done.`

### 6. `list`
Muestra todas las tareas, opcionalmente filtradas por estado.
- **Uso**: `python src/cli/main.py list [status]`
- **Argumentos**:
  - `status` (Opcional): Uno de `todo`, `in-progress`, `done`. Si no se provee, se muestran todas.
- **Salida de Éxito**: Tabla o lista tabulada con ID, Descripción, Estado y Fecha de Creación.
