# Análisis de impacto de CR-001

Cambio evaluado: motivo obligatorio en ajustes manuales de existencias de RF-015. La tabla compara el alcance del cambio antes y después de CR-001.

| Dimensión | Artefactos afectados | Efecto y medida |
|---|---|---|
| Alcance | RF-015, CU-006, CLS-MovimientoInventario, PRU-016 a PRU-018, matriz y reporte v1.1 | Un requisito, un caso de uso y una clase modificados. Se actualizó una prueba y se añadieron dos. La regla se aplica solo a ajustes manuales; la salida por venta mantiene su flujo. |
| Tiempo | Documentación, modelo y revisión de vínculos | El CR estimó 2 horas para actualizar y comprobar la documentación y el modelo afectados. |
| Calidad/costo | Validación del motivo, historial, stock y pruebas documentadas | Se documentan pruebas de aceptación con motivo válido y de rechazo de motivo vacío o compuesto por espacios. En el alcance evaluado, las pruebas documentadas pasan de 6 a 8. |

En el diseño, CLS-MovimientoInventario incorpora `motivo` y `validarMotivo`; `registrarAjuste` recibe el motivo. El ajuste, su motivo y el stock deben guardarse en una misma transacción.
