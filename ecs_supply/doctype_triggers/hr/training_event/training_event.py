from __future__ import unicode_literals
import frappe
from frappe import _


@frappe.whitelist()
def before_insert(doc, method=None):
    event_name = frappe.db.sql(""" select max(event_name) as max from `tabTraining Event`""",as_dict=1)
    for x in event_name :
        doc.event_name = int(x.max) +1
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
    pass
@frappe.whitelist()
def on_submit(doc, method=None):
    employee = frappe.get_doc("Employee", self.employee)
    log = employee.append("attendance_request_logs", {})
    log.explanation = self.explanation
    log.country = self.country
    log.from_date = self.from_date
    log.to_date = self.to_date
    log.save()
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
