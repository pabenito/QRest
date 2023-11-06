from typing import Optional, Any, List
from abc import ABC, abstractmethod
from pymongo.client_session import ClientSession


class IBasicRepository(ABC):
    @abstractmethod
    def get_all(self, session: Optional[ClientSession] = None):
        pass

    @abstractmethod
    def get(self, id: str, session: Optional[ClientSession] = None):
        pass

    @abstractmethod
    def exists(self, id: str, session: Optional[ClientSession] = None):
        pass

    @abstractmethod
    def create(self, document, session: Optional[ClientSession] = None) -> str:
        pass

    @abstractmethod
    def delete(self, id: str, session: Optional[ClientSession] = None):
        pass


class IStandardRepository(IBasicRepository):

    @abstractmethod
    def get_all_with_query_and_projection(self,
                                          has_attribute: Optional[List[str]] = None,
                                          does_not_have_attribute: Optional[List[str]] = None,
                                          include_projection_attribute: Optional[List[str]] = None,
                                          exclude_projection_attribute: Optional[List[str]] = None,
                                          id_projection: Optional[bool] = None,
                                          session: Optional[ClientSession] = None) -> Any:
        pass

    @abstractmethod
    def get_with_query_and_projection(self, id: str,
                                      has_attribute: Optional[List[str]] = None,
                                      does_not_have_attribute: Optional[List[str]] = None,
                                      include_projection_attribute: Optional[List[str]] = None,
                                      exclude_projection_attribute: Optional[List[str]] = None,
                                      id_projection: Optional[bool] = None,
                                      session: Optional[ClientSession] = None) -> Any:
        pass

    @abstractmethod
    def get_attribute(self, id: str, attribute: str, session: Optional[ClientSession] = None) -> Any:
        pass

    @abstractmethod
    def set_attribute(self, id: str, attribute: str, value, session: Optional[ClientSession] = None):
        pass

    @abstractmethod
    def unset_attribute(self, id: str, attribute: str, session: Optional[ClientSession] = None):
        pass

    @abstractmethod
    def push_to_list_attribute(self, id: str, attribute: str, element, session: Optional[ClientSession] = None):
        pass

    @abstractmethod
    def pull_from_list_attribute(self, id: str, attribute: str, element, session: Optional[ClientSession] = None):
        pass

    @abstractmethod
    def get_from_list_attribute(self, id: str, attribute: str, element, session: Optional[ClientSession] = None) -> Any:
        pass

    @abstractmethod
    def has_attribute(self, id: str, attribute: str, session: Optional[ClientSession] = None) -> bool:
        pass

    @abstractmethod
    def has_element_in_list_attribute(self, id: str, attribute: str, element, session: Optional[ClientSession] = None) -> bool:
        pass
