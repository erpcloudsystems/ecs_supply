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
            "width": 130
        },
		{
			"label": _("الرتبة"),
			"fieldname": "rank",
			"fieldtype": "Data",
			"width": 100
		},
        {
            "label": _("تاريخ التكريم"),
            "fieldname": "date",
            "fieldtype": "Date",
            "width": 130
        },
		{
			"label": _("نوع العلاوة"),
			"fieldname": "bonus_type",
			"fieldtype": "Data",
			"width": 150
		},
        {
            "label": _("سبب التكريم"),
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
    if filters.get("bonus_type"):
        conditions += "and bonus_type = %(bonus_type)s"
    if filters.get("from_date"):
        conditions += " and date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and date <= %(to_date)s"
    if filters.get("rank"):
        conditions += "and rank = %(rank)s"
    if filters.get("reason"):
        conditions += "and reason = %(reason)s"

    result = []
    item_results = frappe.db.sql("""
        select
            officers, employee_name, rank, bonus_type, date, reason
        from
            `tabOfficers Bonus And Decorations`
        where
            `tabOfficers Bonus And Decorations`.docstatus = 1
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'officers': item_dict.officers,
            'employee_name': item_dict.employee_name,
            'rank': item_dict.rank,
            'bonus_type': item_dict.bonus_type,
            'date': item_dict.date,
            'reason': item_dict.reason,
        }
        result.append(data)
    return result