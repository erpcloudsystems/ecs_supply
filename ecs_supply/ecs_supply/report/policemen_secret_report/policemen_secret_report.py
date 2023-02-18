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
			"width": 250
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
            "width": 200
        },
        {
            "label": _("تاريخ التقرير"),
            "fieldname": "report_date",
            "fieldtype": "Date",
            "width": 150
        },
        {
            "label": _("التقدير"),
            "fieldname": "estimation",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("الدرجة"),
            "fieldname": "policemen_degree",
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
    if filters.get("from_date"):
        conditions += " and report_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and report_date <= %(to_date)s"
    if filters.get("policemen_rank"):
        conditions += "and policemen_rank = %(policemen_rank)s"
    if filters.get("estimation"):
        conditions += "and estimation = %(estimation)s"
    if filters.get("policemen_degree"):
        conditions += "and policemen_degree = %(policemen_degree)s"

    result = []
    item_results = frappe.db.sql("""
        select
            policemen, employee_name, policemen_rank, estimation, policemen_degree, report_date
        from
            `tabPolicemen Secret Report`
        where
            `tabPolicemen Secret Report`.docstatus = 1
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'policemen': item_dict.policemen,
            'employee_name': item_dict.employee_name,
            'policemen_rank': item_dict.policemen_rank,
            'estimation': item_dict.estimation,
            'policemen_degree': item_dict.policemen_degree,
            'report_date': item_dict.report_date,
        }
        result.append(data)
    return result