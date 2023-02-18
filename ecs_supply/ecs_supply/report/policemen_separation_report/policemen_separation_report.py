# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe import msgprint, _
from frappe.utils import flt


def execute(filters=None):
    columns, data = [], []
    columns = get_columns()
    data = get_data(filters, columns)
    return columns, data


def get_columns():
    return [
        {
            "label": _("اسم الفرد"),
            "fieldname": "employee_name",
            "fieldtype": "Data",
            "width": 250
        },
        {
            "label": _("رقم الفرد"),
            "fieldname": "policemen",
            "fieldtype": "Link",
            "options": "Employee",
            "width": 130
        },
        {
            "label": _("الرتبة"),
            "fieldname": "policemen_rank",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("تاريخ انهاءالخدمة"),
            "fieldname": "separation_begins_on",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": _("رقم القرار"),
            "fieldname": "decision_number",
            "fieldtype": "Data",
            "width": 120
        },
    ]


def get_data(filters, columns):
    item_price_qty_data = []
    item_price_qty_data = get_item_price_qty_data(filters)
    return item_price_qty_data


def get_item_price_qty_data(filters):
    conditions = ""
    if filters.get("policemen"):
        conditions += "and policemen = %(policemen)s"
    if filters.get("decision_number"):
        conditions += "and decision_number = %(decision_number)s"
    if filters.get("from_date"):
        conditions += " and separation_begins_on >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and separation_begins_on <= %(to_date)s"
    if filters.get("reason"):
        conditions += "and reason = %(reason)s"

    result = []
    item_results = frappe.db.sql("""
        select
            policemen, employee_name, decision_number, separation_begins_on, reason, policemen_rank
        from
            `tabPolicemen Separation`
        where
            `tabPolicemen Separation`.docstatus = 1
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'policemen': item_dict.policemen,
            'employee_name': item_dict.employee_name,
            'decision_number': item_dict.decision_number,
            'separation_begins_on': item_dict.separation_begins_on,
            'reason': item_dict.reason,
            'policemen_rank': item_dict.policemen_rank,
        }
        result.append(data)
    return result