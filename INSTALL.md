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

**[gap]** Verificar comando exacto en docs oficiales antes de ejecutar:

- https://github.com/github/spec-kit
- https://codelabs.developers.google.com/codelabs/getting-started-with-spec-driven-development-in-antigravity

Comandos candidatos (el correcto depende de versión de Spec Kit a abril 2026):

```bash
# Opción A — vía uvx (Python)
uvx spec-kit init --agent agy

# Opción B — vía npm
npx @github/spec-kit init --agent agy

# Opción C — clonar + setup local
git clone https://github.com/github/spec-kit.git temp-speckit
cd temp-speckit
./scripts/install-agy.sh
```

Tras instalación exitosa, debe existir:

```
task-cli-sandbox/
├── .agents/
│   └── workflows/
│       ├── speckit.constitution.yml (o .md)
│       ├── speckit.specify.yml
│       ├── speckit.clarify.yml
│       ├── speckit.plan.yml
│       ├── speckit.tasks.yml
│       ├── speckit.analyze.yml
│       ├── speckit.implement.yml
│       └── speckit.checklist.yml
└── .specify/
    └── memory/
        └── constitution.md (vacío hasta /speckit.constitution)
```

## Verificación de comandos Spec Kit en Antigravity

Una vez instalado:

1. Abrir Antigravity con el workspace `task-cli-sandbox`
2. En el TUI, escribir `/` y verificar autocomplete
3. Debe aparecer: `/speckit.constitution`, `/speckit.specify`, `/speckit.clarify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.analyze`, `/speckit.implement`, `/speckit.checklist`
4. Adicional: skills `@speckit.*` invocables directamente

Si no aparecen → revisar `.agents/workflows/` y reinstalar Spec Kit.

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
