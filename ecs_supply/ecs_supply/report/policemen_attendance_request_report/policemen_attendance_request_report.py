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
            "width": 120
        },
        {
            "label": _("الرتبة"),
            "fieldname": "policemen_rank",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("الدولة"),
            "fieldname": "country",
            "fieldtype": "Data",
            "width": 120
        },
		{
			"label": _("من تاريخ"),
			"fieldname": "from_date",
			"fieldtype": "Date",
			"width": 120
		},
		{
			"label": _("الي تاريخ"),
			"fieldname": "to_date",
			"fieldtype": "Date",
			"width": 120
		},
        {
            "label": _("النوع"),
            "fieldname": "type",
            "fieldtype": "Data",
            "width": 120
        },
		{
			"label": _("الملاحظات"),
			"fieldname": "notes",
			"fieldtype": "Data",
			"width": 200
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
    if filters.get("from_date"):
        conditions += " and from_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and from_date <= %(to_date)s"
    if filters.get("policemen_rank"):
        conditions += "and policemen_rank = %(policemen_rank)s"
    if filters.get("country"):
        conditions += "and country = %(country)s"
    if filters.get("type"):
        conditions += "and type = %(type)s"
    if filters.get("notes"):
        conditions += "and notes = %(notes)s"


    result = []
    item_results = frappe.db.sql("""
        select
            policemen, employee_name, policemen_rank, country, from_date, to_date, type, notes
        from
            `tabPolicemen Attendance Request`
        where
            `tabPolicemen Attendance Request`.docstatus = 1
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'policemen': item_dict.policemen,
            'employee_name': item_dict.employee_name,
            'policemen_rank': item_dict.policemen_rank,
            'country': item_dict.country,
            'from_date': item_dict.from_date,
            'to_date': item_dict.to_date,
            'type': item_dict.type,
            'notes': item_dict.notes,
        }
        result.append(data)
    return result