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
            "label": _("نوع الاصابة"),
            "fieldname": "injury_type",
            "fieldtype": "Data",
            "width": 150
        },
		{
			"label": _("من تاريخ"),
			"fieldname": "from_date",
			"fieldtype": "Date",
			"width": 120
		},
		{
			"label": _("الي تاريخ"),
			"fieldname": "to_date",
			"fieldtype": "Date",
			"width": 120
		},
        {
            "label": _("سبب الاصابة"),
            "fieldname": "injury_reason",
            "fieldtype": "Data",
            "width": 180
        },
        {
            "label": _("درجة العجز"),
            "fieldname": "disability_degree",
            "fieldtype": "Data",
            "width": 150
        },
		{
			"label": _("تاريخ ثبوته"),
			"fieldname": "disability_date",
			"fieldtype": "Date",
			"width": 120
		},
		{
			"label": _("رقم القرار"),
			"fieldname": "decision_number",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("تاريخ القرار"),
			"fieldname": "decision_date",
			"fieldtype": "Date",
			"width": 120
		},
		{
			"label": _("الوصف"),
			"fieldname": "description",
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
    if filters.get("officers"):
        conditions += "and officers = %(officers)s"
    if filters.get("from_date"):
        conditions += " and from_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and to_date <= %(to_date)s"
    if filters.get("rank"):
        conditions += "and rank = %(rank)s"
    if filters.get("injury_type"):
        conditions += "and injury_type = %(injury_type)s"
    if filters.get("injury_reason"):
        conditions += "and injury_reason = %(injury_reason)s"
    if filters.get("disability_degree"):
        conditions += "and disability_degree = %(disability_degree)s"
    if filters.get("disability_date"):
        conditions += "and disability_date = %(disability_date)s"
    if filters.get("decision_number"):
        conditions += "and decision_number = %(decision_number)s"
    if filters.get("decision_date"):
        conditions += "and decision_date = %(decision_date)s"
    if filters.get("description"):
        conditions += "and description = %(description)s"


    result = []
    item_results = frappe.db.sql("""
        select
            officers, employee_name, rank, injury_type, from_date, to_date, injury_reason, disability_degree, disability_date, decision_number, decision_date, description
        from
            `tabHealth Status`
        where
            `tabHealth Status`.docstatus = 1
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'officers': item_dict.officers,
            'employee_name': item_dict.employee_name,
            'rank': item_dict.rank,
            'injury_type': item_dict.injury_type,
            'from_date': item_dict.from_date,
            'to_date': item_dict.to_date,
            'injury_reason': item_dict.injury_reason,
            'disability_degree': item_dict.disability_degree,
            'disability_date': item_dict.disability_date,
            'decision_number': item_dict.decision_number,
            'decision_date': item_dict.decision_date,
            'description': item_dict.description,
        }
        result.append(data)
    return result