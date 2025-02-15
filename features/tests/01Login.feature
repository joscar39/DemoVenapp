Feature: Login

  @test1
  Scenario Outline: TC-LP001 - Login Iniciar sesion exitoso con usuario valido
    # TC-LP001 - Login Iniciar sesion exitoso con usuario valido
    Given Acceder a la URL del aplicativo Venapp
    Then Mostrar la URL acorde al modulo de login de la web VenApp con el title:"<Title>"
    When Ingresar correo en el campo email: "<Email>"
    When Ingresar contraseña en el campo contraseña: "<Password>"
    When Hacer click en el boton Iniciar Sesion
    Then Verificar que se muestre el home correspondiente al acceso exitoso del usuario

    Examples:
      |    Title   | Email                  |   Password |
      | Ven App    | automation@yopmail.com | Aa123456.  |

  @test2.0
  Scenario Outline: TC-LP004 - Login Iniciar sesion fallido con datos invalidos
    # TC-LP004 - Login Iniciar sesion fallido con datos invalidos
    Given Acceder a la URL del aplicativo Venapp
    Then Mostrar la URL acorde al modulo de login de la web VenApp con el title:"<Title>"
    When Ingresar correo en el campo email: "<Email>"
    When Ingresar contraseña en el campo contraseña: "<Password>"
    When Hacer click en el boton Iniciar Sesion
    Then Verificar que se muestre alerta de credenciales invalidas

    Examples:
      |    Title   | Email                  |   Password |
      | Ven App    | automation@yopmail.com | 123456  |

  @test2.1
  Scenario Outline: TC-LP004 - Login Iniciar sesion fallido con datos invalidos
    # TC-LP004 - Login Iniciar sesion fallido con datos invalidos
    Given Acceder a la URL del aplicativo Venapp
    Then Mostrar la URL acorde al modulo de login de la web VenApp con el title:"<Title>"
    When Ingresar correo en el campo email: "<Email>"
    When Ingresar contraseña en el campo contraseña: "<Password>"
    When Hacer click en el boton Iniciar Sesion
    Then Verificar que se muestre alerta de Email no registrado como usuario

    Examples:
      |    Title   | Email              |   Password |
      | Ven App    | errado@yopmail.com | Aa123456.  |