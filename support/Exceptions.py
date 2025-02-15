class ErrorStepException(Exception):
    """Excepción detectar errores capturados de manera personalizada.
    Atributos:
    message_original (str, optional): El mensaje de la excepción original que causó este error.    """

    def __init__(self, message="Ups Houston we have a problem", message_original=None):
        super().__init__(message)
        self.message_original = message_original