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
            "width": 120
        },
        {
            "label": _("الرتبة"),
            "fieldname": "policemen_rank",
            "fieldtype": "Data",
            "width": 150
        },
		{
			"label": _("السنة"),
			"fieldname": "year",
			"fieldtype": "Data",
			"width": 100
		},
        {
            "label": _("الغيابات خلال العام"),
            "fieldname": "absent_days_during_year",
            "fieldtype": "Data",
            "width": 130
        },
		{
			"label": _("المخالفات خلال العام"),
			"fieldname": "violation_during_year",
			"fieldtype": "Data",
			"width": 130
		},
        {
            "label": _("التاخيرات خلال العام"),
            "fieldname": "delays_during_year",
            "fieldtype": "Data",
            "width": 130
        },
		{
			"label": _("الجزاءات خلال العام"),
			"fieldname": "penalty_during_year",
			"fieldtype": "Data",
			"width": 130
		},
        {
            "label": _("حالة محو الجزاءات"),
            "fieldname": "erase_penalty",
            "fieldtype": "Data",
            "width": 120
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
    if filters.get("year"):
        conditions += "and year = %(year)s"
    if filters.get("absent_days_during_year"):
        conditions += "and absent_days_during_year = %(absent_days_during_year)s"
    if filters.get("violation_during_year"):
        conditions += "and violation_during_year = %(violation_during_year)s"
    if filters.get("delays_during_year"):
        conditions += "and delays_during_year = %(delays_during_year)s"
    if filters.get("penalty_during_year"):
        conditions += "and penalty_during_year = %(penalty_during_year)s"
    if filters.get("erase_penalty"):
        conditions += "and erase_penalty = %(erase_penalty)s"

    result = []
    item_results = frappe.db.sql("""
        select
            policemen, employee_name, policemen_rank, year, absent_days_during_year, violation_during_year, delays_during_year, penalty_during_year, erase_penalty
        from
            `tabPenalty During Year`
        where
            `tabPenalty During Year`.docstatus = 1
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'policemen': item_dict.policemen,
            'employee_name': item_dict.employee_name,
            'policemen_rank': item_dict.policemen_rank,
            'year': item_dict.year,
            'absent_days_during_year': item_dict.absent_days_during_year,
            'violation_during_year': item_dict.violation_during_year,
            'delays_during_year': item_dict.delays_during_year,
            'penalty_during_year': item_dict.penalty_during_year,
            'erase_penalty': item_dict.erase_penalty,
        }
        result.append(data)
    return result