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
			"label": _("الرتبة"),
			"fieldname": "rank",
			"fieldtype": "Data",
			"width": 100
		},
        {
            "label": _("رقم الأقدمية"),
            "fieldname": "officers",
            "fieldtype": "Link",
			"options": "Employee",
            "width": 130
        },
        {
            "label": _("اسم الفرقة"),
            "fieldname": "course_type",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("تاريخ بدء الفرقة"),
            "fieldname": "start_date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": _("تاريخ نهاية الفرقة"),
            "fieldname": "end_date",
            "fieldtype": "Date",
            "width": 120
        },
	
        {
            "label": _("الموقع"),
            "fieldname": "location",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("نتيجة الفرقة"),
            "fieldname": "training_result",
            "fieldtype": "Data",
            "width": 100
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
    if filters.get("course_type"):
        conditions += "and course_type = %(course_type)s"
    if filters.get("from_date"):
        conditions += " and start_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and start_date <= %(to_date)s"
    if filters.get("rank"):
        conditions += "and rank = %(rank)s"
    if filters.get("location"):
        conditions += "and location = %(location)s"
    if filters.get("training_result"):
        conditions += "and training_result = %(training_result)s"

    result = []
    item_results = frappe.db.sql("""
        select
            officers, employee_name, rank, course_type, start_date, location, training_result
        from
            `tabOfficers Training Event`
        where
            `tabOfficers Training Event`.docstatus = 1
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'officers': item_dict.officers,
            'employee_name': item_dict.employee_name,
            'rank': item_dict.rank,
            'course_type': item_dict.course_type,
            'start_date': item_dict.start_date,
            'location': item_dict.location,
            'training_result': item_dict.training_result,
        }
        result.append(data)
    return result