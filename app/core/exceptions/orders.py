from app.core.exceptions import *


class OrderException(QRestException):
    pass


class OrderNotFoundException(ResourceNotFoundException, OrderException):
    def __init__(self, value: str):
        self.entity = "Order"
        self.key = "id"
        super().__init__(value)


class OrderAlreadyExistsException(ResourceAlreadyExistsException, OrderException):
    def __init__(self, value: str):
        self.entity = "Order"
        self.key = "id"
        super().__init__(value)


class OrderValidationException(EntityValidationException, OrderException):
    def __init__(self, message: str):
        self.entity = "Order"
        super().__init__(message)


class OrderInvalidInputException(InvalidInputException, OrderException):
    def __init__(self, message: str):
        super().__init__(message)


class OrderOperationFailedException(OperationFailedException, OrderException):
    def __init__(self, message: str):
        super().__init__(message)
