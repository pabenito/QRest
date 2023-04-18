import os

from tempfile import NamedTemporaryFile

from invoice_generator.api import Invoice, Item, Client, Provider, Creator
from invoice_generator.pdf import SimpleInvoice

# choose english as language
os.environ["INVOICE_LANG"] = "es"

client = Client('Client company')
provider = Provider('QRest', bank_account='2600420569', bank_code='2010')
creator = Creator('John Doe')

invoice = Invoice(client, provider, creator)
invoice.currency_locale = 'en_US.UTF-8'
invoice.add_item(Item(32, 600, description="Item 1"))
invoice.add_item(Item(60, 50, description="Item 2", tax=21))
invoice.add_item(Item(50, 60, description="Item 3", tax=0))
invoice.add_item(Item(5, 600, description="Item 4", tax=15))

pdf = SimpleInvoice(invoice)
pdf.gen("InvoiceGenerator.pdf", generate_qr_code=True)