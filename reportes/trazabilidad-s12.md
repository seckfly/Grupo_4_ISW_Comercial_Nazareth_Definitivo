# Resumen de trazabilidad (sesión 12)

La [matriz](../matrices/trazabilidad.md) enumera los 15 requisitos funcionales y los 6 no funcionales del [SRS](../docs/SRS.md). La [hoja de cálculo](trazabilidad-s12.xlsx) recalcula los totales y comprueba los vínculos con las pruebas registradas en [pruebas.md](../pruebas/pruebas.md).

| Medida | Resultado |
|---|---:|
| Requisitos funcionales con prueba documentada | 5 de 15 |
| Requisitos no funcionales con prueba documentada | 0 de 6 |
| Casos de uso documentados | 8 |
| Clases del modelo de la línea base | 6 |
| Requisitos funcionales vinculados con ese modelo | 5 de 15 |
| Pruebas documentadas | 9 |

PRU es un identificador, no un ordinal continuo: el último caso lleva el código PRU-019 y el archivo contiene nueve filas de pruebas. Cada caso describe un escenario y su resultado esperado; el repositorio no registra su ejecución.

## Recorrido de CR-001

REQ-015 → CU-006 → CLS-Producto y CLS-MovimientoInventario → PRU-016, PRU-017, PRU-018 y PRU-019. La matriz registra CR-001 en la columna «Último CR». El recorrido inverso parte de una PRU y vuelve a REQ-015 mediante la columna Requisito del documento de pruebas.
