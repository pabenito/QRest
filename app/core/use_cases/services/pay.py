from app.core.entities.order import ReceiptElement

from copy import deepcopy


class PayServices:
    def get_to_be_paid_after_payment(self, to_be_paid: list[ReceiptElement], elements: list[ReceiptElement]) -> list[ReceiptElement]:
        dict_to_be_paid = self.create_dict_from_receipt(deepcopy(to_be_paid))
        for element in elements:
            if element.element not in dict_to_be_paid:
                raise ValueError(f"Element {element.element} not found in to_be_paid {dict_to_be_paid.keys()}")
            dict_to_be_paid[element.element].quantity -= element.quantity
            dict_to_be_paid[element.element].clients = self.list_less_list(dict_to_be_paid[element.element].clients, element.clients)
            dict_to_be_paid[element.element].total -= element.quantity * dict_to_be_paid[element.element].price
            if dict_to_be_paid[element.element].quantity == 0:
                del dict_to_be_paid[element.element]
        return list(dict_to_be_paid.values())



    @staticmethod
    def create_dict_from_receipt(receipt: list[ReceiptElement]) -> dict[str, ReceiptElement]:
        receipt_dict = {}
        for element in receipt:
            receipt_dict[element.element] = element
        return receipt_dict

    @staticmethod
    def list_less_list(list1, list2):
        result = deepcopy(list1)
        for element in list2:
            if element in result:
                result.remove(element)
        return result
