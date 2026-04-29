# AGENTS.md — task-cli sandbox

> Workspace de validación de Antigravity como Capa 3 M1 (D15). Segundo Spec Kit de la Agencia.
> Reglas constitucionales globales: ver `cerebro-digital-spec/AGENTS.md` (heredadas).

---

## ⚠️ TIER 0 — Reglas heredadas del repo padre

Las **8 reglas constitucionales** de la Agencia viven en `cerebro-digital-spec/AGENTS.md`:

1. Etiquetas epistémicas obligatorias
2. GATE FINAL: Juan mergea PRs en GitHub
3. Lookup pre-prompt
4. Anti-sycophancy
5. Allow once durante Spec Kit
6. Reconexión de contexto al inicio de cada sesión
7. Co-creación con preguntas en puntos críticos
8. Verificar contratos firmados antes de proponer cambios sistémicos (incluye **política ASK**)

**Si este workspace está abierto solo (sin cerebro-digital-spec en el mismo workspace), abrir el archivo y leerlo antes de actuar.** Path canónico:

```
C:\Users\Personal\Documents\cerebro-digital-spec\AGENTS.md
```

---

## Identidad de este workspace

**Nombre:** task-cli-sandbox
**Propósito:** segundo Spec Kit de la Agencia, primer software real (CLI Python add/list/status/update/delete del curso SDD)
**Capa:** 3 M1 (Antigravity, validación D15)
**Modelos esperados:** Gemini 3.1 Pro (oscilación por fase, ver `cerebro-digital-spec/Referencias/baseline-modelos-google.md`)
**No es cliente:** es ejercicio de validación. Comparable a `agent-sandbox` pero en M1.

---

## Reglas específicas de este experimento

### Validación de D15

Este workspace **es el experimento de validación de D15** (Antigravity como Capa 3 M1). Por eso:

- Cada fase Spec Kit registra empíricamente: modelo usado, tokens, tiempo, retries, calidad 1-5 en la plantilla del baseline.
- Al cerrar, decidir si D15 se promueve a contrato firmado en `Metodología/` o se queda como decision_*.md.

### Modelo por defecto

**Gemini 3 Flash** como default model en Antigravity. Solo escalar a Pro Low/High según oscilación firmada en `baseline-modelos-google.md`.

### Spec Kit — invocación

Antigravity soporta Spec Kit nativamente vía:

- `/speckit.constitution` → `/speckit.specify` → `/speckit.clarify` → [GATE 1] → `/speckit.plan` → [GATE 2] → `/speckit.tasks` → `/speckit.analyze` → [GATE 3] → `/speckit.implement`
- Capa 2 (Gemini CLI Codebase Investigator) en cada gate
- GATE FINAL: Juan mergea PR en GitHub (TIER 0 #2)

Scaffolding requerido: `.agents/workflows/` (Antigravity) — instalar con CLI oficial Spec Kit con flag para `agy`.

### Capa 2 (Gemini CLI) en gates

Aplicar protocolo destilado en sesión T-85: Gemini CLI revisa cada gate con Generalist o Codebase Investigator antes de avanzar. No skippear `clarify` aunque la spec parezca clara.

### Permisos

**Allow once siempre.** Nunca Allow always. TIER 0 #5.

---

## Anclas a documentos del repo padre

- **Stack agentes:** `cerebro-digital-spec/AGENTS.md` (sección "Stack de agentes vigentes")
- **D15 (Antigravity):** `.claude/memory/decision_antigravity_capa3.md`
- **Baseline modelos:** `cerebro-digital-spec/Referencias/baseline-modelos-google.md`
- **Workflow Spec Kit:** `.claude/memory/methodology_speckit_workflow.md` + `cerebro-digital-spec/Referencias/protocolo-spec-kit-ejecucion.md` (pendiente destilar)
- **Handoff:** `.claude/memory/pattern_handoff_claude_antigravity.md`
- **Contrato diálogo:** `cerebro-digital-spec/Metodología/05. Contrato de diálogo.md`

---

## Fin del experimento

Al cerrar task-cli (PR mergeado por Juan):

1. Llenar plantilla de registro empírico en `baseline-modelos-google.md`
2. Decidir promoción D15 (firmar en `Metodología/` o seguir como memoria)
3. Destilar hallazgos a `protocolo-spec-kit-ejecucion.md` (junto con T-85)
4. Bitácora de sesión en `cerebro-digital-spec/Sesiones Claude Code/`

<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan:
C:\Users\Personal\Documents\agent-sandbox_task-cli\specs\001-task-cli-python\plan.md
<!-- SPECKIT END -->
