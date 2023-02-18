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
            "width": 120
        },
		{
			"label": _("من تاريخ"),
			"fieldname": "from_date",
			"fieldtype": "Date",
			"width": 130
		},
		{
			"label": _("الي تاريخ"),
			"fieldname": "to_date",
			"fieldtype": "Date",
			"width": 130
		},
        {
            "label": _("اسم المؤتمر"),
            "fieldname": "conference_name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("جهة المؤتمر"),
            "fieldname": "conference_side",
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
    if filters.get("officers"):
        conditions += "and officers = %(officers)s"
    if filters.get("from_date"):
        conditions += " and from_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and to_date <= %(to_date)s"
    if filters.get("rank"):
        conditions += "and rank = %(rank)s"
    if filters.get("conference_name"):
        conditions += "and conference_name = %(conference_name)s"
    if filters.get("conference_side"):
        conditions += "and conference_side = %(conference_side)s"

    result = []
    item_results = frappe.db.sql("""
        select
            officers, employee_name, rank, conference_name, conference_side, from_date, to_date
        from
            `tabOfficer Conferences Details`
        where
            `tabOfficer Conferences Details`.docstatus = 1
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'officers': item_dict.officers,
            'employee_name': item_dict.employee_name,
            'rank': item_dict.rank,
            'conference_name': item_dict.conference_name,
            'conference_side': item_dict.conference_side,
            'from_date': item_dict.from_date,
            'to_date': item_dict.to_date,
        }
        result.append(data)
    return result