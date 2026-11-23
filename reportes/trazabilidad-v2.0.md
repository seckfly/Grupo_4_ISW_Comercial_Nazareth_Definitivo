# Trazabilidad de Comercial Nazareth · v2.0

La [matriz](../matrices/trazabilidad.md) reúne los 15 RF, los seis RNF y las ocho reglas del [SRS](../docs/SRS.md). La [hoja de cálculo](trazabilidad-v2.0.xlsx) calcula los totales y comprueba los vínculos con [pruebas.md](../pruebas/pruebas.md).

| Medida | Resultado |
|---|---:|
| RF con prueba documentada | 15 de 15 |
| RNF con prueba documentada | 6 de 6 |
| Reglas del negocio con prueba vinculada | 8 de 8 |
| Casos de uso documentados | 8 |
| Clases del modelo | 6 |
| RF vinculados con el modelo de clases | 5 de 15 |
| Casos de prueba documentados | 23 |

Las pruebas registran escenarios y resultados esperados. La cobertura de pruebas se calcula sobre vínculos documentales; la ejecución de los casos se registra por separado cuando corresponda.

## Trazabilidad de los cambios

| CR | Versión de incorporación | Requisito, proceso o regla | Evidencia de verificación |
|---|---|---|---|
| CR-001 · Motivo obligatorio en ajustes | v1.1 | REQ-015, identificado como RF-015 en v2.0, [CU-006](../docs/CU.md#cu-006-gestionar-inventario) y CLS-MovimientoInventario. La matriz de v2.0 también vincula RF-015 con CLS-Producto. | [PRU-016 a PRU-018](../pruebas/pruebas.md) documentan el motivo válido, vacío y formado solo por espacios. La v2.0 añade PRU-019, que cubre el fallo de guardado. |
| CR-002 · Límites de concurrencia en Kanban | v2.0 | [Reglas de movimiento y capacidad](../docs/agilidad.md#reglas-de-concurrencia). En curso y En revisión admiten dos tarjetas cada una, incluidas las bloqueadas. | [Acuerdo de las reglas](https://trello.com/c/rCAaVxzg) y [aplicación de los límites](https://trello.com/c/loubRJnf) en Trello. La evidencia corresponde al proceso del equipo. |
| CR-003 · Compra con recepción inmediata | v2.0 | RF-005, BR-004 y BR-008, [CU-008](../docs/CU.md#cu-008-registrar-orden-de-compra) y [CU-009](../docs/CU.md#cu-009-gestionar-compras-recepción-de-mercadería). | [PRU-006 y PRU-008](../pruebas/pruebas.md) describen la orden pendiente, la recepción inmediata y parcial y el rechazo de referencias repetidas o cantidades mayores al saldo. |
| CR-004 · Comprobación de Yape y Plin | v2.0 | RF-001, BR-001 y [CU-001](../docs/CU.md#cu-001-registrar-venta). | [PRU-020](../pruebas/pruebas.md) documenta el importe exacto, la comprobación manual del abono y los rechazos correspondientes. |

La columna «Último CR» de la [matriz de trazabilidad](../matrices/trazabilidad.md#requisitos-funcionales) relaciona RF-015, RF-005 y RF-001 con sus cambios. PRU-006 complementa al CR-003 con el escenario de orden pendiente, vinculado a RF-004. El CR-002 se sigue desde las tarjetas del tablero y las reglas de concurrencia.

[Registro de cambios](../docs/cambios.md) · [Matriz de impacto](../matrices/impacto-cambios.md) · [Matriz de riesgos](../matrices/riesgos-cambios.md)
