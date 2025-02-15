from behave import *

from support.Exceptions import ErrorStepException


@then(u'Verificar que se muestre alerta de credenciales invalidas')
def step_impl(context):
    try:
        context.application.LoginPage.CheckAlertInvalidCredentials()
    except Exception as ex:
        message_fail = f"Fallo el step al intentar validar las alertas de credenciales invalidas \n El motivo: {ex}"
        raise ErrorStepException(message_fail)


@then(u'Verificar que se muestre alerta de Email no registrado como usuario')
def step_impl(context):
    try:
        context.application.LoginPage.CheckAlertUserNonExistent()
    except Exception as ex:
        message_fail = f"Fallo el step al intentar validar las alertas de credenciales invalidas \n El motivo: {ex}"
        raise ErrorStepException(message_fail)