Feature: 01 Login
  Background:
    Given Acceder a la URL del aplicativo Venapp

  Scenario Outline: 01TC-86420 - Login Iniciar sesion exitoso con usuario valido
    # TC-86420: Login Iniciar sesion exitoso con usuario valido
    Then Mostrar la URL acorde al modulo de login de la web VenApp con el title:"<Title>"
    When Ingresar correo en el campo email: "<Email>"
    When Ingresar contraseña en el campo contraseña: "<Password>"
    When Hacer click en el boton Iniciar Sesion
    Then Verificar que se muestre el home correspondiente al acceso exitoso del usuario

    Examples:
      |    Title   | Email                  |   Password |
      | Ven App    | automation@yopmail.com | Aa123456.  |