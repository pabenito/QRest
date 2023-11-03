from typing import Optional


class QRestException(Exception):
    pass


class DocumentNotFoundException(QRestException):
    def __init__(self, document: str, key: str, value: str):
        super().__init__(f"There is no {document} with {key} {value}.")


class FieldNotFoundException(QRestException):
    def __init__(self, document: str, key: str, value: str, field: str):
        super().__init__(f"The {document} with {key} {value}, does not have field {field}.")


class FieldDoesNotMatchException(QRestException):
    def __init__(self, document: str, key: str, value: str, field: str, field_value: str):
        super().__init__(f"The {document} with {key} {value}, does not have field {field} with value {field_value}.")


class DocumentAlreadyExistsException(QRestException):
    def __init__(self, resource: str, key: str, value: str):
        super().__init__(f"{resource} with {key} {value} already exists.")


class FieldAlreadyExistsException(QRestException):
    def __init__(self, document: str, key: str, value: str, field: str):
        super().__init__(f"The {document} with {key} {value} already has field {field}.")


class EntityValidationException(QRestException):
    def __init__(self, resource: str, message: str):
        super().__init__(f"{resource} is not valid: {message}.")


class InvalidInputException(QRestException):
    def __init__(self, resource: str, message: str):
        super().__init__(message)


class OperationFailedException(QRestException):
    def __init__(self, document: str, key: str, value: str, field: Optional[str]):
        message_append = f" with field {field}" if field else ""
        super().__init__(f"Unknown error. {document} with {key} {value}{message_append}.")
