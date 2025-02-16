

class Datatest:

    #Datos de URL para levantar desde el navegador
    URL_WEB = "https://venapp.com/"

    #Ejecucion de modo headless(sin pantalla), True or False
    HEADLESS_MODE = False

    #Opciones disponibles de navegador: 'microsoft edge', 'chrome' y 'firefox'
    BROWSER = "chrome"

    #Opciones de teleoperadoras
    OPTIONS_TELEMARKETER = {"Digitel": "1", "Movistar": "2", "Movilnet": "3"}

    #Listado de mostos disponibles a cancelar recarga por teleoperadoras
    LIST_AMOUNT_MOVISTAR = [60, 120, 180, 240, 300, 360, 420, 480]
    LIST_AMOUNT_MOVILNET = [60, 120, 180, 240, 300, 360, 420, 480]
    LIST_AMOUNT_DIGITEL = [50, 100, 150, 200, 250, 300, 350, 400]

    #Diccionario de textos corregidos de tipo de servicios
    SYNTAX_TYPE_SERVICE = {
        "movil": "Móvil",
        "movile": "Móvil",
        "Movil": "Móvil",
        "Movile": "Móvil",
        "fijo": "Fijo",
        "fixed": "Fijo",
        "Fixed": "Fijo",
        "internet": "Internet",
        "Internet": "Internet"
    }