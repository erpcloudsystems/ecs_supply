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
			"label": _("اسم الموظف"),
			"fieldname": "employee_name",
			"fieldtype": "Data",
			"width": 200
		},
        {
            "label": _("رقم الموظف"),
            "fieldname": "civilians",
            "fieldtype": "Link",
            "options": "Employee",
            "width": 200
        },
        {
            "label": _("تاريخ التكريم"),
            "fieldname": "date",
            "fieldtype": "Date",
            "width": 130
        },
		{
			"label": _("نوع التكريم"),
			"fieldname": "type_of_honor",
			"fieldtype": "Data",
			"width": 200
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
    if filters.get("civilians"):
        conditions += "and civilians = %(civilians)s"
    if filters.get("type_of_honor"):
        conditions += "and type_of_honor = %(type_of_honor)s"
    if filters.get("from_date"):
        conditions += " and date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and date <= %(to_date)s"
    if filters.get("notes"):
        conditions += "and notes = %(notes)s"

    result = []
    item_results = frappe.db.sql("""
        select
            civilians, employee_name, type_of_honor, date, notes
        from
            `tabCivilians Honors`
        where
            `tabCivilians Honors`.docstatus = 1
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'civilians': item_dict.civilians,
            'employee_name': item_dict.employee_name,
            'type_of_honor': item_dict.type_of_honor,
            'date': item_dict.date,
            'notes': item_dict.notes,
        }
        result.append(data)
    return result