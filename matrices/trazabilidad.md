# Matriz de trazabilidad de Comercial Nazareth

Esta matriz reúne los 15 requisitos funcionales y los 6 no funcionales del [SRS](../docs/SRS.md). Los casos de uso se toman de [CU.md](../docs/CU.md). Las clases se enlazan cuando aparecen en el [modelo de clases](../modelos/clases.png), que conserva el alcance de la línea base v1.1. Las pruebas están documentadas en [pruebas.md](../pruebas/pruebas.md) y [pruebas-catalogo.md](../pruebas/pruebas-catalogo.md).

## Requisitos funcionales

| ID | Requisito | Caso de uso o ámbito | Clase del modelo | Pruebas documentadas | Último CR |
|---|---|---|---|---|---|
| REQ-001 | Registrar venta | CU-001 | CLS-Venta, CLS-DetalleVenta, CLS-Producto, CLS-MovimientoInventario | PRU-001, PRU-003 | — |
| REQ-002 | Consultar existencias y alertas | CU-006 | CLS-Producto | PRU-002 | — |
| REQ-003 | Identificar proveedor de la orden | CU-008 | — | PRU-020 | — |
| REQ-004 | Registrar orden de compra | CU-008, CU-009 | — | PRU-021 | — |
| REQ-005 | Registrar recepción | CU-009 | — | PRU-022 | — |
| REQ-006 | Acceder según perfil | Acceso transversal | — | PRU-023 | — |
| REQ-007 | Consultar catálogo | CU-003; también CU-001, CU-005 y CU-008 | CLS-Producto, CLS-ListaProductos, CLS-Cliente | PRU-007 | — |
| REQ-008 | Gestionar promociones | CU-004 | — | PRU-024 | — |
| REQ-009 | Solicitar separación | CU-005 | — | PRU-025 | — |
| REQ-010 | Vincular cliente a la venta | CU-002; extiende CU-001 | CLS-Cliente, CLS-Venta | PRU-004 | — |
| REQ-011 | Consultar clientes frecuentes | Consulta administrativa | — | PRU-026 | — |
| REQ-012 | Consultar resumen y reportes | Consulta administrativa | — | PRU-027 | — |
| REQ-013 | Administrar accesos | Acceso transversal | — | PRU-028 | — |
| REQ-014 | Consultar cuenta y beneficios | Portal de clientes | — | PRU-029 | — |
| REQ-015 | Mantener productos e inventario | CU-006 | CLS-Producto, CLS-MovimientoInventario | PRU-016, PRU-017, PRU-018, PRU-019 | CR-001 |

## Requisitos no funcionales

| ID | Requisito | Ámbito | Prueba documentada |
|---|---|---|---|
| RNF-001 | Rapidez de registro | CU-001 | PRU-030 |
| RNF-002 | Separación de perfiles | Acceso transversal | PRU-031 |
| RNF-003 | Tiempo de consulta | Consultas de productos, stock y resumen | PRU-032 |
| RNF-004 | Integridad de venta | CU-001 | PRU-033 |
| RNF-005 | Consistencia monetaria | CU-001 | PRU-034 |
| RNF-006 | Respaldo recuperable | Respaldo de datos | PRU-035 |

## Lectura de la matriz

Los 15 requisitos funcionales y los 6 no funcionales tienen al menos una prueba documentada. Cinco requisitos funcionales tienen un vínculo con las seis clases del modelo disponible. Los ámbitos «Acceso transversal», «Consulta administrativa», «Portal de clientes» y «Respaldo de datos» provienen del SRS; no representan casos de uso adicionales.

Desde REQ-015 se llega a CU-006, CLS-Producto, CLS-MovimientoInventario y PRU-016 a PRU-019. Desde cualquiera de esas pruebas se regresa a REQ-015 mediante la columna Requisito de los documentos de pruebas. CR-001 queda registrado como último cambio de ese requisito.

[Hoja de cálculo con cobertura actualizable](../reportes/trazabilidad-s12.xlsx).
