from bson import ObjectId

from app import db
from app.core.entities.order import Element
from app.db.repositories.interfaces.command import ICommandRepository
from app.db.repositories.mongo_repositories import OptionalOCCRepository, MongoStandardRepository, MongoOCCRepository


class MongoCommandRepository(ICommandRepository):
    @staticmethod
    def _get_db():
        return db.get_collection("order")

    def get_version(self, order_id: str, element: Element) -> int:
        result = self._get_db().find_one(
            {
                "_id": ObjectId(order_id),
                "current_command": {
                    "$elemMatch": {
                        "section": element.section,
                        "element": element.element,
                        "variants": {
                            "$all": [variant.model_dump() for variant in element.variants]
                        },
                        "extras": {
                            "$all": [extra for extra in element.extras]
                        },
                        "ingredients": {
                            "$all": [ingredient for ingredient in element.ingredients]
                        }
                    }
                }
            },
            {
                "current_command.$": True
            }
        )

        if not result:
            raise Exception(f"No order found with order_id {order_id}")
        if 'current_command' not in result or len(result['current_command']) == 0:
            raise Exception("The specified element was not found in the current_command array")
        return result['current_command'][0]['version']

    def add(self, order_id: str, element: Element, version: int):
        pass

    def update(self, order_id: str, element: Element, version: int) -> Element:
        pass

    def remove(self, order_id: str, element: Element, version: int):
        pass
