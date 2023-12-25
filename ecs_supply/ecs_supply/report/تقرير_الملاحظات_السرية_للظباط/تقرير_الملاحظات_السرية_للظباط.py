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
			"label": _("اسم الظابط"),
			"fieldname": "first_name",
			"fieldtype": "Data",
			"width": 200
		},
        {
            "label": _("رقم الأقدمية"),
            "fieldname": "the_seniority_number",
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
			"label": _("قرار الوضع"),
			"fieldname": "position_decision",
			"fieldtype": "Data",
			"width": 150
		},
        {
            "label": _("تاريخ الوضع"),
            "fieldname": "position_date",
            "fieldtype": "Date",
            "width": 120
        },
		{
			"label": _("قرار الرفع"),
			"fieldname": "lifting_decision",
			"fieldtype": "Data",
			"width": 150
		},
        {
            "label": _("تاريخ الرفع"),
            "fieldname": "lifting_date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": _("السبب"),
            "fieldname": "reason",
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
        conditions += "AND policemen = %(policemen)s"


    result = []
    item_results = frappe.db.sql("""
        select
            OA.the_seniority_number,
            OA.first_name,
            OA.policemen_rank,
            TS.position_decision,
            TS.position_date,
            TS.lifting_decision,
            TS.lifting_date,
            TS.reason
        from
            `tabSecret Notes Officers` SN
        Join
            `tabThe Statement` TS
        ON TS.parent = SN.name
		
		JOIN
			`tabOfficers Affairs` OA 
        ON OA.name = SN.officers_affairs
           Where OA.enabled =1                       
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'the_seniority_number': item_dict.the_seniority_number,
            'first_name': item_dict.first_name,
            'policemen_rank': item_dict.policemen_rank,
            'position_decision': item_dict.position_decision,
            'position_date': item_dict.position_date,
            'lifting_decision': item_dict.lifting_decision,
            'lifting_date': item_dict.lifting_date,
            'reason': item_dict.reason,
            "cur_user":frappe.session.user
        }
        result.append(data)
    return result