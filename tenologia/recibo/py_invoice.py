from datetime import datetime, date
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item, Transaction
from pyinvoice.templates import SimpleInvoice

doc = SimpleInvoice('pyinvoice.pdf')

doc.invoice_info = InvoiceInfo(None, datetime.now(), None)  # Invoice info, optional

# Add Item
doc.add_item(Item('Agua', 'Fría', 1, 1.1))
doc.add_item(Item('Coca-cola', 'Con limón', 2, 2.2))
doc.add_item(Item('Nestea', 'Con limón', 3, 3.3))

# Tax rate, optional
doc.set_item_tax_rate(21)

doc.finish()