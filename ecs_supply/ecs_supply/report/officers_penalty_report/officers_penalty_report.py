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
			"label": _("اسم الضابط"),
			"fieldname": "employee_name",
			"fieldtype": "Data",
			"width": 200
		},
        {
            "label": _("رقم الضابط"),
            "fieldname": "officers",
            "fieldtype": "Link",
			"options": "Employee",
            "width": 150
        },
        {
            "label": _("الرتبة"),
            "fieldname": "rank",
            "fieldtype": "Data",
            "width": 130
        },
        {
            "label": _("تاريخ الجزاء"),
            "fieldname": "penalty_date",
            "fieldtype": "Date",
            "width": 120
        },
		{
			"label": _("نوع الجزاء"),
			"fieldname": "penalty_type",
			"fieldtype": "Data",
			"width": 200
		},
        {
            "label": _("السبب"),
            "fieldname": "reason",
            "fieldtype": "Data",
            "width": 300
        },
    ]


def get_data(filters, columns):
    item_price_qty_data = []
    item_price_qty_data = get_item_price_qty_data(filters)
    return item_price_qty_data


def get_item_price_qty_data(filters):
    conditions = ""
    if filters.get("officers"):
        conditions += "and officers = %(officers)s"
    if filters.get("rank"):
        conditions += "and rank = %(rank)s"
    if filters.get("penalty_type"):
        conditions += "and penalty_type = %(penalty_type)s"
    if filters.get("from_date"):
        conditions += " and penalty_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and penalty_date <= %(to_date)s"
    if filters.get("reason"):
        conditions += "and reason = %(reason)s"

    result = []
    item_results = frappe.db.sql("""
        select
            officers, employee_name, rank, penalty_type, penalty_date, reason
        from
            `tabOfficers Penalty`
        where
            `tabOfficers Penalty`.docstatus = 1
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'officers': item_dict.officers,
            'employee_name': item_dict.employee_name,
            'rank': item_dict.rank,
            'penalty_type': item_dict.penalty_type,
            'penalty_date': item_dict.penalty_date,
            'reason': item_dict.reason,
        }
        result.append(data)
    return result