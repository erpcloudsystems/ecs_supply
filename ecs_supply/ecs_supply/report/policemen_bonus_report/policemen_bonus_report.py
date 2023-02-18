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
            "width": 130
        },
        {
            "label": _("تاريخ العلاوة"),
            "fieldname": "bonus_date",
            "fieldtype": "Date",
            "width": 100
        },
		{
			"label": _("نوع العلاوة"),
			"fieldname": "bonus_type",
			"fieldtype": "Data",
			"width": 150
		},
        {
            "label": _("السنة"),
            "fieldname": "year",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": _("الملاحظات"),
            "fieldname": "notes",
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
    if filters.get("policemen"):
        conditions += "and policemen = %(policemen)s"
    if filters.get("bonus_type"):
        conditions += "and bonus_type = %(bonus_type)s"
    if filters.get("from_date"):
        conditions += " and bonus_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and bonus_date <= %(to_date)s"
    if filters.get("year"):
        conditions += "and year = %(year)s"
    if filters.get("notes"):
        conditions += "and notes = %(notes)s"

    result = []
    item_results = frappe.db.sql("""
        select
            policemen, employee_name, bonus_type, year, bonus_date, notes
        from
            `tabPolicemen Bonus`
        where
            `tabPolicemen Bonus`.docstatus = 1
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'policemen': item_dict.policemen,
            'employee_name': item_dict.employee_name,
            'bonus_type': item_dict.bonus_type,
            'bonus_date': item_dict.bonus_date,
            'year': item_dict.year,
            'notes': item_dict.notes,
        }
        result.append(data)
    return result