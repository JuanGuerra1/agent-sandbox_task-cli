"""
conftest.py — inyecta el project root en sys.path para que
los tests puedan importar 'src.*' y los integration tests puedan
invocar 'python src/cli/main.py' desde el CWD correcto.
"""
import sys
from pathlib import Path

# Asegura que el root del proyecto esté en sys.path
PROJECT_ROOT = Path(__file__).parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
