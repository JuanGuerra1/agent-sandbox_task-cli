# task-cli sandbox

Workspace de validación de **Antigravity como Capa 3 M1** (D15, firmada 2026-04-28).

Segundo Spec Kit de la Agencia. Primer software real (vs T-85 que fue investigación).

---

## Qué se construye

CLI Python con 5 comandos: `add`, `list`, `status`, `update`, `delete`.

Ejercicio del curso SDD. Tres user stories independientes (US1, US2, US3) que se pueden implementar y validar por separado.

---

## Por qué este workspace existe

1. **Validar D15** — primer experimento de Antigravity como Capa 3 ejecutora en M1
2. **Calibrar baseline de modelos** — llenar `cerebro-digital-spec/Referencias/baseline-modelos-google.md` con datos reales por fase Spec Kit
3. **Validar protocolo handoff** — primera oportunidad de probar relevo Claude Code ↔ Antigravity en feature real
4. **Generar evidencia para firmar `Metodología/07. Método de entrega a clientes`** — sin task-cli no hay contrato comercial

---

## Stack del experimento

| Capa | Agente | Modelo |
|---|---|---|
| **1 — Estratega / PO** | Claude Code (M1) | Anthropic Pro |
| **2 — Consultor en gates** | Gemini CLI (M1) | Auto (Gemini 3) |
| **3 — Ejecutor agéntico** | Antigravity (M1) | Gemini 3.1 Pro (oscilación por fase) |

---

## Reglas del experimento

Ver `AGENTS.md` (en este workspace) y `cerebro-digital-spec/AGENTS.md` (TIER 0 global).

Reglas críticas:
- **Allow once siempre** durante Spec Kit
- **GATE FINAL = Juan mergea** en GitHub
- **Default model = Flash**, escalar a Pro Low/High según `baseline-modelos-google.md`
- **Capa 2 (Gemini CLI) revisa cada gate** antes de avanzar

---

## Setup desde cero (instrucciones para Juan)

### 1. Crear este workspace

```bash
# Decidir ubicación, ejemplo:
cd C:\Users\Personal\Documents\
mkdir task-cli-sandbox
cd task-cli-sandbox
```

### 2. Inicializar Git

```bash
git init
git branch -M main
```

### 3. Copiar plantillas desde cerebro-digital-spec

Copia estos archivos a la raíz del nuevo workspace:

```
cerebro-digital-spec/setup-templates/task-cli/AGENTS.md       → ./AGENTS.md
cerebro-digital-spec/setup-templates/task-cli/.antigravityignore → ./.antigravityignore
cerebro-digital-spec/setup-templates/task-cli/README.md       → ./README.md
```

### 4. Instalar Spec Kit con flag Antigravity

Verificar primero comando exacto en docs oficiales:

```bash
# Comando esperado (verificar en https://github.com/github/spec-kit):
spec-kit init --agent agy

# O si requiere uvx/python:
uvx spec-kit init --agent agy
```

Esto crea `.agents/workflows/` con los slash commands `/speckit.*`.

### 5. Crear repo en GitHub (privado)

```bash
gh repo create JuanGuerra1/task-cli-sandbox --private --source=. --remote=origin
git add AGENTS.md .antigravityignore README.md .agents/
git commit -m "spec: setup task-cli sandbox para validación D15 Antigravity"
git push -u origin main
```

### 6. Abrir en Antigravity

- Abrir Antigravity
- File → Open Workspace → seleccionar `task-cli-sandbox/`
- O agregar al workspace existente `agencia-ia.code-workspace` (recomendado para que Antigravity vea también `cerebro-digital-spec/`)

### 7. Configurar modelo default

Settings → Models → Default model: **Gemini 3 Flash**

### 8. Comenzar Spec Kit

Primer prompt al agente:

```
Lee AGENTS.md (de este workspace) y cerebro-digital-spec/AGENTS.md (TIER 0 global).
Reporta qué entiendes del experimento antes de invocar /speckit.constitution.
```

Después: `/speckit.constitution` → flujo completo Spec Kit con gates.

---

## Registro empírico

Mientras se ejecuta cada fase, llenar la plantilla de `cerebro-digital-spec/Referencias/baseline-modelos-google.md`. Datos a capturar por fase:
- Modelo usado
- Tokens consumidos
- Tiempo de pared
- Retries
- Calidad subjetiva 1-5
- Hallazgos

---

## Al cerrar el experimento

1. Llenar baseline empírico completo
2. Bitácora de sesión en `cerebro-digital-spec/Sesiones Claude Code/Sesion YYYY-MM-DD - task-cli en Antigravity.md`
3. Decidir promoción D15:
   - Si funcionó bien → firmar en `Metodología/` (07 ampliado o nuevo 08)
   - Si no funcionó → mantener D15 como decision_*.md y reevaluar
4. Destilar hallazgos al protocolo Spec Kit (junto con T-85)
5. PR a `cerebro-digital-spec` con cambios derivados (baseline llenado, hallazgos, etc.)
