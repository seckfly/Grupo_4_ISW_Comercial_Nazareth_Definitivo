
# Comercial Nazareth: laboratorio 7

Grupo 4 · Ingeniería de Software

Gestión del cambio y trazabilidad de requisitos aplicada al sistema de gestión comercial y portal de clientes de Comercial Nazareth.

## Integrantes

| Integrante | Código |
|---|---|
| Marco Antonio Martell Alvarez | N00471929 |
| Alejandro Horna Quezada | N00475530 |
| Isaí Samuel Bejarano Benites | N00490010 |
| Cesar Jeremin Alonso Chuquimango Reyes | N00480808 |
| Alonso Castillo Davalos | N00491764 |

## Documentos

El alcance comprende cinco requisitos de venta, existencias, catálogo, vinculación del cliente y mantenimiento de productos.

- [Convención de identificadores](docs/convencion-ids.md).
- [Requisitos seleccionados](docs/SRS.md).
- [Casos de uso](docs/CU.md).
- [Diagrama de clases](modelos/clases.png), con su fuente editable [clases.drawio](modelos/clases.drawio).
- [Pruebas documentadas](pruebas/pruebas.md).
- [Matriz de trazabilidad](matrices/trazabilidad.md).
- [Reporte de trazabilidad v1.1](reportes/reporte-v1.1.md).

## Sesión 12

- [Impacto de CR-001](matrices/impacto-cr-001.md): alcance, tiempo y calidad/costo.
- [Riesgos de CR-001](matrices/riesgos-cr-001.md): probabilidad, impacto y respuesta.
- [Reporte de verificación de trazabilidad](reportes/trazabilidad-s12.md).

Para actualizar el reporte después de cambiar algún artefacto, ejecutar desde la raíz del repositorio:

```bash
python3 scripts/verificar-trazabilidad.py
```

El script coteja los IDs de la matriz con SRS, casos de uso, diagrama editable y pruebas. La cobertura indica vínculos documentados; no representa ejecución de pruebas.

## Adaptación ágil V2

- [Documentación de la adaptación ágil](docs/agilidad.md).
- [Tablero Kanban en Trello](https://trello.com/b/9LEaT3KG/comercial-nazareth-kanban-v2).
- [PR #1: adaptación ágil y prueba PRU-019](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Lab7_V2/pull/1).
- [PR #2: actualización de las reglas de concurrencia](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Lab7_V2/pull/2).

La adaptación incorpora PRU-019 para el fallo al guardar un ajuste manual de REQ-015. Se mantienen los cinco requisitos y se amplía la documentación a nueve pruebas, con una cobertura por requisitos del 100 %.

## Antecedentes

- [Repositorio original del laboratorio 7](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Lab7).
- [Documentación de la línea base v1.0](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Lab7_V2/tree/v1.0).
- [Documentación de la línea base v1.1](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Lab7_V2/tree/v1.1).
- [Reporte histórico de trazabilidad v1.1](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Lab7_V2/blob/v1.1/reportes/reporte-v1.1.md).
