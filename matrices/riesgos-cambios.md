# Matriz de riesgos de los cambios · v2.0

La probabilidad y el impacto son estimaciones cualitativas en una escala de baja, media y alta. El [registro de cambios](../docs/cambios.md) enlaza la evidencia de cada CR.

| ID | CR asociado | Riesgo | Probabilidad | Impacto | Prevención | Contingencia |
|---|---|---|---|---|---|---|
| R-01 | CR-001 | Se actualiza el stock sin conservar el motivo del ajuste. | Media | Alta | Guardar ajuste, motivo y stock en una sola transacción. Revisar PRU-016 y el escenario de fallo de PRU-019. | Revertir el intento y comprobar que el historial y el stock conservan el estado anterior. |
| R-02 | CR-001 | Se acepta un motivo vacío o compuesto solo por espacios. | Media | Media | Validar el motivo antes de guardar. Revisar PRU-017 y PRU-018. | Rechazar el ajuste y solicitar un motivo válido antes de volver a ingresarlo. |
| R-03 | CR-001 | La validación del motivo afecta las salidas de stock generadas por ventas. | Baja | Alta | Aplicar la validación en CU-006. Usar PRU-001 para revisar la salida por venta. | Corregir la regla aplicada al flujo de ventas y repetir la comprobación. |
| R-04 | CR-001 | La actualización documental supera las dos horas estimadas. | Media | Media | Revisar los artefactos enlazados a RF-015 y comprobar sus IDs. | Revisar el esfuerzo y ajustar la planificación antes de cerrar la revisión. |
| R-05 | CR-002 | Una columna supera dos tarjetas al mover otra o al dejar fuera del conteo una tarjeta bloqueada. | Media | Media | Contar las tarjetas de la columna de destino antes de mover una, incluidas las bloqueadas. | Detener nuevos movimientos hacia esa columna y resolver el bloqueo o completar una tarjeta para liberar espacio. |
| R-06 | CR-002 | Una tarjeta pasa a Terminado sin la evidencia de sus criterios de aceptación. | Media | Media | Revisar los criterios y sus enlaces antes de cerrar la tarjeta. | Devolverla a revisión cuando haya espacio y completar la evidencia. |
| R-07 | CR-003 | Una orden pendiente incrementa existencias o una compra con recepción inmediata queda guardada parcialmente. | Media | Alta | Vincular el incremento a la recepción y guardar en una sola transacción la compra, la recepción y sus movimientos cuando la mercadería ya llegó. Revisar la orden pendiente en PRU-006 y el fallo de la recepción inmediata en PRU-008. | Verificar que la orden pendiente conserve el stock. Ante un fallo de la compra con recepción inmediata, comprobar que se reviertan la compra, la recepción y los movimientos y que el stock quede intacto. |
| R-08 | CR-003 | Una recepción duplica una entrada o supera el saldo de la orden. | Media | Alta | Validar la referencia y la cantidad contra el saldo. Revisar PRU-008. | Rechazar la recepción y contrastar la referencia, el saldo y los movimientos previos. |
| R-09 | CR-004 | Se registra una venta con un importe incorrecto o sin comprobar el abono. | Media | Alta | Exigir el total exacto y la confirmación manual. Revisar PRU-020. | Detener el registro de la venta y verificar el importe y el abono antes de volver a intentarlo. |
| R-10 | CR-004 | El QR de demostración se interpreta como un comprobante de pago. | Media | Media | Identificar el QR como demostración y comprobar el abono de forma manual. Revisar PRU-020. | Verificar el abono antes de confirmar la venta y aclarar el uso del QR. |

[Ver el alcance y la verificación de cada cambio](impacto-cambios.md).
