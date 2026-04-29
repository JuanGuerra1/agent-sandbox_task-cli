# Quickstart: task-cli-sandbox

## Requisitos Previos

- Python 3.10 o superior instalado.
- Entorno local donde se tenga permisos de escritura.

## Configuración

1. Clona o navega al repositorio.
2. No se requieren dependencias externas. Solo se utilizan librerías estándar de Python (`argparse`, `json`, `datetime`).

## Ejecución del CLI

Puedes ejecutar el CLI directamente llamando al script principal de Python. Opcionalmente, puedes crear un alias (por ejemplo en tu `.bashrc` o de PowerShell):

**Linux/macOS:**
```bash
alias task-cli='python3 src/cli/main.py'
```

**Windows (PowerShell):**
```powershell
Set-Alias -Name task-cli -Value "python src/cli/main.py"
```

## Ejemplos de Uso

**1. Añadir una tarea:**
```bash
task-cli add "Comprar leche"
```

**2. Listar todas las tareas:**
```bash
task-cli list
```

**3. Actualizar la descripción de una tarea (asumiendo ID 1):**
```bash
task-cli update 1 "Comprar leche de almendras"
```

**4. Marcar tarea en progreso:**
```bash
task-cli mark-in-progress 1
```

**5. Marcar tarea como completada:**
```bash
task-cli mark-done 1
```

**6. Listar tareas completadas:**
```bash
task-cli list done
```

**7. Eliminar una tarea:**
```bash
task-cli delete 1
```

## Pruebas (Test)

Para ejecutar las pruebas unitarias y de integración, instala `pytest`:

```bash
pip install pytest
pytest
```
