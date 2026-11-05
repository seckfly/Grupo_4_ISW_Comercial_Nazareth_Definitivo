# Pruebas del catálogo ampliado

Este archivo complementa [las nueve pruebas de la línea base](pruebas.md). Cada caso describe un escenario y su resultado esperado a partir del [SRS](../docs/SRS.md) y los [casos de uso](../docs/CU.md).

| ID | Requisito | Escenario | Resultado esperado |
|---|---|---|---|
| PRU-020 | REQ-003 | Registrar una orden con razón social, RUC y teléfono del proveedor; consultar la orden guardada. | La orden conserva los tres datos del proveedor sin requerir un catálogo de proveedores. |
| PRU-021 | REQ-004 | Registrar una orden con dos productos, cantidades y costos conocidos; consultar el total y el estado. | La orden conserva el detalle y el proveedor, calcula el total estimado y queda en estado pendiente. |
| PRU-022 | REQ-005 | Recibir parte de una orden pendiente y consultar cantidades recibidas, stock, movimiento y saldo de la orden. | La recepción aumenta el stock según la cantidad recibida y registra la entrada en la misma transacción; la orden conserva el saldo pendiente. |
| PRU-023 | REQ-006 | Iniciar y cerrar sesión con el perfil administrativo y con un cliente registrado; intentar acceder a funciones protegidas tras cerrar sesión. | Cada perfil accede a sus funciones autorizadas y el cierre de sesión impide continuar con la sesión anterior. |
| PRU-024 | REQ-008 | Crear una campaña por producto con descuento y vigencia; editarla, pausarla, activarla y eliminarla. | La campaña conserva los cambios de descuento, vigencia y estado; las acciones modifican la campaña seleccionada. |
| PRU-025 | REQ-009 | Crear desde el portal una solicitud de separación de hasta tres productos; consultar su código, importe estimado y estado. | La solicitud se guarda con esos datos y su vencimiento de 24 horas; no confirma una venta ni descuenta existencias. |
| PRU-026 | REQ-011 | Consultar un cliente identificado con compras previas y contrastar nombre, contacto, frecuencia e historial básico. | La consulta muestra los datos y el historial correspondientes al cliente elegido. |
| PRU-027 | REQ-012 | Consultar un periodo con ventas conocidas y contrastar ventas, métodos de pago y productos con movimiento. | El resumen corresponde al periodo elegido y coincide con los registros de ventas y movimientos preparados. |
| PRU-028 | REQ-013 | Con un administrador autorizado, crear, editar y desactivar una cuenta; intentar una operación protegida con un rol no autorizado. | Los cambios de cuenta y rol se conservan; el rol no autorizado es rechazado y la cuenta administrativa permanece protegida. |
| PRU-029 | REQ-014 | Ingresar como cliente registrado con compras y puntos conocidos; consultar su cuenta. | Se muestran sus datos, historial de compras y puntos asociados a esa cuenta. |
| PRU-030 | RNF-001 | Medir diez registros equivalentes de venta de hasta tres líneas, con precios cargados y un administrador; excluir la espera de un pago externo. | Cada registro se confirma en menos de 15 segundos en las condiciones indicadas. |
| PRU-031 | RNF-002 | Ingresar como cliente registrado y revisar la navegación; intentar una operación administrativa protegida. | Las opciones administrativas no aparecen en la navegación del cliente y la operación protegida rechaza el rol. |
| PRU-032 | RNF-003 | En entorno local, con un usuario y el catálogo de demostración, medir diez consultas de productos, diez de stock y diez de resumen. | Cada consulta responde en tres segundos o menos en las condiciones indicadas. |
| PRU-033 | RNF-004 | Registrar una venta válida; repetir con stock insuficiente y con un fallo de guardado, consultando venta, detalle, movimiento y stock. | En éxito se confirman juntos; en los intentos rechazados o fallidos no quedan modificaciones parciales. |
| PRU-034 | RNF-005 | Calcular subtotales y totales con cantidades y precios conocidos y compararlos con los importes mostrados y guardados. | Los importes usan dos decimales y la diferencia respecto del cálculo redondeado es S/ 0,00. |
| PRU-035 | RNF-006 | Conservar una copia de la base de datos al cierre de la jornada; restaurarla y comparar las ventas y sus registros asociados. | La restauración recupera los registros conservados, incluidas las ventas de esa jornada. |
