from selenium.webdriver import Keys

from configurations.config import Datatest
from support.BaseActions import BaseActions
from support.GeneralLocators import LocatorsRechargePage as rep

class RechargerPage(BaseActions):

    def __init__(self, driver):
        super().__init__(driver)

    """
    FUNCIONES PARA GESTOS Y ACCIONES
    """
    def SelectTypeTelemarketer(self, telemarketer):
        if isinstance(telemarketer, str) and telemarketer != "":
            #Buscar el parametro en el diccionario de teleoperadores
            value = Datatest.OPTIONS_TELEMARKETER.get(telemarketer)
            if value is not None:
                formatted_option = rep.locatorOptionTelemarketer[1].format(value)
                BaseActions.clickOnElementBySelector(self, rep.locatorOptionTelemarketer[0],
                                                     formatted_option, 3)
                BaseActions.screenshot(self, f"Opcion de telemarketer seleccionado: {telemarketer}")
                return value # Retornar el valor de operador seleccionado para continuar con el proceso de llenado de datos
            else:
                raise RuntimeError(f"El dato ingresado como telemarketer no esta dentro de las opciones validas: ",
                                   telemarketer)
        else:
            raise RuntimeError(f"El dato ingresado como Operador telefonico no es correcto o esta vacio:"
                               f" {telemarketer if telemarketer != '' else 'Empty'}")


    def ClickOnInputSelectTypeService(self):
        BaseActions.scrollToElementIsVisibility(self, rep.locatorInputSelectAmount[0],
                                                rep.locatorInputSelectAmount[1], 3)
        BaseActions.clickOnElementBySelector(self, rep.locatorInputSelectTypeService[0],
                                             rep.locatorInputSelectTypeService[1], 3)

    def SelectTypeOfServiceByTelemarketer(self, type_service):
        if isinstance(type_service, str) and type_service != "":
            formatted_data = rep.locatorOptionTypeServiceAndTypePrefix[1].format(type_service)
            BaseActions.clickOnElementBySelector(self, rep.locatorOptionTypeServiceAndTypePrefix[0],
                                                 formatted_data, 3)
        else:
            raise RuntimeError(f"El dato ingresado como Tipo de servicio no es correcto o esta vacio:"
                               f" {type_service if type_service != '' else 'Empty'}")

    def SelectPrefixByTelemarketer(self, prefix):
        if isinstance(prefix, str) and prefix != "":
            formatted_data = rep.locatorOptionTypeServiceAndTypePrefix[1].format(prefix)
            BaseActions.clickOnElementBySelector(self, rep.locatorInputSelectPrefixNumber[0],
                                                 rep.locatorInputSelectPrefixNumber[1], 3)
            BaseActions.clickOnElementBySelector(self, rep.locatorOptionTypeServiceAndTypePrefix[0],
                                                 formatted_data, 3)
        else:
            raise RuntimeError(f"El dato ingresado como prefijo no es correcto o esta vacio:"
                               f" {prefix if prefix != '' else 'Empty'}")

    def InsertNumberPhone(self, number):
        if isinstance(number, str) and number != "":
            BaseActions.sendTextBySelector(self, rep.locatorInputNumberPhone[0],
                                           rep.locatorInputNumberPhone[1], number, 3)
        else:
            raise RuntimeError(f"El dato ingresado como Numero de telefono no es correcto o esta vacio:"
                               f" {number if number != '' else 'Empty'}")

    def ClickOnInputSelectAmount(self, amount):
        if isinstance(amount, str) and amount != "":
            formatted_amount = rep.locatorOptionListAmount[1].format(amount)
            BaseActions.clickOnElementBySelector(self, rep.locatorInputSelectAmount[0],
                                                 rep.locatorInputSelectAmount[1], 3)
            BaseActions.clickOnElementBySelector(self, rep.locatorOptionListAmount[0],
                                                 formatted_amount, 3)
            
        else:
            raise RuntimeError(f"El dato ingresado como Monto a seleccionar en la lista para recargar no es correcto o esta vacio:"
                               f" {amount if amount != '' else 'Empty'}")

    def CLickOnButtonRecharge(self):
        BaseActions.clickOnElementBySelector(self, rep.locatorButtonRecharge[0],
                                             rep.locatorButtonRecharge[1], 3)



    """
    FUNCIONES PARA VALIDADORES
    """

    def CheckAmountChargeCorrectly(self, amount):
        if isinstance(amount, str) and amount != "":
            formatted_amount = rep.locatorCheckTotalAmount[1].format(amount)
            val = BaseActions.findElementIsDisplayed(self, rep.locatorCheckTotalAmount[0], formatted_amount, 3)
            if val:
                BaseActions.screenshot(self, "Se visualiza correctamente el monto agregado a recargar")
            else:
                raise RuntimeError("No se muestra el valor de la recarga cargado en el campo total de la recarga")
        else:
            raise RuntimeError(f"El dato ingresado como Monto a recargar no es correcto o esta vacio:"
                               f" {amount if amount != '' else 'Empty'}")


    def CheckRedirectionToPaymentGateway(self):
        val = BaseActions.findElementIsDisplayed(self, rep.locatorCheckRedirectionPaymentGateway[0],
                                                 rep.locatorCheckRedirectionPaymentGateway[1], 3)
        if val:
            BaseActions.screenshot(self, "Se mostro la pasarela de pago exitosamente")
        else:
            raise RuntimeError("No se muestra el texto validador de la pantala de pasarela de pago")

    def CheckAmountTotalRecharge(self, amount):
        formatted_amount = rep.locatorCheckTotalAmount[1].format(amount)
        val = BaseActions.findElementIsDisplayed(self, rep.locatorCheckTotalAmount[0], formatted_amount, 3)
        if val:
            BaseActions.screenshot(self, "El monto total a recargar coincide con el visualizado al seleccionar producto")
        else:
            raise RuntimeError("El monto indicado no coincide con el visualizado en la seleccion del producto")