# Comercial Nazareth: entrega definitiva

Grupo 4 · Ingeniería de Software

Sistema de gestión comercial y portal de clientes de Comercial Nazareth. El repositorio reúne el SRS completo, los ocho casos de uso, las pruebas del catálogo y el flujo de CU-006: Gestionar inventario.

## Integrantes

| Integrante | Código |
|---|---|
| Marco Antonio Martell Alvarez | N00471929 |
| Alejandro Horna Quezada | N00475530 |
| Isaí Samuel Bejarano Benites | N00490010 |
| Cesar Jeremin Alonso Chuquimango Reyes | N00480808 |
| Alonso Castillo Davalos | N00491764 |


## Documentos

| Documento | Contenido |
|---|---|
| [SRS completo](docs/SRS.md) | Quince requisitos funcionales, seis no funcionales y ocho reglas del negocio. |
| [Casos de uso](docs/CU.md) | Ocho casos de uso, sus actores, flujos y excepciones. |
| [Proceso crítico](docs/proceso-critico.md) | Justificación y flujo de CU-006, con los controles del ajuste manual. |
| [Convención de identificadores](docs/convencion-ids.md) | Identificadores usados en SRS, casos de uso, modelo y pruebas. |
| [Matriz de trazabilidad](matrices/trazabilidad.md) | Vínculos de los 15 requisitos funcionales y los 6 no funcionales. |
| [Pruebas](pruebas/pruebas.md) | Veintitrés casos documentados, incluidos los escenarios de CR-001. |
| [Hoja de trazabilidad](reportes/trazabilidad-s12.xlsx) | Cobertura calculada a partir de los vínculos de la matriz. |
| [Agilidad y concurrencia](docs/agilidad.md) | Kanban, límites de dos tarjetas por etapa y evidencias del flujo de V2. |
| [Reporte v1.1](reportes/reporte-v1.1.md) | Comparación histórica entre v1.0 y v1.1. |

## Modelos

| Modelo | Visualización | Fuente editable |
|---|---|---|
| Casos de uso del sistema | [PNG](modelos/casos-de-uso.png) | Diagrama de los ocho casos de uso. |
| Clases del alcance seleccionado | [PNG](modelos/clases.png) | [draw.io](modelos/clases.drawio) |
| Flujo de CU-006: Gestionar inventario | [PNG](modelos/actividad-gestionar-inventario.png) | [draw.io](modelos/actividad-gestionar-inventario.drawio) · [XML](modelos/actividad-gestionar-inventario.xml) |

## Alcance de la trazabilidad

La [matriz](matrices/trazabilidad.md) reúne los 15 RF, los seis RNF y las ocho reglas del negocio del SRS. Los 23 casos de [pruebas.md](pruebas/pruebas.md) cubren el catálogo de requisitos. El modelo disponible tiene seis clases vinculadas con cinco RF. La [hoja de cálculo](reportes/trazabilidad-s12.xlsx) calcula la cobertura y comprueba los vínculos entre requisitos y pruebas.

CU-006 incorpora CR-001: cada ajuste manual requiere un motivo válido y conserva el ajuste, el motivo y el stock en una misma transacción. El flujo de esta entrega desarrolla ese proceso y su relación con la reposición.

## Sesión 12

- [Impacto de CR-001](matrices/impacto-cr-001.md): alcance, tiempo y calidad/costo.
- [Riesgos de CR-001](matrices/riesgos-cr-001.md): probabilidad, impacto y respuesta.
- [Resumen de trazabilidad](reportes/trazabilidad-s12.md) y [hoja de cálculo](reportes/trazabilidad-s12.xlsx): catálogo completo y cobertura documental.

## Kanban

[Tablero de Comercial Nazareth](https://trello.com/b/9LEaT3KG/comercial-nazareth-kanban-v2). En curso y En revisión admiten un máximo de dos tarjetas cada una. Las reglas contemplan capacidad, bloqueos, correcciones y criterios de cierre.

