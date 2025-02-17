from support.BaseActions import BaseActions
from support.GeneralLocators import LocatorsLoginPage as lp

class LoginPage(BaseActions): #El page de login hereda la clase BaseActions

    def __init__(self, driver):
        super().__init__(driver) #Llama al constructor de la clase padre BaseActions

    """
    FUNCIONES PARA GESTOS Y ACCIONES
    """

    def InsertEmailToInput(self, email):
        if isinstance(email, str) and email != "":
            BaseActions.sendTextBySelector(self, lp.locatorInputEmail[0],
                                           lp.locatorInputEmail[1], email,3)
        else:
            raise RuntimeError(f"El dato ingresado como Email no es correcto o esta vacio:"
                               f" {email if email != '' else 'Empty'}")

    def InsertPasswordToInput(self, password):
        if isinstance(password, str) and password != "":
            BaseActions.sendTextBySelector(self, lp.locatorInputPassword[0],
                                           lp.locatorInputPassword[1], password, 3)
        else:
            raise RuntimeError(f"El dato ingresado como Password no es correcto o esta vacio:"
                               f" {password if password != '' else 'Empty'}")


    def ClickOnButtonLogin(self):
        BaseActions.clickOnElementBySelector(self, lp.locatorButtonLogin[0],
                                             lp.locatorButtonLogin[1], 3)




    """
    FUNCIONES PARA VALIDADORES
    """

    def ValidateInitLoginPage(self, title):
        if isinstance(title, str) and title !="":
            val = BaseActions.getTitleWeb(self)
            if val == title:
                BaseActions.screenshot(self, "Validado el title de la web correctamente")
            else:
                raise RuntimeError("No se mostro el title del Login Page como se esperaba o la url no es la correcta")
        else:
            raise RuntimeError(f"El dato ingresado como Title no es correcto o esta vacio:"
                               f" {title if title != '' else 'Empty'}")


    def CheckLoginSuccess(self):
        val = BaseActions.findElementIsDisplayed(self, lp.locatorCheckTextRechargeLoginSuccess[0],
                                                 lp.locatorCheckTextRechargeLoginSuccess[1], 3)

        val2 = BaseActions.findElementIsDisplayed(self, lp.LocatorCheckTextLotteryLoginSuccess[0],
                                                  lp.LocatorCheckTextLotteryLoginSuccess[1], 3)

        if val and val2:
            BaseActions.screenshot(self, "Se Inicio sesion correctamente")
        else:
            raise RuntimeError("No se mostro los textos de Recarga y Lotería indicativo de login exitoso")


    def CheckAlertInvalidCredentials(self):
        val = BaseActions.findElementIsDisplayed(self, lp.locatorAlertInvalidCredential[0],
                                                 lp.locatorAlertInvalidCredential[1], 3)

        if val:
            BaseActions.screenshot(self, "Se Mostro alerta correctamente")
        else:
            raise RuntimeError("No se mostro los textos de credenciales incorrectas")

    def CheckAlertUserNonExistent(self):
        val = BaseActions.findElementIsDisplayed(self, lp.locatorAlertUserNonExistent[0],
                                                 lp.locatorAlertUserNonExistent[1], 3)

        if val:
            BaseActions.screenshot(self, "Se Mostro alerta correctamente")
        else:
            raise RuntimeError("No se mostro los textos de usuario no existente")