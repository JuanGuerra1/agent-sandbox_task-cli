<!--
Sync Impact Report:
- Version change: [INITIAL] → 1.0.0
- List of modified principles: 
  - I. Disciplina de Gates (Capa 1/2/3) [NEW]
  - II. Arquitectura de Capas y Persistencia [NEW]
  - III. Validación de Modelos y Baseline [NEW]
  - IV. Trazabilidad vía Spec Kit [NEW]
  - V. Economía de Tokens y Presupuesto [NEW]
- Added sections: 
  - Stack Tecnológico y Persistencia
  - Workflow de Validación
- Removed sections: None
- Templates requiring updates:
  - .specify/templates/plan-template.md (✅ compatible)
  - .specify/templates/spec-template.md (✅ compatible)
  - .specify/templates/tasks-template.md (✅ compatible)
- Follow-up TODOs: None
-->

# task-cli-sandbox Constitution

## Core Principles

### I. Disciplina de Gates (Capa 1/2/3)
Respeto absoluto a la disciplina de gates definida en el Spec Kit. La Capa 1 (Gemini CLI) debe revisar y validar cada artefacto (spec, plan, tasks) antes de proceder a la siguiente fase. No se permite saltar el gate `clarify` incluso si la especificación parece clara.

### II. Arquitectura de Capas y Persistencia
Implementación de un CLI en Python para gestión de tareas (add, update, delete, list). La persistencia de datos debe realizarse exclusivamente en un archivo JSON local. La lógica de negocio debe estar desacoplada de la interfaz CLI para facilitar pruebas independientes.

### III. Validación de Modelos y Baseline
Uso mandatorio de Gemini 3 Flash como modelo por defecto para Antigravity. El escalado a modelos Pro (Low/High) solo se realizará según las reglas de oscilación firmadas en `baseline-modelos-google.md`. Se debe registrar el consumo de tokens y tiempo por cada fase.

### IV. Trazabilidad vía Spec Kit
Todo incremento de código debe estar respaldado por un artefacto de Spec Kit. Ningún cambio sistémico puede ser propuesto sin actualizar primero `spec.md`, `plan.md` o `tasks.md`. Los commits deben seguir la convención de Git de la Agencia.

### V. Economía de Tokens y Presupuesto
Mantenimiento del presupuesto estimado bajo $1.00 por sesión de validación. Optimización de prompts y respuestas para evitar relleno innecesario. Cada interacción debe ser concisa y técnica.

## Stack Tecnológico y Persistencia

Python 3.x para la lógica del CLI y gestión de archivos. JSON como formato de serialización para la base de datos local. Uso de `pytest` para la validación de contratos y lógica.

## Workflow de Validación

Ejecución end-to-end siguiendo el flujo: `/speckit.specify` → `/speckit.clarify` → [GATE 1] → `/speckit.plan` → [GATE 2] → `/speckit.tasks` → [GATE 3] → `/speckit.implement`. Cada gate requiere la aprobación explícita de Juan Guerra (simulado o real según el entorno).

## Governance

La constitución es la ley suprema de este sandbox de validación. Cualquier desviación de los principios debe ser documentada como una violación justificada en el `plan.md`. El GATE FINAL para cualquier merge a la rama principal es responsabilidad de Juan Guerra.

**Version**: 1.0.0 | **Ratified**: 2026-04-29 | **Last Amended**: 2026-04-29
