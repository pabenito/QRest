from typing import Optional

from pymongo.client_session import ClientSession


class IBasicRepository:
    def create(self, document, session: Optional[ClientSession] = None) -> str:
        pass

    def delete(self, id: str, session: Optional[ClientSession] = None):
        pass

    def get(self, id: str, session: Optional[ClientSession] = None):
        pass

    def exists(self, id: str, session: Optional[ClientSession] = None):
        pass


class IStandardRepository(IBasicRepository):
    def get_attribute(self, id: str, attribute: str, session: Optional[ClientSession] = None):
        pass

    def set_attribute(self, id: str, attribute: str, value, session: Optional[ClientSession] = None):
        pass

    def unset_attribute(self, id: str, attribute: str, session: Optional[ClientSession] = None):
        pass

    def push_to_list_attribute(self, id: str, attribute: str, value, session: Optional[ClientSession] = None):
        pass

    def pull_from_list_attribute(self, id: str, attribute: str, match: dict, session: Optional[ClientSession] = None):
        pass

    def get_from_list_attribute(self, id: str, attribute: str, match: dict, session: Optional[ClientSession] = None):
        pass

    def has_attribute(self, id: str, attribute: str, session: Optional[ClientSession] = None) -> bool:
        pass

    def has_element_in_list_attribute(self, id: str, attribute: str, match: dict, session: Optional[ClientSession] = None) -> bool:
        pass
