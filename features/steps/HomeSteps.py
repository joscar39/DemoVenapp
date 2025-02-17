from behave import *

from support.Exceptions import ErrorStepException


@when(u'Hacer click en el modulo recargas desde el menu lateral')
def step_impl(context):
    try:
        context.application.HomePage.ClickOnModuleRechargerInSideMenu()
    except Exception as ex:
        message_fail = f"Fallo el step al intentar hacer click en el modulo recargas desde el menu lateral\n El motivo: {ex}"
        raise ErrorStepException(message_fail)

@then(u'Validar la redireccion al modulo recargas')
def step_impl(context):
    try:
        context.application.HomePage.CheckRedirectionSuccessfullyToRechargesPage()
    except Exception as ex:
        message_fail = f"Fallo el step al intentar validar la redireccion al modulo recargas\n El motivo: {ex}"
        raise ErrorStepException(message_fail)

