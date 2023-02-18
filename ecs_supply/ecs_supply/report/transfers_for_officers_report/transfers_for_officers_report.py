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
			"width": 170
		},
        {
            "label": _("رقم الضابط"),
            "fieldname": "officers",
            "fieldtype": "Link",
            "options": "Employee",
            "width": 120
        },
        {
            "label": _("الرتبة"),
            "fieldname": "rank",
            "fieldtype": "Data",
            "width": 100
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
            "label": _("جهة العمل الداخلية"),
            "fieldname": "sub_department",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("جهة العمل الداخلية الجديدة"),
            "fieldname": "new_sub_department",
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
    if filters.get("officers"):
        conditions += "and officers = %(officers)s"
    if filters.get("from_date"):
        conditions += " and transfer_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and transfer_date <= %(to_date)s"
    if filters.get("rank"):
        conditions += "and rank = %(rank)s"
    if filters.get("main_department"):
        conditions += "and main_department = %(main_department)s"
    if filters.get("new_main_department"):
        conditions += "and new_main_department = %(new_main_department)s"
    if filters.get("sub_department"):
        conditions += "and sub_department = %(sub_department)s"
    if filters.get("new_sub_department"):
        conditions += "and new_sub_department = %(new_sub_department)s"
    if filters.get("transfer_reason"):
        conditions += "and transfer_reason = %(transfer_reason)s"

    result = []
    item_results = frappe.db.sql("""
        select
            officers, employee_name, rank, main_department, new_main_department, sub_department, new_sub_department, transfer_date, transfer_reason
        from
            `tabTransfers for Officers`
        where
            `tabTransfers for Officers`.docstatus = 1
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'officers': item_dict.officers,
            'employee_name': item_dict.employee_name,
            'rank': item_dict.rank,
            'main_department': item_dict.main_department,
            'new_main_department': item_dict.new_main_department,
            'sub_department': item_dict.sub_department,
            'new_sub_department': item_dict.new_sub_department,
            'transfer_date': item_dict.transfer_date,
            'transfer_reason': item_dict.transfer_reason,
        }
        result.append(data)
    return result