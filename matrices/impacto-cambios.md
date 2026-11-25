# Matriz de impacto de los cambios · v2.0

La versión indicada es la primera que incorporó cada cambio. El [registro de cambios](../docs/cambios.md) enlaza sus Issues y pull requests.

| Cambio | Versión de incorporación | Alcance y elementos afectados | Tiempo o esfuerzo | Efecto y verificación |
|---|---|---|---|---|
| [CR-001](../docs/cambios.md) · Motivo obligatorio en ajustes | v1.1 | RF-015, CU-006 y CLS-MovimientoInventario. El modelo incorpora `motivo` y `validarMotivo`, y `registrarAjuste` recibe el motivo. | La estimación original fue de 2 horas para actualizar la documentación y el modelo y revisar sus vínculos. | Guarda el ajuste, su motivo y el stock en una sola transacción. El alcance original pasó de 6 a 8 pruebas documentadas. PRU-016 a PRU-018 cubren la aceptación y el rechazo del motivo. |
| [CR-002](../docs/cambios.md) · Límites de concurrencia en Kanban | v2.0 | Cambia las reglas del equipo para iniciar, revisar y devolver tarjetas. En curso y En revisión admiten dos tarjetas cada una. | Si la columna de destino está llena, la tarjeta espera en su columna actual. El equipo prioriza liberar espacio antes de iniciar más trabajo. | Cada tarjeta bloqueada cuenta para su límite y las tarjetas terminadas conservan su evidencia. Las [reglas de concurrencia](../docs/agilidad.md#reglas-de-concurrencia) y el tablero permiten comprobar el cambio. |
| [CR-003](../docs/cambios.md) · Compra con recepción inmediata | v2.0 | RF-005, BR-004 y BR-008. CU-008 permite registrar la compra con la recepción y CU-009 cubre la entrada de existencias. | Cuando la mercadería ya llegó, la compra y la recepción se registran en el mismo formulario. Una orden pendiente se atiende al recibir la mercadería. | Compra, recepción y movimientos se guardan juntos. PRU-006 cubre la orden pendiente y su anulación. PRU-008 contempla la recepción inmediata, parcial, los rechazos por duplicación o exceso y el fallo de guardado. |
| [CR-004](../docs/cambios.md) · Comprobación de Yape y Plin | v2.0 | RF-001, BR-001 y CU-001. Exige el importe exacto y la confirmación manual del abono. | Humberto comprueba el abono antes de confirmar la venta. | PRU-020 documenta el rechazo de ventas con importe distinto o sin comprobación y el registro de la venta cuando se cumplen ambas condiciones. |

[Ver los riesgos y las medidas de respuesta](riesgos-cambios.md).
