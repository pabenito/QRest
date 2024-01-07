from app.extra.entities.order import ReceiptElement


class ToBePaidServices:
    def get_to_be_paid_for_client(self, to_be_paid: list[ReceiptElement], client: str) -> list[ReceiptElement]:
        to_be_paid_for_client = []
        for element in to_be_paid:
            if client in element.clients:
                element_for_client = element.model_copy(update={
                    "clients": [client] * element.clients.count(client),
                    "total": element.price * element.clients.count(client)})
                to_be_paid_for_client.append(element_for_client)
        return to_be_paid_for_client


