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
			"label": _("أسم الزائر"),
			"fieldname": "name1",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("العنوان"),
			"fieldname": "visitor_address",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("رقم البطاقة"),
			"fieldname": "no_old",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("جهة الزيارة الداخلية"),
			"fieldname": "visit_depart",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("الجهة التابع لها"),
			"fieldname": "entities",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("طبيعة الزيارة"),
			"fieldname": "visit_type",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("سبب الزيارة"),
			"fieldname": "visit_reason",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("تاريخ الزيارة"),
			"fieldname": "visit_date",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("وقت الزياره"),
			"fieldname": "time",
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
    if filters.get("genral_visit"):
        conditions += "where `tabDaily Visit`.genral_visit = %(genral_visit)s"
    if filters.get("from_date"):
        conditions += " and `tabDaily Visit`.visit_date  >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and `tabDaily Visit`.visit_date  <= %(to_date)s"

    result = []
    item_results = frappe.db.sql("""
		select 
			`tabDaily Visitors`.name1  ,
			`tabDaily Visitors`.entities  ,
			`tabDaily Visit`.no_old,
			`tabDaily Visit`.visit_type ,
			`tabDaily Visit`.visit_depart ,
			`tabDaily Visit`.visit_date ,
			`tabDaily Visit`.time ,
			`tabDaily Visit`.visit_reason, 
			`tabDaily Visit`.visitor_address,
			`tabDaily Visit`.genral_visit

			
		from
				`tabDaily Visit` 
		JOIN    
			`tabDaily Visitors` ON `tabDaily Visitors`.name = `tabDaily Visit`.visitors


		
            {conditions}
        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'name1': item_dict.name1,
            'entities': item_dict.entities,
            'no_old': item_dict.no_old,
            'visit_type': item_dict.visit_type,
            'visit_depart': item_dict.visit_depart,
            'visit_date': item_dict.visit_date,
            'time': item_dict.time,
            'visit_reason': item_dict.visit_reason,
            'visitor_address': item_dict.visitor_address,
            'cur_user':frappe.db.get_value("User", frappe.session.user, ["full_name"])
        }
        result.append(data)
    return result