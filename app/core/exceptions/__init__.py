class EntityValidationException:
    def __init__(self, resource: str, message: str):
        super().__init__(f"{resource} is not valid: {message}.")


class InvalidInputException:
    def __init__(self, resource: str, message: str):
        super().__init__(message)