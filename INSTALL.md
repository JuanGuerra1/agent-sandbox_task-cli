# INSTALL.md — Setup técnico task-cli sandbox

> Pasos verificables antes de invocar el primer `/speckit.*` en Antigravity.

## Pre-requisitos en M1 (Windows)

| Item | Comando de verificación | Estado esperado |
|---|---|---|
| Python ≥ 3.10 | `python --version` | 3.10+ |
| Node.js ≥ 20 (para Spec Kit CLI si usa npm) | `node --version` | v20+ |
| Git | `git --version` | cualquier versión moderna |
| GitHub CLI | `gh --version` | autenticado en `JuanGuerra1` |
| Antigravity | Abierto en M1 | Pro $20/mes activo |
| Gemini CLI | `gemini --version` | v0.39.1+ |
| Claude Code | `claude --version` | activo (M1) |

## Verificación de Antigravity

Antes de empezar, verificar en Antigravity:

1. **Settings → Models** → confirmar que **Gemini 3 Flash** está seleccionado como default
2. **Settings → Models → AI Credit Overages** → ON (para no quedarse sin cuota a mitad de implement)
3. **AI Credits disponibles** → 1000 (default Pro)
4. **Workspaces cargados** → agregar `task-cli-sandbox` (cuando exista)

## Instalación de Spec Kit oficial

**[hecho]** Comando verificado 2026-04-29 — gap cerrado:

```powershell
# Requiere: Python 3.11+ y uv instalado
# Ejecutar desde cualquier directorio (NO desde dentro del target)

$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONUTF8 = "1"
uvx --from git+https://github.com/github/spec-kit.git specify init <NOMBRE-O-PATH-DESTINO> --integration agy --force

# Ejemplo para inicializar en directorio ya existente:
uvx --from git+https://github.com/github/spec-kit.git specify init "C:\Users\Personal\Documents\agent-sandbox_task-cli" --integration agy --force
```

> **Nota encoding:** `PYTHONIOENCODING=utf-8` es obligatorio en Windows — sin él el instalador falla con UnicodeEncodeError en cp1252.

> **Nota `--force`:** necesario si el directorio ya existe (con archivos). Sin `--force`, el instalador aborta.

> **Nota integración:** el flag correcto es `--integration agy` (no `--agent agy`). El instalador escoge automáticamente PowerShell como tipo de scripts en Windows.

Tras instalación exitosa, la estructura real creada es:

```
agent-sandbox_task-cli/
├── AGENTS.md                          ← plantilla de la Agencia (copiada antes)
├── INSTALL.md                         ← este archivo
├── README.md                          ← plantilla de la Agencia
├── .antigravityignore                 ← plantilla de la Agencia
├── .agents/
│   └── skills/
│       ├── speckit-constitution/SKILL.md
│       ├── speckit-specify/SKILL.md
│       ├── speckit-clarify/SKILL.md
│       ├── speckit-plan/SKILL.md
│       ├── speckit-tasks/SKILL.md
│       ├── speckit-analyze/SKILL.md
│       ├── speckit-implement/SKILL.md
│       ├── speckit-checklist/SKILL.md
│       ├── speckit-taskstoissues/SKILL.md
│       ├── speckit-git-commit/SKILL.md
│       ├── speckit-git-feature/SKILL.md
│       ├── speckit-git-initialize/SKILL.md
│       ├── speckit-git-remote/SKILL.md
│       └── speckit-git-validate/SKILL.md
└── .specify/
    ├── memory/constitution.md         ← vacío hasta @speckit-constitution
    ├── templates/
    │   ├── constitution-template.md
    │   ├── spec-template.md
    │   ├── plan-template.md
    │   ├── tasks-template.md
    │   └── checklist-template.md
    ├── extensions/git/                ← scripts PowerShell + bash para git
    ├── integrations/agy.manifest.json
    └── workflows/speckit/workflow.yml
```

> **Diferencia vs T-85 (agent-sandbox):** Antigravity usa **skills** (`@speckit-*` invocables en chat) en lugar de slash commands (`/speckit.*`). La invocación en el TUI es distinta — ver §"Verificación de comandos" abajo.

## Verificación de comandos Spec Kit en Antigravity

Una vez instalado e iniciado el workspace en Antigravity:

1. Abrir Antigravity → **File → Open Folder** → seleccionar `agent-sandbox_task-cli`
2. En el chat, escribir `@` y verificar autocomplete
3. Debe aparecer la lista de skills: `@speckit-constitution`, `@speckit-specify`, `@speckit-clarify`, `@speckit-plan`, `@speckit-tasks`, `@speckit-analyze`, `@speckit-implement`, `@speckit-checklist`
4. **Modelo recomendado por fase** → ver `cerebro-digital-spec/Referencias/baseline-modelos-google.md`

> **Diferencia importante vs agent-sandbox:** en Antigravity las skills se invocan con `@` (no con `/`). El TUI de opencode usaba `/speckit.*` — Antigravity usa `@speckit-*`.

Si no aparecen en autocomplete → revisar que `.agents/skills/` contiene los directorios correctos y reiniciar Antigravity.

## Gemini CLI en M1

Verificar que Gemini CLI tiene acceso al workspace:

```bash
cd task-cli-sandbox
gemini --version
gemini -p "lista archivos de este directorio" --output-format json
```

Debe responder con la lista de archivos del workspace en JSON.

## Test de TIER 0 cross-stack (validación previa)

Antes de empezar Spec Kit, validar que Antigravity lee `AGENTS.md`:

1. Abrir Antigravity en el workspace
2. Seleccionar Gemini 3 Flash
3. Prompt:
   ```
   Lee AGENTS.md y cerebro-digital-spec/AGENTS.md (si está accesible).
   Cita las 8 reglas TIER 0.
   ```
4. **Test de éxito:** el agente cita las 8 reglas con etiquetas `[hecho]`/`[hipótesis]` correctamente.
5. **Si falla:** reorganizar workspace (multi-root) o copiar `cerebro-digital-spec/AGENTS.md` al workspace task-cli.

## Próximo paso post-setup

Si todo verifica → invocar `/speckit.constitution` con prompt similar a T-85, adaptado a task-cli.
