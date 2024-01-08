-- Insertar datos en la tabla `empleados`
INSERT INTO `empleados` (`nombre`, `rol`) VALUES
  ('Marta', 'Admin'),
  ('Carlos', 'Content Operator');

-- Insertar datos en la tabla `precios`
INSERT INTO `precios` (`id_tienda`, `id_producto`, `precio`) VALUES
  (100, 201, 10190.00),
  (102, 201, 10190.00);

-- Insertar datos en la tabla `productos`
INSERT INTO `productos` (`nombre`, `categoria`, `descripcion`) VALUES
  ('Refrigerador', 'Electrodomesticos', 'Refrigerador Samsung Top Mount 12 Pies Acero Inoxidable');
