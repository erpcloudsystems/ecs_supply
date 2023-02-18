from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import in_words


@frappe.whitelist()
def before_insert(doc, method=None):
    pass
@frappe.whitelist()
def after_insert(doc, method=None):
    pass
@frappe.whitelist()
def onload(doc, method=None):
    pass
@frappe.whitelist()
def before_validate(doc, method=None):
    pass
@frappe.whitelist()
def validate(doc, method=None):
    totals = 0
    totals1 = 0
    for d in doc.buying_order_items:
        d.amount = 0
        d.amount = d.quantity * d.rate
        
        totals += d.quantity
        totals1 += d.amount
    doc.total_quantity = totals
    doc.total_amount = totals1
    doc.in_word = in_words(doc.total_amount)
@frappe.whitelist()
def on_submit(doc, method=None):
    pass
@frappe.whitelist()
def on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def before_save(doc, method=None):
    pass
@frappe.whitelist()
def before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def on_update(doc, method=None):
    pass
