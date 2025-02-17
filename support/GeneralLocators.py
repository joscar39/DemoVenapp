from selenium.webdriver.common.by import By


class LocatorsLoginPage:


    locatorInputEmail = (By.XPATH, "//input[@Placeholder='Email']")
    locatorInputPassword = (By.XPATH, "//input[@Placeholder='Contraseña']")
    locatorButtonLogin = (By.XPATH, "//button[@type='button']/div/p[contains(text(), 'Iniciar sesión')]")
    locatorCheckTextRechargeLoginSuccess = (By.XPATH, "//h6[contains(text(), 'Recargas')]")
    LocatorCheckTextLotteryLoginSuccess = (By.XPATH, "//h6[contains(text(), 'Lotería')]")
    locatorAlertInvalidCredential = (By.XPATH, "//p[contains(text(),'Contraseña incorrecta')]")
    locatorAlertUserNonExistent = (By.XPATH, "//p[contains(text(),'Este email no está registrado como usuario')]")

class LocatorsHomePage:

    locatorOptionModuleRecharge = (By.XPATH, "(//div[@class='MuiListItemIcon-root css-1f8bwsm'])[position()=4]")
    locatorValidateRedirectionRechargePage = (By.XPATH, "//h6[contains(text(), 'Recargas')]")
    locatorUrlRechargesPage = "/recharges"

class LocatorsRechargePage:


    locatorOptionTelemarketer= (By.XPATH, "(//img[@class='MuiBox-root css-bu02ye'])[position()={}]")


    locatorInputSelectTypeService = (By.ID, "mui-component-select-serviceType")
    locatorOptionTypeServiceAndTypePrefix = (By.XPATH, "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']/li/p[text()='{}']")
    locatorInputSelectPrefixNumber = (By.XPATH, "//div[@id='mui-component-select-prefix']")
    locatorInputNumberPhone = (By.XPATH, "//input[@name='serviceNumber']")
    locatorInputSelectAmount = (By.XPATH, "//div[@id='mui-component-select-amount']")
    locatorOptionListAmount = (By.XPATH, "//li//p[text()='Bs.{}']")
    locatorCheckTotalAmount = (By.XPATH, "//h5[contains(text(),'Total de la recarga')]/following-sibling::h5[contains(.,'Bs.{}')]")
    locatorButtonRecharge = (By.XPATH, "//div/p[contains(text(), 'RECARGAR')]")
    locatorCheckRedirectionPaymentGateway = (By.XPATH, "//h6[contains(text(), 'Método de pago')]")