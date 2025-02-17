from features.pom.Home_Page import HomePage
from features.pom.Login_Page import LoginPage
from features.pom.Recharger_Page import RechargerPage


class Application:

    # Constructor de la clase Application
    def __init__(self, driver):
        # Instancias de las clases de los Page, reciben como parametro el objeto driver
        self.LoginPage = LoginPage(driver)
        self.HomePage = HomePage(driver)
        self.RechargerPage = RechargerPage(driver)