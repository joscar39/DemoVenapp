import time
import traceback

import allure
from allure_commons.types import AttachmentType
from selenium.common import NoSuchElementException, ElementNotInteractableException, TimeoutException, \
    WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configurations.config import Datatest


class BaseActions:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    ########################## CONFIGURATION OF BROWSER AND SET VALUES OR DATA ###############################

    @staticmethod
    def time_wait(seconds):
        """
        Funcion que permite hacer una espera obligatoria por un intervalo de tiempo
        :param seconds: segundos totales de espera
        """
        time.sleep(seconds)

    def getTitleWeb(self):
        """
        Metodo para Obtener el title de una pagina web
        :return: Retorna el valor del title
        """
        try:
            val = None
            self.driver.implicitly_wait(10)
            val = self.driver.title
            print(f"Se encontro el title: {val}")
            allure.attach(val, "Obtencion de title")
            return str(val)
        except Exception as e:
            message = f"Error desconocido al obtener la URL actual del navegador\nLog: {traceback.format_exc()}"
            raise RuntimeError(message) from e

    def getCurrentUrl(self):
        """
        Metodo que permite obtener la URL actual del navegador y retornarlo
        :return: Valor obtenido en la URL actual del navegador manejado por selenium
        """
        try:
            return self.driver.current_url

        except Exception as e:
            message = f"Error desconocido al obtener la URL actual del navegador\nLog: {traceback.format_exc()}"
            raise RuntimeError(message) from e

    ##################################### SEARCH AND SEND; INPUTS, ELEMENTS, TEXT AND SELECTORS ################

    def sendTextBySelector(self, by_type: str, selector: str, text: str or int or float, seconds: float):
        """
        Metodo que permite enviar texto sobre un input a traves de localizador por selectores

        :param by_type: tipo de atributo BY a utilizar (XPATH, ID, CSS, ETC)
        :param selector: Localizador utilizado para identificar el selector
        :param text: Texto que se enviara al input, sea numerico o alfabetico se envia en formato str
        :param seconds: segundos que tardara el metodo en esperar que el input a recibir el texto este presente
        """

        try:
            ele = None
            ele = WebDriverWait(self.driver, seconds).until(EC.visibility_of_element_located((by_type, selector)))
            ele.clear()
            ele.send_keys(text)
            BaseActions.time_wait(0.5)
            print(f"Cargado el texto {text} correctamente")
            allure.attach(f"Cargado el texto {text} correctamente", "Envio de texto en input")
        except (NoSuchElementException, ElementNotInteractableException, TimeoutException) as e:
            message = f"No se pudo interactuar con el input:\nElemento: {selector} (tipo: {by_type})\nLog: {traceback.format_exc()}"
            raise RuntimeError(message) from e
        except WebDriverException as e:
            message = f"Error general de WebDriver al enviar el texto:\nElemento: {selector} (tipo: {by_type})\nLog: {traceback.format_exc()}"
            raise RuntimeError(message) from e
        except Exception as e:
            message = f"Error desconocido al enviar el texto:\nElemento: {selector} (tipo: {by_type})\nLog: {traceback.format_exc()}"
            raise RuntimeError(message) from e

    def scrollToElementIsVisibility(self, by_type: str, selector: str, seconds: float):
        """
        Hacer scroll hacia un elemento específico

        :param seconds: Tiempo de espera hasta encontrar el elemento.
        :param by_type: Ingresar el tipo de selector a usar, si es XPATH, CLASS_NAME, ID, etc.
        :param selector: Ruta del elemento hacia donde se desea realizar el scroll.

        """

        try:
            val = WebDriverWait(self.driver, seconds).until(
                EC.presence_of_element_located((by_type, selector)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            if val.is_displayed():
                print(f"Desplazando al elemento {selector}")
                BaseActions.time_wait(0.5)
        except (NoSuchElementException, ElementNotInteractableException, TimeoutException) as e:
            message = f"No se pudo interactuar con el elemento:\nElemento: {selector} (tipo: {by_type})\nLog: {traceback.format_exc()}"
            raise RuntimeError(message) from e
        except WebDriverException as e:
            message = f"Error general de WebDriver al hacer scroll:\nElemento: {selector} (tipo: {by_type})\nLog: {traceback.format_exc()}"
            raise RuntimeError(message) from e
        except Exception as e:
            message = f"Error desconocido al hacer scroll:\nElemento: {selector} (tipo: {by_type})\nLog: {traceback.format_exc()}"
            raise RuntimeError(message) from e

    @staticmethod
    def getNearestAmountOptions(Entered_amount, Telemarketer, Promotion):
        """
        Encuentra el monto más cercano al ingresado por el usuario
        dentro de una lista de montos disponibles para el pago de recargas.

        Args:
            Entered_amount: El monto ingresado por el usuario (puede ser decimal).
            Telemarketer: Teleoperador seleccionado.
            Promotion: Indicador si el teleoperador tiene habilitado promociones de recarga

        Returns:
            El monto más cercano al ingresado por el usuario (cadena de texto) y un monto de promocion si aplica si no envia 0
            o un mensaje de error si el monto ingresado no es válido.
        """

        try:
            entered_amount = float(Entered_amount)  # Convertir a número (maneja decimales)
        except ValueError:
            return "Error: Monto ingresado no válido."

        if entered_amount < 0:
            return "Error: Monto ingresado debe ser mayor o igual a 0."

        available_amounts = None
        if Telemarketer == "1":
            available_amounts = Datatest.LIST_AMOUNT_DIGITEL
        elif Telemarketer == "2":
            available_amounts = Datatest.LIST_AMOUNT_MOVISTAR
        elif Telemarketer == "3":
            available_amounts = Datatest.LIST_AMOUNT_MOVILNET

        if available_amounts is not None:
            # Crear una list comprehension que permita obtener la diferencia entre el valor ingresado y los montos disponibles
            differences = [abs(entered_amount - amount) for amount in available_amounts]

            # Retorna el indice del valor menor en la lista de differences
            index_of_min_difference = differences.index(min(differences))
            add_promotion = None
            if str(Promotion).lower() == "yes":

                add_promotion = (index_of_min_difference + 1) * Datatest.PROMOTION_RECHARGE #Agregar +1 para compensar posicion cero

                sum_promotion = int(available_amounts[index_of_min_difference]) + add_promotion

                return str(available_amounts[index_of_min_difference]), str(sum_promotion)
            else:
                return str(available_amounts[index_of_min_difference])
        else:
            raise RuntimeError("la opcion de teleoperador seleccionado no existe en la lista disponible")


    #################### CLICK ON ELEMENT #################################################


    def clickOnElementBySelector(self, by_type: str, selector: str, seconds: float):
        """
        Metodo para Hacer click sobre un elemento que se localice por selectores
        :param by_type: tipo de atributo BY a utilizar (XPATH, ID, CSS, ETC)
        :param selector: Localizador utilizado para identificar el selector
        :param seconds: tiempo de espera mientras se localiza el elemento
        """

        try:
            ele = None
            ele = WebDriverWait(self.driver, seconds).until(EC.element_to_be_clickable
                                                            ((by_type, selector)))
            ele.click()
            print(f"Se realizo click sobre el elemento con el selector: {selector} de tipo {by_type}")
            allure.attach(f"Se realizo click sobre el elemento con el selector: {selector} de tipo {by_type}",
                          "Click sobre elemento localizado con selector")
            BaseActions.time_wait(0.5)
        except (NoSuchElementException, ElementNotInteractableException, TimeoutException) as e:
            message = f"No se pudo interactuar con el elemento:\nElemento: {selector} (tipo: {by_type})\nLog: {traceback.format_exc()}"
            raise RuntimeError(message) from e
        except WebDriverException as e:
            message = f"Error general de WebDriver al hacer click:\nElemento: {selector} (tipo: {by_type})\nLog: {traceback.format_exc()}"
            raise RuntimeError(message) from e
        except Exception as e:
            message = f"Error desconocido al hacer click:\nElemento: {selector} (tipo: {by_type})\nLog: {traceback.format_exc()}"
            raise RuntimeError(message) from e

    ####################### EVALUATE ELEMENT TO RETURN BOOLEAN OR RESULT ####################################

    def findElementIsDisplayed(self, by_type: str, selector: str, seconds: float):
        """
        Metodo que permite localizar un elemento a travez de un selector y retorna True si es localizado exitosamente

        :param by_type: tipo de atributo BY a utilizar (XPATH, ID, CSS, ETC)
        :param selector: Localizador utilizado para identificar el selector
        :param seconds: Tiempo de espera para que el elemento sea localizado
        :return: True si localiza el elemento, o False si no lo encuentra
        """

        try:
            element = None
            element = WebDriverWait(self.driver, seconds).until(EC.visibility_of_element_located
                                                                ((by_type, selector)))
            if element.is_displayed():
                print(f"Se encontro en pantalla el elemento: {selector} de tipo {by_type}")
                allure.attach(f"Se encontro en pantalla el elemento: {selector} de tipo {by_type}",
                              "verificacion de elemento")
                return True
        except TimeoutException:
            print(f"Error: Tiempo de espera agotado mientras se buscaba el elemento: {selector} de tipo {by_type}")
            allure.attach(
                f"Error: Tiempo de espera agotado mientras se buscaba el elemento: {selector} de tipo {by_type}")
            return False
        except NoSuchElementException:
            print(f"Error: No se encontró el elemento: {selector} de tipo {by_type}")
            allure.attach(f"Error: No se encontró el elemento: {selector} de tipo {by_type}")
            return False
        except ElementNotInteractableException:
            print(f"Error: No se puede interactuar con el elemento: {selector} de tipo {by_type}")
            allure.attach(f"Error: No se puede interactuar con el elemento: {selector} de tipo {by_type}")
            return False
        except Exception:
            print(f"Error desconocido: No se localizo el elemento: {selector} de tipo {by_type}")
            allure.attach(f"Error desconocido: No se localizo el elemento: {selector} de tipo {by_type}")
            return False


    #################### ALLURE SCREENSHOT AND UPLOAD FILE #################################

    def screenshot(self, name: str):
        """
        Metodo para capturar evidencia en allure
        :param name: nombre que se le asignara a la evidencia
        """

        allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
