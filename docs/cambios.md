# Registro de cambios de Comercial Nazareth

| CR | Versión | Issue | PR | Evidencia |
|---|---|---|---|---|
| CR-001 · Motivo obligatorio en ajustes | v1.1 | [#8](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Definitivo/issues/8) | [#12](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Definitivo/pull/12) | [Comparación v1.0–v1.1](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Definitivo/compare/v1.0...v1.1), [reporte](../reportes/reporte-v1.1.md), [impacto](../matrices/impacto-cr-001.md) y [riesgos](../matrices/riesgos-cr-001.md). |
| CR-002 · Límites de concurrencia en Kanban | v2.0 | [#9](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Definitivo/issues/9) | [#13](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Definitivo/pull/13) | [Reglas del tablero y evidencias en Trello](agilidad.md#reglas-de-concurrencia). |
| CR-003 · Compra con recepción inmediata | v2.0 | [#10](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Definitivo/issues/10) | [#7](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Definitivo/pull/7) | [RF-005](SRS.md), [CU-008 y CU-009](CU.md) y [PRU-006 y PRU-008](../pruebas/pruebas.md). |
| CR-004 · Comprobación de Yape y Plin | v2.0 | [#11](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Definitivo/issues/11) | [#7](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Definitivo/pull/7) | [RF-001 y BR-001](SRS.md), [CU-001](CU.md) y [PRU-020](../pruebas/pruebas.md). |

El PR #7 sincronizó la documentación de compras y pagos. Los escenarios de prueba detallan los resultados esperados de ambos cambios.

## Impacto de compras y pagos

| CR | Alcance | Tiempo | Calidad y riesgo |
|---|---|---|---|
| CR-003 | CU-008 permite registrar la recepción al guardar una compra. CU-009 cubre la entrada de existencias. | La compra recibida se registra en el mismo formulario. La orden pendiente se atiende cuando llega la mercadería. | Guardar compra, recepción y movimientos en una transacción evita ingresos parciales. PRU-008 cubre además una referencia duplicada y el exceso de unidades. |
| CR-004 | La venta con Yape o Plin exige el importe exacto y la comprobación manual del abono. | Humberto comprueba el abono antes de confirmar la venta. | PRU-020 comprueba que la operación rechace la falta de confirmación o un importe distinto y que conserve el método al guardar. |
