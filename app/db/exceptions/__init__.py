from typing import Optional


class PersistenceException(Exception):
    pass


class DocumentNotFoundException(PersistenceException):
    def __init__(self, document: str, key: str, value: str):
        super().__init__(f"There is no {document} with {key} {value}.")


class FieldNotFoundException(PersistenceException):
    def __init__(self, document: str, key: str, value: str, field: str):
        super().__init__(f"The {document} with {key} {value}, does not have field {field}.")


class FieldDoesNotMatchException(PersistenceException):
    def __init__(self, document: str, key: str, value: str, field: str, field_value: str):
        super().__init__(f"The {document} with {key} {value}, does not have field {field} with value {field_value}.")


class DocumentAlreadyExistsException(PersistenceException):
    def __init__(self, resource: str, key: str, value: str):
        super().__init__(f"{resource} with {key} {value} already exists.")


class FieldAlreadyExistsException(PersistenceException):
    def __init__(self, document: str, key: str, value: str, field: str):
        super().__init__(f"The {document} with {key} {value} already has field {field}.")


class OperationFailedException(PersistenceException):
    def __init__(self, document: str, key: str, value: str, field: Optional[str]):
        message_append = f" with field {field}" if field else ""
        super().__init__(f"Unknown error. {document} with {key} {value}{message_append}.")


class PersistenceExceptionFactory:
    def __init__(self, collection: str):
        self.collection = collection
        self.key = "_id"

    def document_not_found(self, value: str) -> DocumentNotFoundException:
        return DocumentNotFoundException(self.collection, self.key, value)

    def field_not_found(self, value: str, field: str) -> FieldNotFoundException:
        return FieldNotFoundException(self.collection, self.key, value, field)

    def field_does_not_match(self, value: str, field: str, field_value: str) -> FieldDoesNotMatchException:
        return FieldDoesNotMatchException(self.collection, self.key, value, field, field_value)

    def field_already_exists(self, value: str, field: str) -> FieldAlreadyExistsException:
        return FieldAlreadyExistsException(self.collection, self.key, value, field)

    def operation_failed(self, value: str, field: Optional[str]) -> OperationFailedException:
        return OperationFailedException(self.collection, self.key, value, field)
