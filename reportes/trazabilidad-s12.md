# Resumen de trazabilidad (sesión 12)

La [matriz](../matrices/trazabilidad.md) reúne los 15 RF, los seis RNF y las ocho reglas del [SRS](../docs/SRS.md). La [hoja de cálculo](trazabilidad-s12.xlsx) calcula los totales y comprueba los vínculos con [pruebas.md](../pruebas/pruebas.md).

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

RF-015 → CU-006 → CLS-Producto y CLS-MovimientoInventario → PRU-016, PRU-017, PRU-018 y PRU-019. La matriz registra CR-001 en la columna «Último CR». El recorrido inverso empieza en una PRU y vuelve a RF-015 mediante la columna «Requisitos» del documento de pruebas.
