from selenium.webdriver.common.by import By


class LoginPage:

    locatorInputEmail = (By.XPATH, "//input[@Placeholder='Email']")
    locatorInputPassword = (By.XPATH, "//input[@Placeholder='Contraseña']")
    locatorButtonLogin = (By.XPATH, "//button[@type='button']/div/p[contains(text(), 'Iniciar sesión')]")
    locatorCheckTextRechargeLoginSuccess = (By.XPATH, "//h6[contains(text(), 'Recargas')]")
    LocatorCheckTextLotteryLoginSuccess = (By.XPATH, "//h6[contains(text(), 'Lotería')]")