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
            "width": 150
        },
        {
            "label": _("الرتبة"),
            "fieldname": "policemen_rank",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("تاريخ الحصول علي الراتب"),
            "fieldname": "additional_salary_date",
            "fieldtype": "Date",
            "width": 170
        },
		{
			"label": _("نوع الراتب"),
			"fieldname": "additional_work_type",
			"fieldtype": "Data",
			"width": 200
		},
        {
            "label": _("قيمة الراتب الاضافي"),
            "fieldname": "additional_salary_value",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("الملاحظات"),
            "fieldname": "notes",
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
    if filters.get("policemen"):
        conditions += "and policemen = %(policemen)s"
    if filters.get("policemen_rank"):
        conditions += "and policemen_rank = %(policemen_rank)s"
    if filters.get("additional_work_type"):
        conditions += "and additional_work_type = %(additional_work_type)s"
    if filters.get("from_date"):
        conditions += " and additional_salary_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and additional_salary_date <= %(to_date)s"
    if filters.get("additional_salary_value"):
        conditions += "and additional_salary_value = %(additional_salary_value)s"
    if filters.get("notes"):
        conditions += "and notes = %(notes)s"

    result = []
    item_results = frappe.db.sql("""
        select
            policemen, employee_name, policemen_rank, additional_work_type, additional_salary_date, additional_salary_value, notes
        from
            `tabGetting Additional Salary`
        where
            `tabGetting Additional Salary`.docstatus = 1
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'policemen': item_dict.policemen,
            'employee_name': item_dict.employee_name,
            'policemen_rank': item_dict.policemen_rank,
            'additional_work_type': item_dict.additional_work_type,
            'additional_salary_date': item_dict.additional_salary_date,
            'additional_salary_value': item_dict.additional_salary_value,
            'notes': item_dict.notes,
        }
        result.append(data)
    return result