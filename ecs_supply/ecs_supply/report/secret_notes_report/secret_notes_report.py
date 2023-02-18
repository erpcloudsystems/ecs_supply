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
			"width": 200
		},
        {
            "label": _("رقم الفرد"),
            "fieldname": "policemen",
            "fieldtype": "Link",
			"options": "Employee",
            "width": 150
        },
        {
            "label": _("الرتبة"),
            "fieldname": "policemen_rank",
            "fieldtype": "Data",
            "width": 150
        },
		{
			"label": _("قرار الوضع"),
			"fieldname": "position_decision",
			"fieldtype": "Data",
			"width": 150
		},
        {
            "label": _("تاريخ الوضع"),
            "fieldname": "position_date",
            "fieldtype": "Date",
            "width": 120
        },
		{
			"label": _("قرار الرفع"),
			"fieldname": "lifting_decision",
			"fieldtype": "Data",
			"width": 150
		},
        {
            "label": _("تاريخ الرفع"),
            "fieldname": "lifting_date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": _("السبب"),
            "fieldname": "reason",
            "fieldtype": "Data",
            "width": 150
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
    if filters.get("policemen_rank"):
        conditions += "and policemen_rank = %(policemen_rank)s"
    if filters.get("position_decision"):
        conditions += "and position_decision = %(position_decision)s"
    if filters.get("from_date"):
        conditions += " and position_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and position_date <= %(to_date)s"
    if filters.get("lifting_decision"):
        conditions += "and lifting_decision = %(lifting_decision)s"
    if filters.get("lifting_date"):
        conditions += "and lifting_date = %(lifting_date)s"
    if filters.get("reason"):
        conditions += "and reason = %(reason)s"

    result = []
    item_results = frappe.db.sql("""
        select
            policemen, employee_name, policemen_rank, position_decision, position_date, lifting_decision, lifting_date, reason
        from
            `tabSecret Notes`
        where
            `tabSecret Notes`.docstatus = 1
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'policemen': item_dict.policemen,
            'employee_name': item_dict.employee_name,
            'policemen_rank': item_dict.policemen_rank,
            'position_decision': item_dict.position_decision,
            'position_date': item_dict.position_date,
            'lifting_decision': item_dict.lifting_decision,
            'lifting_date': item_dict.lifting_date,
            'reason': item_dict.reason,
        }
        result.append(data)
    return result