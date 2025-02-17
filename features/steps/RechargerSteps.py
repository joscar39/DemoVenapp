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

@when(u'Seleccionar monto a recargar: "{Amount}", "{Promotion}"')
def step_impl(context, Amount, Promotion):
    try:

        #Obtener el monto más cercano a las opciones de recarga y el monto de promocion en caso que si aplica
        context.nearest_amount = BaseActions.getNearestAmountOptions(Amount, context.value_telemarketer, Promotion)
        context.check_amount = None
        if str(Promotion).lower() == "yes":
            # Actualizar la variable nearest_amount con el monto seleccionado más la suma de la promocion aplicada
            context.check_amount = context.nearest_amount[1]
            # Envia monto a seleccionar en la lista de opciones cuando hay promociones activas
            context.application.RechargerPage.ClickOnInputSelectAmount(context.nearest_amount[0])
        else:
            # Actualizar la variable nearest_amount solo con el monto seleccionado en la lista de opciones
            context.check_amount = context.nearest_amount
            # Envia monto a seleccionar en la lista de opciones cuando no hay promociones activas
            context.application.RechargerPage.ClickOnInputSelectAmount(context.nearest_amount)


    except Exception as ex:
        message_fail = f"Fallo el step al intentar seleccionar un monto a recargar\n El motivo: {ex}"
        raise ErrorStepException(message_fail)

@then(u'Validar monto en el campo de total de recarga')
def step_impl(context):
    try:
        if context.check_amount is not None:
            context.application.RechargerPage.CheckAmountChargeCorrectly(context.check_amount)
        else:
            raise RuntimeError(f"El valor de monto a verificar es Nulo: {context.check_amount}")
    except Exception as ex:
        message_fail = f"Fallo el step al intentar validar el monto en el campo de total a recargar\n El motivo: {ex}"
        raise ErrorStepException(message_fail)


@when(u'Pulsar boton recargar')
def step_impl(context):
    try:
        context.application.RechargerPage.CLickOnButtonRecharge()
    except Exception as ex:
        message_fail = f"Fallo el step al intentar pulsar el boton de recargar\n El motivo: {ex}"
        raise ErrorStepException(message_fail)

@then(u'Validar redireccion al carrito de compras')
def step_impl(context):
    try:
        context.application.RechargerPage.CheckRedirectionToPaymentGateway()
    except Exception as ex:
        message_fail = f"Fallo el step al intentar validar la redireccion al checkout del carrito de compras\n El motivo: {ex}"
        raise ErrorStepException(message_fail)

@then(u'Confirmar que el monto total de la recarga sea el mismo al seleccionar el producto')
def step_impl(context):
    try:
        if context.check_amount is not None:
            context.application.RechargerPage.CheckAmountTotalRecharge(context.check_amount)
        else:
            raise RuntimeError(f"El valor de monto a verificar es Nulo: {context.check_amount}")
    except Exception as ex:
        message_fail = f"Fallo el step al intentar confirmar el monto total a recargar en la pasarela de pago\n El motivo: {ex}"
        raise ErrorStepException(message_fail)