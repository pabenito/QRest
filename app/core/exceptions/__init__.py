class QRestException(Exception):
    pass


class ResourceNotFoundException(QRestException):
    def __init__(self, value: str):
        self.entity = "Resource"
        self.key = "id"
        super().__init__(f"{self.entity} with {self.key} {value} not found.")


class ResourceAlreadyExistsException(QRestException):
    def __init__(self, value: str):
        self.entity = "Resource"
        self.key = "id"
        super().__init__(f"{self.entity} with {self.key} {value} already exists.")


class EntityValidationException(QRestException):
    def __init__(self, message: str):
        self.entity = "Entity"
        super().__init__(f"{self.entity} is not valid: {message}")


class InvalidInputException(QRestException):
    def __init__(self, message: str):
        super().__init__(message)


class OperationFailedException(QRestException):
    def __init__(self, message: str):
        super().__init__(message)
