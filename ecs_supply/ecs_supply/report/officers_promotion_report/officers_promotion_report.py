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
            "label": _("تاريخ الترقية"),
            "fieldname": "promotion_date",
            "fieldtype": "Date",
            "width": 130
        },
		{
			"label": _("الرتبة"),
			"fieldname": "current_rank",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("الرتبة الجديدة"),
			"fieldname": "new_rank",
			"fieldtype": "Data",
			"width": 150
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
    if filters.get("officers"):
        conditions += "and officers = %(officers)s"
    if filters.get("from_date"):
        conditions += " and promotion_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and promotion_date <= %(to_date)s"
    if filters.get("current_rank"):
        conditions += "and current_rank = %(current_rank)s"
    if filters.get("new_rank"):
        conditions += "and new_rank = %(new_rank)s"
    if filters.get("notes"):
        conditions += "and notes = %(notes)s"

    result = []
    item_results = frappe.db.sql("""
        select
            officers, employee_name, current_rank, new_rank, promotion_date, notes
        from
            `tabOfficers Promotion`
        where
            `tabOfficers Promotion`.docstatus = 1
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'officers': item_dict.officers,
            'employee_name': item_dict.employee_name,
            'current_rank': item_dict.current_rank,
            'new_rank': item_dict.new_rank,
            'promotion_date': item_dict.promotion_date,
            'notes': item_dict.notes,
        }
        result.append(data)
    return result