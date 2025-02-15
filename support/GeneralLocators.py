from selenium.webdriver.common.by import By


class LoginPage:

    locatorUrlLoginPage = "/auth/login"
    locatorInputEmail = (By.XPATH, "//input[@Placeholder='Email']")
    locatorInputPassword = (By.XPATH, "//input[@Placeholder='Contraseña']")
    locatorButtonLogin = (By.XPATH, "//button[@type='button']/div/p[contains(text(), 'Iniciar sesión')]")
    locatorCheckTextRechargeLoginSuccess = (By.XPATH, "//h6[contains(text(), 'Recargas')]")
    LocatorCheckTextLotteryLoginSuccess = (By.XPATH, "//h6[contains(text(), 'Lotería')]")
    locatorAlertInvalidCredential = (By.XPATH, "//p[contains(text(),'Contraseña incorrecta')]")
    locatorAlertUserNonExistent = (By.XPATH, "//p[contains(text(),'Este email no está registrado como usuario')]")

class HomePage:

    locatorModuleRecharge = (By.XPATH, "(//div[@class='MuiListItemIcon-root css-1f8bwsm'])[position()=4]")
    locatorOptionTelemarketerDigitel = (By.XPATH, "(//img[@class='MuiBox-root css-bu02ye'])[position()=1]")
    locatorOptionTelemarketerMovistar = (By.XPATH, "(//img[@class='MuiBox-root css-bu02ye'])[position()=2]")
    locatorOptionTelemarketerMovilnet = (By.XPATH, "(//img[@class='MuiBox-root css-bu02ye'])[position()=3]")

class RechargePage:

    locatorInputSelectTypeService = (By.ID, "mui-component-select-serviceType")
    locatorOptionTypeServiceTypePrefixAndListAmount = (By.XPATH, "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']/li/p[text()='{}']")
    locatorInputSelectPrefixNumber = (By.XPATH, "//div[@id='mui-component-select-prefix']")
    # locatorOptionTypePrefixNumber = (By.XPATH, "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']/li/p[text()='{}']")
    locatorInputNumberPhone = (By.XPATH, "//input[@name='serviceNumber']")
    locatorInputSelectAmount = (By.XPATH, "//div[@id='mui-component-select-amount']")
    locatorCheckTotalAmount = (By.XPATH, "//h5[contains(text(),'Total de la recarga')]/following-sibling::h5[contains(.,'Bs.{}')]")
