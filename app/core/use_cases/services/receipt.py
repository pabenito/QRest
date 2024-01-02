from app.core.entities.menu import Section
from app.core.entities.order import ReceiptElement, Command


class ReceiptServices:
    def generate_receipt_from_commands(self, menu: list[Section], commands: list[Command]) -> list[ReceiptElement]:
        price_dict = self._generate_price_dict(menu)
        receipt = {}
        for command in commands:
            for element in command.elements:
                if element.element not in price_dict:
                    raise ValueError(f"Element {element.element} not found in menu")
                if element.element in receipt:
                    receipt[element.element].quantity += element.quantity
                    receipt[element.element].clients.extend(element.clients)
                    receipt[element.element].total += element.quantity * price_dict[element.element]
                else:
                    receipt[element.element] = (ReceiptElement(
                        section=element.section,
                        element=element.element,
                        quantity=element.quantity,
                        clients=element.clients,
                        price=price_dict[element.element],
                        total=element.quantity * price_dict[element.element]))
        return list(receipt.values())

    @staticmethod
    def get_receipt_for_client(self, receipt: list[ReceiptElement], client: str) -> list[ReceiptElement]:
        receipt_for_client = []
        for element in receipt:
            if client in element.clients:
                element_for_client = element.model_copy(update={
                    "clients": [client] * element.clients.count(client),
                    "total": element.price * element.clients.count(client)})
                receipt_for_client.append(element_for_client)
        return receipt_for_client

    @staticmethod
    def _generate_price_dict(menu: list[Section]) -> dict[str, float]:
        price_dict = {}
        for section in menu:
            if section.elements is not None:
                for element in section.elements:
                    price_dict[element.name] = element.price
        return price_dict

