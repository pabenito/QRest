class EntityValidationException(Exception):
    def __init__(self, resource: str, message: str):
        super().__init__(f"{resource} is not valid: {message}.")


class InvalidInputException(Exception):
    def __init__(self, message: str):
        super().__init__(message)