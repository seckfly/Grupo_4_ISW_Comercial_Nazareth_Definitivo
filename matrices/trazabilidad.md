# Matriz de trazabilidad de Comercial Nazareth

La matriz reúne los 15 requisitos funcionales, los seis no funcionales y las ocho reglas del [SRS](../docs/SRS.md). Los casos de uso están en [CU.md](../docs/CU.md); el modelo disponible y las [pruebas](../pruebas/pruebas.md) aportan los demás vínculos. Las pruebas describen escenarios y resultados esperados.

## Requisitos funcionales

| ID | Requisito | Caso de uso o ámbito | Clase del modelo | Pruebas documentadas | Último CR |
|---|---|---|---|---|---|
| RF-001 | Registrar venta | CU-001 | CLS-Venta, CLS-DetalleVenta, CLS-Producto, CLS-MovimientoInventario | PRU-001, PRU-003, PRU-020 | [CR-004](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Definitivo/issues/11) |
| RF-002 | Consultar existencias y alertas | CU-006 | CLS-Producto | PRU-002 | — |
| RF-003 | Identificar proveedor de la orden | CU-008 | — | PRU-005 | — |
| RF-004 | Registrar orden de compra | CU-008, CU-009 | — | PRU-006 | — |
| RF-005 | Registrar recepción | CU-009 y CU-008 (recepción inmediata) | — | PRU-008 | [CR-003](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Definitivo/issues/10) |
| RF-006 | Acceder según perfil | Acceso transversal | — | PRU-009 | — |
| RF-007 | Consultar catálogo | CU-003; también CU-001, CU-005 y CU-008 | CLS-Producto, CLS-ListaProductos, CLS-Cliente | PRU-007 | — |
| RF-008 | Gestionar promociones | CU-004 | — | PRU-010 | — |
| RF-009 | Solicitar separación | CU-005 | — | PRU-011 | — |
| RF-010 | Vincular cliente a la venta | CU-002; extiende CU-001 | CLS-Cliente, CLS-Venta | PRU-004 | — |
| RF-011 | Consultar clientes frecuentes | Consulta administrativa | — | PRU-012 | — |
| RF-012 | Consultar resumen y reportes | Consulta administrativa | — | PRU-013 | — |
| RF-013 | Administrar accesos | Acceso transversal | — | PRU-014 | — |
| RF-014 | Consultar cuenta y beneficios | Portal de clientes | — | PRU-015 | — |
| RF-015 | Mantener productos e inventario | CU-006 | CLS-Producto, CLS-MovimientoInventario | PRU-016, PRU-017, PRU-018, PRU-019 | [CR-001](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Definitivo/issues/8) |

## Requisitos no funcionales

| ID | Requisito | Ámbito | Prueba documentada |
|---|---|---|---|
| RNF-001 | Rapidez de registro | CU-001 | PRU-021 |
| RNF-002 | Separación de perfiles | Acceso transversal | PRU-009 |
| RNF-003 | Tiempo de consulta | Consultas de productos, stock y resumen | PRU-022 |
| RNF-004 | Integridad de venta | CU-001 | PRU-001 |
| RNF-005 | Consistencia monetaria | CU-001 | PRU-003 |
| RNF-006 | Respaldo recuperable | Respaldo de datos | PRU-023 |

## Reglas del negocio

| ID | Regla verificada | Pruebas documentadas |
|---|---|---|
| BR-001 | Yape y Plin con importe exacto y comprobación manual | PRU-020 |
| BR-002 | Precio y redondeo; descuento concordante | PRU-003, PRU-010 |
| BR-003 | Venta sin cliente asociado | PRU-004 |
| BR-004 | El stock aumenta al confirmar la recepción | PRU-006, PRU-008 |
| BR-005 | Separación sin venta ni bloqueo de existencias | PRU-011 |
| BR-006 | Alerta por umbral y decisión de reponer | PRU-002, PRU-006 |
| BR-007 | Proveedor guardado en la orden | PRU-005 |
| BR-008 | Recepción parcial y rechazo de duplicados o exceso | PRU-008 |

## Lectura de la matriz

Los 15 RF y los seis RNF tienen al menos un caso de prueba documentado. Los ocho casos de uso y las seis clases del modelo se conservan. Cinco RF se vinculan directamente con ese modelo de clases; las demás filas identifican su caso de uso o ámbito y sus pruebas.

La columna «Último CR» vincula RF-015 con CR-001, RF-005 con CR-003 y RF-001 con CR-004. El [informe de trazabilidad](../reportes/reporte-v2.0.md#trazabilidad-de-los-cambios) reúne esos recorridos y la evidencia de Kanban correspondiente a CR-002.

[Hoja de cálculo de trazabilidad](../reportes/trazabilidad-v2.0.xlsx).
