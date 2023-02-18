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
			"width": 250
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
            "width": 150
        },
        {
            "label": _("تاريخ تسجيل العمل المسند"),
            "fieldname": "assigned_date",
            "fieldtype": "Date",
            "width": 200
        },
        {
            "label": _("العمل المسند"),
            "fieldname": "work_assigned",
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
    if filters.get("officers"):
        conditions += "and officers = %(officers)s"
    if filters.get("from_date"):
        conditions += " and assigned_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and assigned_date <= %(to_date)s"
    if filters.get("rank"):
        conditions += "and rank = %(rank)s"
    if filters.get("work_assigned"):
        conditions += "and work_assigned = %(work_assigned)s"
    if filters.get("notes"):
        conditions += "and notes = %(notes)s"


    result = []
    item_results = frappe.db.sql("""
        select
            officers, employee_name, rank, work_assigned, assigned_date, notes
        from
            `tabRecording Work Assigned To Officer`
        where
            `tabRecording Work Assigned To Officer`.docstatus = 1
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'officers': item_dict.officers,
            'employee_name': item_dict.employee_name,
            'rank': item_dict.rank,
            'work_assigned': item_dict.work_assigned,
            'notes': item_dict.notes,
            'assigned_date': item_dict.assigned_date,
        }
        result.append(data)
    return result