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
            "label": _("الأسم"),
            "fieldname": "vis_name",
            "fieldtype": "Data",
            "width": 250
        },
        {
            "label": _("طبيعة العمل"),
            "fieldname": "working_type",
            "fieldtype": "Data",
            "width": 120
        },
		{
            "label": _("أسم الشركة"),
            "fieldname": "company_name",
            "fieldtype": "Data",
            "width": 100
        },
      
    ]


def get_data(filters, columns):
    emp = []
    emp = get_emps(filters)
    return emp


def get_emps(filters):
    conditions = ""
    result = []
    item_results = frappe.db.sql(f"""
        SELECT
            HC.company_name,
            HCD.vis_name,
            HCD.working_type

                        
        FROM
            `tabHesitant companies` HC
        JOIN
            `tabHesitant companies data` HCD          
        ON HCD.parent = HC.name
        WHERE HC.enabled = 1
        ORDER BY  HC.company_name
        {conditions}
     """.format(conditions=conditions), filters, as_dict=1)
    for item_dict in item_results:
        data = {
            'company_name': item_dict.company_name,
            'vis_name': item_dict.vis_name,
            'working_type': item_dict.working_type,
            'cur_user':frappe.session.user
        }
        result.append(data)

    return result
