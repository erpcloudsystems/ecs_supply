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
			"width": 250
		},
        {
            "label": _("رقم الموظف"),
            "fieldname": "civilians",
            "fieldtype": "Link",
			"options": "Employee",
            "width": 150
        },
        {
            "label": _("الدرجة الوظيفية"),
            "fieldname": "civilians_degree",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("تاريخ التقرير"),
            "fieldname": "report_date",
            "fieldtype": "Date",
            "width": 150
        },
        {
            "label": _("السنة"),
            "fieldname": "year",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": _("التقدير"),
            "fieldname": "estimation",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("الدرجة"),
            "fieldname": "civilians_grade",
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
    if filters.get("civilians"):
        conditions += "and civilians = %(civilians)s"
    if filters.get("from_date"):
        conditions += " and report_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and report_date <= %(to_date)s"
    if filters.get("civilians_degree"):
        conditions += "and civilians_degree = %(civilians_degree)s"
    if filters.get("estimation"):
        conditions += "and estimation = %(estimation)s"
    if filters.get("year"):
        conditions += "and year = %(year)s"
    if filters.get("civilians_grade"):
        conditions += "and civilians_grade = %(civilians_grade)s"

    result = []
    item_results = frappe.db.sql("""
        select
            civilians, employee_name, civilians_degree, year, estimation, civilians_grade, report_date
        from
            `tabCivilians Secret Report`
        where
            `tabCivilians Secret Report`.docstatus = 1
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'civilians': item_dict.civilians,
            'employee_name': item_dict.employee_name,
            'civilians_degree': item_dict.civilians_degree,
            'year': item_dict.year,
            'estimation': item_dict.estimation,
            'civilians_grade': item_dict.civilians_grade,
            'report_date': item_dict.report_date,
        }
        result.append(data)
    return result