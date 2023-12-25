from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import nowdate ,getdate

frappe.whitelist()
def daily():
    doctypes = ['Officers Affairs', 'Envestigation Employee', 'The Recruits', 'Human Resources']
    for doctype in doctypes:
        docs = frappe.get_all(doctype, filters={'disabled': 0}, fields=['name'])
        for doc in docs:
            doc_obj = frappe.get_doc(doctype, doc['name'])
            if getdate(doc_obj.date_of_implementation) < getdate(nowdate()):
                frappe.db.set_value(doctype,doc['name'],'disabled',1)         
                frappe.db.commit()