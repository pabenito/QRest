class QRestException(Exception):
    pass


class ResourceNotFoundException(QRestException):
    def __init__(self, resource: str, key: str, value: str):
        super().__init__(f"{resource} with {key} {value} not found.")


class ResourceAlreadyExistsException(QRestException):
    def __init__(self, resource: str, key: str, value: str):
        super().__init__(f"{resource} with {key} {value} already exists.")


class EntityValidationException(QRestException):
    def __init__(self, resource: str, message: str):
        super().__init__(f"{resource} is not valid: {message}.")


class InvalidInputException(QRestException):
    def __init__(self, resource: str, message: str):
        super().__init__(message)


class OperationFailedException(QRestException):
    def __init__(self, resource: str, message: str):
        super().__init__(message)


class ConcurrencyCollisionException(QRestException):
    def __init__(self, resource: str, id: str, method: str, expected_version: int):
        super().__init__(f"{resource} with id '{id}' mismatch version in method {method}. Expected version: '{expected_version}'.")
