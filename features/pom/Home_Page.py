from support.BaseActions import BaseActions
from support.GeneralLocators import LocatorsHomePage as hp

class HomePage(BaseActions):

    def __init__(self, driver):
        super().__init__(driver)

    """
    FUNCIONES PARA GESTOS Y ACCIONES
    """
    def ClickOnModuleRechargerInSideMenu(self):
        BaseActions.clickOnElementBySelector(self, hp.locatorOptionModuleRecharge[0],
                                             hp.locatorOptionModuleRecharge[1], 3)

    """
    FUNCIONES PARA VALIDADORES
    """

    def CheckRedirectionSuccessfullyToRechargesPage(self):
        val = BaseActions.findElementIsDisplayed(self, hp.locatorValidateRedirectionRechargePage[0],
                                                 hp.locatorValidateRedirectionRechargePage[1], 3)
        current_url = BaseActions.getCurrentUrl(self)

        if val and current_url.endswith(hp.locatorUrlRechargesPage):
            BaseActions.screenshot(self, "Redirecciono a pagina de recargas exitosamente")
        else:
            if not val:
                raise RuntimeError("No se localizo el titulo Recargas luego de redireccionar")
            elif current_url.endswith(hp.locatorUrlRechargesPage):
                raise RuntimeError(f"La Url no cuenta con la terminacion: {hp.locatorUrlRechargesPage}")