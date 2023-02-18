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
            "width": 150
        },
        {
            "label": _("الدرجة"),
            "fieldname": "civilians_degree",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": _("تاريخ الانتقال"),
            "fieldname": "transfer_date",
            "fieldtype": "Date",
            "width": 120
        },
		{
			"label": _("جهة العمل الرئيسية"),
			"fieldname": "main_department",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("جهة العمل الرئيسية الجديدة"),
			"fieldname": "new_main_department",
			"fieldtype": "Data",
			"width": 150
		},
        {
            "label": _("الادراة الحالية"),
            "fieldname": "current_department_new",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("الادراة الجديدة"),
            "fieldname": "new_department_new",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("القسم الحالي"),
            "fieldname": "current_department_sec",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("القسم الجديد"),
            "fieldname": "new_department_sec",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("الوكالة الحالية"),
            "fieldname": "current_department",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("الوكالة الجديدة"),
            "fieldname": "new_department",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("الوحدة الحالية"),
            "fieldname": "current_designation_filed",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("الوحدة الجديدة"),
            "fieldname": "new_designation_filed",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("سبب الانتقال"),
            "fieldname": "transfer_reason",
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
    if filters.get("civilians"):
        conditions += "and civilians = %(civilians)s"
    if filters.get("from_date"):
        conditions += " and transfer_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and transfer_date <= %(to_date)s"
    if filters.get("civilians_degree"):
        conditions += "and civilians_degree = %(civilians_degree)s"
    if filters.get("main_department"):
        conditions += "and main_department = %(main_department)s"
    if filters.get("new_main_department"):
        conditions += "and new_main_department = %(new_main_department)s"
    if filters.get("current_department_new"):
        conditions += "and current_department_new = %(current_department_new)s"
    if filters.get("new_department_new"):
        conditions += "and new_department_new = %(new_department_new)s"
    if filters.get("current_department_sec"):
        conditions += "and current_department_sec = %(current_department_sec)s"
    if filters.get("new_department_sec"):
        conditions += "and new_department_sec = %(new_department_sec)s"
    if filters.get("current_department"):
        conditions += "and current_department = %(current_department)s"
    if filters.get("new_department"):
        conditions += "and new_department = %(new_department)s"
    if filters.get("current_designation_filed"):
        conditions += "and current_designation_filed = %(current_designation_filed)s"
    if filters.get("new_designation_filed"):
        conditions += "and new_designation_filed = %(new_designation_filed)s"

    result = []
    item_results = frappe.db.sql("""
        select
            civilians, employee_name, civilians_degree, main_department, new_main_department, current_department_new, new_department_new,
            current_department_sec, new_department_sec, current_department, new_department, current_designation_filed, new_designation_filed, transfer_date, transfer_reason
        from
            `tabTransfers for Civilians`
        where
            `tabTransfers for Civilians`.docstatus = 1
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'civilians': item_dict.civilians,
            'employee_name': item_dict.employee_name,
            'civilians_degree': item_dict.civilians_degree,
            'main_department': item_dict.main_department,
            'new_main_department': item_dict.new_main_department,
            'current_department_new': item_dict.current_department_new,
            'new_department_new': item_dict.new_department_new,
            'current_department_sec': item_dict.current_department_sec,
            'new_department_sec': item_dict.new_department_sec,
            'current_department': item_dict.current_department,
            'new_department': item_dict.new_department,
            'current_designation_filed': item_dict.current_designation_filed,
            'new_designation_filed': item_dict.new_designation_filed,
            'transfer_date': item_dict.transfer_date,
            'transfer_reason': item_dict.transfer_reason,
        }
        result.append(data)
    return result