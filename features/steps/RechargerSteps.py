import random

from behave import *


from configurations.config import Datatest
from support.BaseActions import BaseActions
from support.Exceptions import ErrorStepException


@when(u'Seleccionar una operadora (Buscar un producto): "{Telemarketer}"')
def step_impl(context, Telemarketer):
    try:
        context.value_telemarketer = context.application.RechargerPage.SelectTypeTelemarketer(Telemarketer)
    except Exception as ex:
        message_fail = f"Fallo el step al intentar Seleccionar una operadora\n El motivo: {ex}"
        raise ErrorStepException(message_fail)

@when(u'Hacer click en el campo select de tipo de servicios')
def step_impl(context):
    try:
        context.application.RechargerPage.ClickOnInputSelectTypeService()
    except Exception as ex:
        message_fail = f"Fallo el step al intentar hacer click sobre el select de tipo de servicios \n El motivo: {ex}"
        raise ErrorStepException(message_fail)

@when(u'Seleccionar un tipo de servicio: "{TypeService}"')
def step_impl(context, TypeService):
    try:
        formatted_text = None
        if TypeService in Datatest.SYNTAX_TYPE_SERVICE: # Se formatea el texto para que coincida textualmente con la opcion del select
            formatted_text = Datatest.SYNTAX_TYPE_SERVICE[TypeService]
        if formatted_text is not None:
            context.application.RechargerPage.SelectTypeOfServiceByTelemarketer(formatted_text)
        else:
            raise RuntimeError(f"El valor ingresado como TypeService, no se encuentra escrito correctamente: {TypeService}")
    except Exception as ex:
        message_fail = f"Fallo el step al intentar al seleccionar un tipo de servicio\n El motivo: {ex}"
        raise ErrorStepException(message_fail)

@when(u'Seleccionar prefijo de teleoperadora: "{Prefix}"')
def step_impl(context, Prefix):
    try:
        context.application.RechargerPage.SelectPrefixByTelemarketer(Prefix)
    except Exception as ex:
        message_fail = f"Fallo el step al intentar Seleccionar el prefijo de la operadora\n El motivo: {ex}"
        raise ErrorStepException(message_fail)

@when(u'Insertar numero telefonico valido: "{NumberPhone}"')
def step_impl(context, NumberPhone):
    try:
        context.application.RechargerPage.InsertNumberPhone(NumberPhone)
    except Exception as ex:
        message_fail = f"Fallo el step al intentar \n El motivo: {ex}"
        raise ErrorStepException(message_fail)

@when(u'Hacer click en el campo select de monto a recargar: "{Amount}"')
def step_impl(context, Amount):
    try:
        #Obtener la posicion index del monto respecto a lista del select y el monto en formato string
        context.nearest_amount = BaseActions.getNearestAmountOptions(Amount, context.value_telemarketer)
        context.application.RechargerPage.ClickOnInputSelectAmount(context.nearest_amount)
    except Exception as ex:
        message_fail = f"Fallo el step al intentar \n El motivo: {ex}"
        raise ErrorStepException(message_fail)

@then(u'Validar monto en en campo de total de recarga')
def step_impl(context):
    try:
        context.application.RechargerPage.CheckAmountChargeCorrectly(context.nearest_amount)
    except Exception as ex:
        message_fail = f"Fallo el step al intentar \n El motivo: {ex}"
        raise ErrorStepException(message_fail)