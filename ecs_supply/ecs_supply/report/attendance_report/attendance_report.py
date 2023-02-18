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
			"label": _("الاسم"),
			"fieldname": "employee_name",
			"fieldtype": "Data",
			"width": 200
		},
        {
            "label": _("الرقم/الكود"),
            "fieldname": "employee",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("تاريخ الغياب"),
            "fieldname": "attendance_date",
            "fieldtype": "Date",
            "width": 150
        },
		{
			"label": _("الحالة"),
			"fieldname": "status",
			"fieldtype": "Data",
			"width": 120
		},
        {
            "label": _("ملاحظات"),
            "fieldname": "notes",
            "fieldtype": "Data",
            "width": 300
        },
        {
            "label": _("نوع الوظيفة"),
            "fieldname": "employment_type",
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
    if filters.get("employee"):
        conditions += "and employee = %(employee)s"
    if filters.get("from_date"):
        conditions += " and attendance_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and attendance_date <= %(to_date)s"
    if filters.get("status"):
        conditions += "and status = %(status)s"
    if filters.get("notes"):
        conditions += "and notes = %(notes)s"
    if filters.get("employment_type"):
        conditions += "and employment_type = %(employment_type)s"

    result = []
    item_results = frappe.db.sql("""
        select
            employee, employee_name, attendance_date, status, notes, employment_type
        from
            `tabAttendance`
        where
            `tabAttendance`.docstatus = 1 and `tabAttendance`.status = "absent"
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'employee': item_dict.employee,
            'employee_name': item_dict.employee_name,
            'attendance_date': item_dict.attendance_date,
            'status': item_dict.status,
            'notes': item_dict.notes,
            'employment_type': item_dict.employment_type,
        }
        result.append(data)
    return result