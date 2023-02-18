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
            "label": _("تاريخ العقوبة"),
            "fieldname": "punishment_date",
            "fieldtype": "Date",
            "width": 120
        },
		{
			"label": _("نوع العقوبة"),
			"fieldname": "punishment_type",
			"fieldtype": "Data",
			"width": 200
		},
        {
            "label": _("رقم قرار الاحالة"),
            "fieldname": "referral_decision_number",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": _("تاريخ الاحالة"),
            "fieldname": "referral_date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": _("رقم الدعوة"),
            "fieldname": "call_number",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": _("قرار مجلس التاديب النهائي"),
            "fieldname": "disciplinary_board_decision",
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
    if filters.get("punishment_type"):
        conditions += "and punishment_type = %(punishment_type)s"
    if filters.get("from_date"):
        conditions += " and punishment_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and punishment_date <= %(to_date)s"
    if filters.get("referral_decision_number"):
        conditions += "and referral_decision_number = %(referral_decision_number)s"
    if filters.get("referral_date"):
        conditions += "and referral_date = %(referral_date)s"
    if filters.get("call_number"):
        conditions += "and call_number = %(call_number)s"
    if filters.get("disciplinary_board_decision"):
        conditions += "and disciplinary_board_decision = %(disciplinary_board_decision)s"
    if filters.get("notes"):
        conditions += "and notes = %(notes)s"

    result = []
    item_results = frappe.db.sql("""
        select
            policemen, employee_name, policemen_rank, punishment_type, punishment_date, referral_decision_number, referral_date,
            call_number, disciplinary_board_decision, notes
        from
            `tabPolicemen Punishment`
        where
            `tabPolicemen Punishment`.docstatus = 1
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'policemen': item_dict.policemen,
            'employee_name': item_dict.employee_name,
            'policemen_rank': item_dict.policemen_rank,
            'punishment_type': item_dict.punishment_type,
            'punishment_date': item_dict.punishment_date,
            'referral_decision_number': item_dict.referral_decision_number,
            'referral_date': item_dict.referral_date,
            'call_number': item_dict.call_number,
            'disciplinary_board_decision': item_dict.disciplinary_board_decision,
            'notes': item_dict.notes,
        }
        result.append(data)
    return result