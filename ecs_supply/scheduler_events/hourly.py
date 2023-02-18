from __future__ import unicode_literals
import frappe
from frappe i
from datetime import date
frappe.whitelist()
def hourly():
    today = date.today()
    employee = frappe.get_list('Employee', filters={'military_end_date': today})
    for x in employee:
        frappe.db.set_value('Employee', x.name, 'status', "Left")
