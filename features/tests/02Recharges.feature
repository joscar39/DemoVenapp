Feature: Recharges
  Background:
    Given Acceder a la URL del aplicativo Venapp

  @test3
  Scenario Outline: TC-REP01 - Buscar un teleoperador en recargas (Busqueda de producto)
    # TC-LP001 - Login Iniciar sesion exitoso con usuario valido (Pre-condicion)
    Then Mostrar la URL acorde al modulo de login de la web VenApp con el title:"<Title>"
    When Ingresar correo en el campo email: "<Email>"
    When Ingresar contraseña en el campo contraseña: "<Password>"
    When Hacer click en el boton Iniciar Sesion
    Then Verificar que se muestre el home correspondiente al acceso exitoso del usuario
    # TC-HP001 - Acceder a modulo Recargas en el menu lateral (Pre-condicion)
    When Hacer click en el modulo recargas desde el menu lateral
    Then Validar la redireccion al modulo recargas
    # TC-REP01 - Buscar un teleoperador en recargas (Busqueda de producto)
    When Seleccionar una operadora (Buscar un producto): "<Telemarketer>"


    Examples:
      |    Title   | Email                  |   Password |Telemarketer|
      | Ven App    | automation@yopmail.com | Aa123456.  |Movistar    |
      | Ven App    | automation@yopmail.com | Aa123456.  |Digitel     |
      | Ven App    | automation@yopmail.com | Aa123456.  |Movilnet    |


  @test4
  Scenario Outline: TC-REP02 - Seleccionar tipo de recarga y cantidad (Agregar producto al carrito)
    # TC-LP001 - Login Iniciar sesion exitoso con usuario valido (Pre-condicion)
    Then Mostrar la URL acorde al modulo de login de la web VenApp con el title:"<Title>"
    When Ingresar correo en el campo email: "<Email>"
    When Ingresar contraseña en el campo contraseña: "<Password>"
    When Hacer click en el boton Iniciar Sesion
    Then Verificar que se muestre el home correspondiente al acceso exitoso del usuario
    # TC-HP001 - Acceder a modulo Recargas en el menu lateral (Pre-condicion)
    When Hacer click en el modulo recargas desde el menu lateral
    Then Validar la redireccion al modulo recargas
    # TC-REP01 - Buscar un producto desde recharge page
    When Seleccionar una operadora (Buscar un producto): "<Telemarketer>"
    # TC-REP02 - Seleccionar tipo de recarga y cantidad (Agregar producto al carrito)
    When Hacer click en el campo select de tipo de servicios
    When Seleccionar un tipo de servicio: "<TypeService>"
    When Seleccionar prefijo de teleoperadora: "<Prefix>"
    When Insertar numero telefonico valido: "<NumberPhone>"
    When Seleccionar monto a recargar: "<Amount>", "<Promotion>"
    Then Validar monto en el campo de total de recarga


    Examples:
      |    Title   | Email                  |   Password |Telemarketer  | TypeService  |  Prefix |  NumberPhone  | Amount  | Promotion  |
      | Ven App    | automation@yopmail.com | Aa123456.  |Movistar      | movil        | 0414    |    8211103    | 125     |  no     |
      | Ven App    | automation@yopmail.com | Aa123456.  |Movistar      | internet     | 0424    |    3780061    | 315     |  no     |
      | Ven App    | automation@yopmail.com | Aa123456.  |Movistar      | fijo         | 02      |    126502028  | 200     |  no     |
      | Ven App    | automation@yopmail.com | Aa123456.  |Digitel       | movil        | 0412    |    2586254    |  25     |  nO     |
      | Ven App    | automation@yopmail.com | Aa123456.  |Digitel       | fijo         | 02      |    432429185  |  350    |  no     |
      | Ven App    | automation@yopmail.com | Aa123456.  |Movilnet      | movil        | 0426    |  5839102      |  102    |  yes    |
      | Ven App    | automation@yopmail.com | Aa123456.  |Movilnet      | movil        | 0416    |  4934043      |  351    |  yes    |


  @test5
  Scenario Outline: TC-REP03 - Confirmar monto total de compra (Validar total del carrito)
    # TC-LP001 - Login Iniciar sesion exitoso con usuario valido (Pre-condicion)
    Then Mostrar la URL acorde al modulo de login de la web VenApp con el title:"<Title>"
    When Ingresar correo en el campo email: "<Email>"
    When Ingresar contraseña en el campo contraseña: "<Password>"
    When Hacer click en el boton Iniciar Sesion
    Then Verificar que se muestre el home correspondiente al acceso exitoso del usuario
    # TC-HP001 - Acceder a modulo Recargas en el menu lateral (Pre-condicion)
    When Hacer click en el modulo recargas desde el menu lateral
    Then Validar la redireccion al modulo recargas
    # TC-REP01 - Buscar un producto desde recharge page
    When Seleccionar una operadora (Buscar un producto): "<Telemarketer>"
    # TC-REP02 - Seleccionar tipo de recarga y cantidad (Agregar producto al carrito)
    When Hacer click en el campo select de tipo de servicios
    When Seleccionar un tipo de servicio: "<TypeService>"
    When Seleccionar prefijo de teleoperadora: "<Prefix>"
    When Insertar numero telefonico valido: "<NumberPhone>"
    When Seleccionar monto a recargar: "<Amount>", "<Promotion>"
    Then Validar monto en el campo de total de recarga
    # TC-REP03 - Confirmar monto total de compra (Validar total del carrito)
    When Pulsar boton recargar
    Then Validar redireccion al carrito de compras
    And Confirmar que el monto total de la recarga sea el mismo al seleccionar el producto



    Examples:
      |    Title   | Email                  |   Password |Telemarketer  | TypeService  |  Prefix |  NumberPhone  | Amount  | Promotion  |
      | Ven App    | automation@yopmail.com | Aa123456.  |Movistar      | movil        | 0414    |    8211103    | 125     |  no     |
      | Ven App    | automation@yopmail.com | Aa123456.  |Movistar      | internet     | 0424    |    3138835    | 315     |  no     |
      | Ven App    | automation@yopmail.com | Aa123456.  |Movistar      | fijo         | 02      |    126502028  | 200     |  no     |
      | Ven App    | automation@yopmail.com | Aa123456.  |Digitel       | movil        | 0412    |    2586254    |  25     |  nO     |
      | Ven App    | automation@yopmail.com | Aa123456.  |Digitel       | fijo         | 02      |    432429185  |  350    |  no     |
      | Ven App    | automation@yopmail.com | Aa123456.  |Movilnet      | movil        | 0426    |  7141110      |  102    |  yes    |
      | Ven App    | automation@yopmail.com | Aa123456.  |Movilnet      | movil        | 0416    |  4934043      |  351    |  yes    |
