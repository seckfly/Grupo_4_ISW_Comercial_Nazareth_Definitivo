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

## Recorrido de CR-001

El cambio de v1.1 enlaza REQ-015, CU-006, CLS-MovimientoInventario y PRU-016 a PRU-018. En v2.0, el requisito figura como RF-015 y también se vincula con CLS-Producto y PRU-019, que cubre el fallo de guardado. La matriz registra CR-001 en la columna «Último CR». El recorrido inverso empieza en una PRU y vuelve a RF-015 mediante la columna «Requisitos» del documento de pruebas.

Consulta el [registro de cambios](../docs/cambios.md) para ver las solicitudes y los PR de esta versión.
