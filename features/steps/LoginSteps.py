from behave import *

from support.Exceptions import ErrorStepException
from web.applications import Application


@given(u'Acceder a la URL del aplicativo Venapp')
def step_impl(context):
    try:
       context.application = Application(context.driver)
    except Exception as ex:
        message_fail = f"Fallo el step al intentar acceder la URL Seleccionada \n El motivo: {ex}"
        raise ErrorStepException(message_fail)

@then(u'Mostrar la URL acorde al modulo de login de la web VenApp con el title:"{Title}"')
def step_impl(context, Title):
    try:
        context.application.LoginPage.ValidateInitLoginPage(Title)
    except Exception as ex:
        message_fail = f"Fallo el step al intentar validar el title de la web \n El motivo: {ex}"
        raise ErrorStepException(message_fail)

@when(u'Ingresar correo en el campo email: "{Email}"')
def step_impl(context, Email):
    try:
        context.application.LoginPage.InsertEmailToInput(Email)
    except Exception as ex:
        message_fail = f"Fallo el step al intentar validar el title de la web \n El motivo: {ex}"
        raise ErrorStepException(message_fail)

@when(u'Ingresar contraseña en el campo contraseña: "{Password}"')
def step_impl(context, Password):
    try:
        context.application.LoginPage.InsertPasswordToInput(Password)
    except Exception as ex:
        message_fail = f"Fallo el step al intentar validar el title de la web \n El motivo: {ex}"
        raise ErrorStepException(message_fail)

@when(u'Hacer click en el boton Iniciar Sesion')
def step_impl(context):
    try:
        context.application.LoginPage.ClickOnButtonLogin()
    except Exception as ex:
        message_fail = f"Fallo el step al intentar validar el title de la web \n El motivo: {ex}"
        raise ErrorStepException(message_fail)

@then(u'Verificar que se muestre el home correspondiente al acceso exitoso del usuario')
def step_impl(context):
    try:
        context.application.LoginPage.CheckLoginSuccess()
    except Exception as ex:
        message_fail = f"Fallo el step al intentar validar el title de la web \n El motivo: {ex}"
        raise ErrorStepException(message_fail)