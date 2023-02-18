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
            "label": _("تاريخ الترقية"),
            "fieldname": "promotion_date",
            "fieldtype": "Date",
            "width": 130
        },
		{
			"label": _("الدرجة"),
			"fieldname": "current_civilians_degree",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("الدرجة الجديدة"),
			"fieldname": "new_civilians_degree",
			"fieldtype": "Data",
			"width": 150
		},
        {
            "label": _("فئة الدرجة"),
            "fieldname": "current_sub_degree",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("فئة الدرجة الجديدة"),
            "fieldname": "new_sub_degree",
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
    if filters.get("civilians"):
        conditions += "and civilians = %(civilians)s"
    if filters.get("from_date"):
        conditions += " and promotion_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and promotion_date <= %(to_date)s"
    if filters.get("current_civilians_degree"):
        conditions += "and current_civilians_degree = %(current_civilians_degree)s"
    if filters.get("new_civilians_degree"):
        conditions += "and new_civilians_degree = %(new_civilians_degree)s"
    if filters.get("current_sub_degree"):
        conditions += "and current_sub_degree = %(current_sub_degree)s"
    if filters.get("new_sub_degree"):
        conditions += "and new_sub_degree = %(new_sub_degree)s"
    if filters.get("notes"):
        conditions += "and notes = %(notes)s"

    result = []
    item_results = frappe.db.sql("""
        select
            civilians, employee_name, current_civilians_degree, new_civilians_degree, current_sub_degree, new_sub_degree, promotion_date, notes
        from
            `tabCivilians Promotion`
        where
            `tabCivilians Promotion`.docstatus = 1
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'civilians': item_dict.civilians,
            'employee_name': item_dict.employee_name,
            'current_civilians_degree': item_dict.current_civilians_degree,
            'new_civilians_degree': item_dict.new_civilians_degree,
            'current_sub_degree': item_dict.current_sub_degree,
            'new_sub_degree': item_dict.new_sub_degree,
            'promotion_date': item_dict.promotion_date,
            'notes': item_dict.notes,
        }
        result.append(data)
    return result