from app.core.exceptions import *


class OrderException(QRestException):
    pass


class OrderNotFoundException(ResourceNotFoundException):
    def __init__(self, value: str):
        super().__init__("Order", "id", value)


class OrderAlreadyExistsException(ResourceAlreadyExistsException, OrderException):
    def __init__(self, value: str):
        super().__init__("Order", "id", value)


class OrderValidationException(EntityValidationException, OrderException):
    def __init__(self, message: str):
        super().__init__("Order", message)


class OrderInvalidInputException(InvalidInputException, OrderException):
    def __init__(self, message: str):
        super().__init__(message)


class OrderOperationFailedException(OperationFailedException, OrderException):
    def __init__(self, message: str):
        super().__init__(message)


class OrderConcurrencyCollisionException(ConcurrencyCollisionException, OrderException):
    def __init__(self, id: str, method: str, expected_version: int):
        super().__init__("order", id, method, expected_version)
