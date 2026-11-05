# Comercial Nazareth: entrega definitiva

Grupo 4 · Ingeniería de Software

Sistema de gestión comercial y portal de clientes de Comercial Nazareth. Esta entrega integra la sesión 12 y la evolución hasta v2.0.1 e incorpora el SRS completo, los ocho casos de uso y el flujo del proceso crítico CU-006: Gestionar inventario.

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
| [Convención de identificadores](docs/convencion-ids.md) | Identificadores y correspondencia con el proyecto de origen. |
| [Matriz de trazabilidad](matrices/trazabilidad.md) | Vínculos de los 15 requisitos funcionales y los 6 no funcionales. |
| [Pruebas de la línea base](pruebas/pruebas.md) | Nueve casos documentados. |
| [Hoja de trazabilidad](reportes/trazabilidad-s12.xlsx) | Cobertura calculada a partir de los vínculos de la matriz. |
| [Agilidad y concurrencia](docs/agilidad.md) | Kanban, límites de dos tarjetas por etapa y evidencias del flujo de V2. |
| [Reporte v1.1](reportes/reporte-v1.1.md) | Comparación histórica entre v1.0 y v1.1. |

## Modelos

| Modelo | Visualización | Fuente editable |
|---|---|---|
| Casos de uso del sistema | [PNG](modelos/casos-de-uso.png) | Diagrama conservado del proyecto de origen. |
| Clases del alcance seleccionado | [PNG](modelos/clases.png) | [draw.io](modelos/clases.drawio) |
| Flujo de CU-006: Gestionar inventario | [PNG](modelos/actividad-gestionar-inventario.png) | [draw.io](modelos/actividad-gestionar-inventario.drawio) · [XML](modelos/actividad-gestionar-inventario.xml) |

## Alcance de la trazabilidad

La [matriz](matrices/trazabilidad.md) enumera los 15 requisitos funcionales y los 6 no funcionales del SRS. Las nueve pruebas de [pruebas.md](pruebas/pruebas.md) se vinculan con cinco requisitos funcionales. El modelo de clases conserva seis clases de la línea base y también se vincula con esos cinco requisitos. La hoja de cálculo muestra las relaciones registradas y los totales resultantes.

CU-006 incorpora CR-001: cada ajuste manual requiere un motivo válido y conserva el ajuste, el motivo y el stock en una misma transacción. El flujo de esta entrega desarrolla ese proceso y su relación con la reposición.

## Sesión 12

- [Impacto de CR-001](matrices/impacto-cr-001.md): alcance, tiempo y calidad/costo.
- [Riesgos de CR-001](matrices/riesgos-cr-001.md): probabilidad, impacto y respuesta.
- [Resumen de trazabilidad](reportes/trazabilidad-s12.md) y [hoja de cálculo](reportes/trazabilidad-s12.xlsx): catálogo completo y cobertura documental.

## Kanban

[Tablero de Comercial Nazareth](https://trello.com/b/9LEaT3KG/comercial-nazareth-kanban-v2). En curso y En revisión admiten un máximo de dos tarjetas cada una. Las reglas contemplan capacidad, bloqueos, correcciones y criterios de cierre.

## Antecedentes

- [Integración histórica de Lab7 y V2.0.1](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Definitivo/pull/1).
- [Adaptación ágil inicial](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Lab7_V2/pull/1).
- [Reglas de concurrencia](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Lab7_V2/pull/2).
- [Línea base v1.0](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Lab7_V2/tree/v1.0).
- [Línea base v1.1](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Lab7_V2/tree/v1.1).
- [Reporte histórico v1.1](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Lab7_V2/blob/v1.1/reportes/reporte-v1.1.md).
- [Base v2.0.1](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Lab7_V2/tree/v2.0.1).
- [Repositorio del proyecto de origen](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth).
- [Repositorio del laboratorio 7](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Lab7).
- [CR-001](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Lab7/issues/5).
