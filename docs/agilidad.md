# Gestión del trabajo en Comercial Nazareth

El tablero organiza cambios pequeños con criterios de aceptación, límites de trabajo en curso y revisión de vínculos entre requisitos y pruebas.

## 1. Trabajo con agilidad

Los identificadores permiten dividir una mejora y seguir sus efectos sin rehacer todos los documentos. La matriz muestra qué requisito, caso de uso, clase y prueba se relacionan. Los cambios pueden revisarse en una rama y entregarse mediante un PR.

En Comercial Nazareth, la regla de registrar un motivo en los ajustes manuales pertenece a RF-015 y CU-006. Esa relación permite ampliar una prueba concreta conservando las reglas de ventas, catálogo y clientes. La documentación se actualiza junto con el incremento para mantener la trazabilidad.

## 2. Prácticas aplicadas

El tablero reúne 16 tarjetas ordenadas por versión. Cada tarjeta indica el criterio de aceptación y enlaza el documento, Issue o pull request que respalda el trabajo registrado.

Se limita el trabajo a dos tarjetas en En curso y dos en En revisión. Al revisar se comprueban el alcance, los identificadores, los enlaces y los resultados esperados. Una corrección devuelve la tarjeta a En curso cuando hay capacidad. El cierre exige comprobar los criterios y conservar su evidencia.

## 3. Kanban en Trello

[Tablero Kanban de Comercial Nazareth · Miércoles](https://trello.com/b/pG8s0HQ8/comercial-nazareth-mi%C3%A9rcoles).

| Estado | Límite | Regla de trabajo |
|---|---|---|
| Por hacer | Sin límite de concurrencia | Tarjetas priorizadas y con criterios de aceptación definidos; trabajo no iniciado. |
| En curso | 2 tarjetas | Iniciar una tarea cuando haya espacio y capacidad para atenderla. |
| En revisión | 2 tarjetas | Contrastar el cambio con sus criterios, la trazabilidad y el SRS. |
| Terminado | Sin límite de concurrencia | Criterios comprobados y evidencias enlazadas; trabajo cerrado. |

### Reglas de concurrencia

El [CR-002](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Definitivo/issues/9) fija dos tarjetas En curso y dos En revisión. Cada columna aplica su propio límite. Una tarjeta cuenta una vez, aunque colaboren varios integrantes.

| Situación | Qué hace el equipo |
|---|---|
| En curso tiene dos tarjetas y se quiere iniciar otra | La tarjeta sigue en Por hacer. El equipo prioriza terminar, revisar o desbloquear las que ya empezó. |
| En revisión tiene dos tarjetas | El trabajo que espera revisión sigue En curso y cuenta en esa etapa. |
| Una tarjeta está bloqueada | Permanece en su columna y cuenta para el límite. Se registra qué la bloquea y qué hace falta para resolverlo. |
| Una revisión requiere correcciones | La tarjeta vuelve a En curso cuando hay espacio. Mientras espera, cuenta en En revisión. |
| Se cumplen los criterios de aceptación | La tarjeta pasa a Terminado con la evidencia enlazada. |

El equipo comprueba el espacio de destino antes de mover una tarjeta. Los límites se muestran en los nombres de las columnas y los criterios se detallan en la [tarjeta del CR-002](https://trello.com/c/M6iVRmxI).

## 4. Seguimiento por versión

| Versión | Tarjetas de referencia |
|---|---|
| v1.0 | [Línea base de requisitos y trazabilidad](https://trello.com/c/239z6Ncn) |
| v1.1 | [CR-001 · Ajustes de inventario](https://trello.com/c/O96QYyu5) y [escenarios de prueba del ajuste](https://trello.com/c/I3ru0jJN) |
| v2.0 | [CR-002 · Límites de Kanban](https://trello.com/c/M6iVRmxI), [CR-003 · Recepción de compras](https://trello.com/c/0V5FRS9T), [CR-004 · Comprobación de pagos](https://trello.com/c/g6LkA2D5) y [cierre de la entrega](https://trello.com/c/59h7x7Eh) |

Las tarjetas de Terminado registran trabajo respaldado por artefactos del repositorio. Por ejemplo, la [tarjeta de PRU-019](https://trello.com/c/pIMnZu8w) remite al escenario de fallo de guardado de un ajuste manual. La [prueba](../pruebas/pruebas.md) describe el resultado esperado y la [matriz](../matrices/trazabilidad.md) la vincula con RF-015.

El alcance y los riesgos del CR-002 se detallan en las [matrices de impacto](../matrices/impacto-cambios.md) y [riesgos](../matrices/riesgos-cambios.md).
