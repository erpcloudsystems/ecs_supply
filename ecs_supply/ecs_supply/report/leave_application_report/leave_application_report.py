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
            "fieldname": "employee",
            "fieldtype": "Data",
            "options": "Employee",
            "width": 200
        },
        {
            "label": _("تاريخ انشاء الاجازة"),
            "fieldname": "posting_date",
            "fieldtype": "Date",
            "width": 130
        },
		{
			"label": _("تاريخ بداية الاجازة"),
			"fieldname": "from_date",
			"fieldtype": "Date",
			"width": 130
		},
		{
			"label": _("تاريخ نهاية الاجازة"),
			"fieldname": "to_date",
			"fieldtype": "Date",
			"width": 130
		},
        {
            "label": _("عدد ايام الاجازة"),
            "fieldname": "total_leave_days",
            "fieldtype": "Data",
            "width": 100
        },
		{
			"label": _("نوع الاجازة"),
			"fieldname": "leave_type",
			"fieldtype": "Link",
            "options": "Leave Type",
            "width": 150
		},
        {
            "label": _("الملاحظات"),
            "fieldname": "description",
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
    if filters.get("employee"):
        conditions += "and employee = %(employee)s"
    if filters.get("leave_type"):
        conditions += "and leave_type = %(leave_type)s"
    if filters.get("from_date"):
        conditions += " and from_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and from_date <= %(to_date)s"
    if filters.get("description"):
        conditions += "and description = %(description)s"

    result = []
    item_results = frappe.db.sql("""
        select
            employee, employee_name, leave_type, posting_date, from_date, to_date, total_leave_days, description
        from
            `tabLeave Application`
        where
            `tabLeave Application`.docstatus = 1
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'employee': item_dict.employee,
            'employee_name': item_dict.employee_name,
            'leave_type': item_dict.leave_type,
            'posting_date': item_dict.posting_date,
            'from_date': item_dict.from_date,
            'to_date': item_dict.to_date,
            'total_leave_days': item_dict.total_leave_days,
            'description': item_dict.description,
        }
        result.append(data)
    return result