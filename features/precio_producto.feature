Feature: Calculo de precio con descuento e IVA
  Como administrador de la Libreria del Centro
  Quiero aplicar descuentos y calcular el precio final con IVA
  Para ofrecer promociones sin perder el control del valor de venta

  Background:
    Given un producto llamado "Novela" con precio base de 10000 pesos

  @positivo @descuento-valido
  Scenario: Aplicar un descuento valido al producto
    When aplico un descuento del 20 por ciento
    Then el descuento queda registrado en 20 por ciento

  @borde @descuento-cero
  Scenario: Aceptar descuento en el limite inferior
    When aplico un descuento del 0 por ciento
    Then el descuento queda registrado en 0 por ciento

  @borde @descuento-maximo
  Scenario: Aceptar descuento en el limite superior
    When aplico un descuento del 40 por ciento
    Then el descuento queda registrado en 40 por ciento

  @negativo @descuento-invalido
  Scenario: Rechazar descuento mayor al permitido
    When intento aplicar un descuento del 41 por ciento
    Then el sistema rechaza el descuento con un mensaje claro

  @positivo @precio-final
  Scenario Outline: Calcular precio final con descuento e IVA del 19 por ciento
    When aplico un descuento del <descuento> por ciento
    Then el precio final debe ser <precio_final> pesos

    Examples:
      | descuento | precio_final |
      | 0         | 11900        |
      | 10        | 10710        |
      | 40        | 7140         |

