from features.pom.Login_Page import LoginPage


class Application:

    # Constructor de la clase Application
    def __init__(self, driver):
        # Instancias de las clases de los Page, reciben como parametro el objeto driver
        self.LoginPage = LoginPage(driver)