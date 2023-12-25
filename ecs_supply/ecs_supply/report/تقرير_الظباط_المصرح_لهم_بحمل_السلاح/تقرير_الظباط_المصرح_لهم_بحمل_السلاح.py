# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe import msgprint, _
from frappe.utils import flt


def execute(filters=None):
    columns, data = [], []
    columns = get_columns(filters)
    data = get_data(filters, columns)
    return columns, data


def get_columns(filters):
    columns = [
        {
            "label": _("رقم الملف"),
            "fieldname": "custom_file_number4",
            "fieldtype": "Data",
            "width": 70
        },
        {
            "label": _("الرتبة"),
            "fieldname": "policemen_rank",
            "fieldtype": "Data",
            "width": 140
        },
        {
            "label": _("رقم الشرطة"),
            "fieldname": "employee_number",
            "fieldtype": "Data",
            "width": 70
        },
        {
            "label": _("اسم رباعي"),
            "fieldname": "first_name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("تاريخ الإلتحاق بالإدارة"),
            "fieldname": "date_of_joining",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("العمل القائم به"),
            "fieldname": "sup_department",
            "fieldtype": "Data",
            "width": 200
        },
    ]

    if filters.get("gun_reason") == 'غير مصرح عضوي' or filters.get("gun_reason") == 'غير مصرح نفسي' :

        columns.append({
            "label": _("السبب"),
            "fieldname": "reason",
            "fieldtype": "Long Text",
            "width": 150,
    
        })

    return columns


def get_data(filters, columns):
    emp = []
    emp = get_emps(filters)
    return emp


def get_emps(filters):
    conditions = ""
    filter_values = {}

    if filters.get("recruit"):
        conditions += " AND EE.employee_number = %(recruit)s"
        filter_values["recruit"] = filters["recruit"]

    if filters.get("gun_reason"):
        conditions += " AND EE.gun_carrying_case = %(gun_reason)s"
        filter_values["gun_reason"] = filters["gun_reason"]

    where_clause = conditions


    result = []
    item_results = frappe.db.sql(f"""
      SELECT
        EE.first_name,
		EE.gun_carrying_case,
        EE.date_of_joining AS date_of_joining,
        EE.the_seniority_number AS the_seniority_number,
        EE.custom_file_number4 AS custom_file_number4,
        EE.sup_department AS sup_department,
        EE.policemen_rank AS policemen_rank,
        EE.main_department23 AS main_department23,

        CASE
            WHEN  EE.gun_carrying_case = 'غير مصرح عضوي'       THEN EE.reason 
            WHEN  EE.gun_carrying_case = 'غير مصرح نفسي'       THEN EE.reason 
            WHEN  EE.gun_carrying_case = 'غير مصرح إحترازي'    THEN EE.reason 
            ELSE NULL
        END AS reason
      FROM
        `tabOfficers Affairs` EE
        WHERE EE.enabled = 1
      {where_clause}
    """, filter_values, as_dict=1)

    for item_dict in item_results:
        data = {
            'date_of_joining': item_dict.date_of_joining,
            'custom_file_number4': item_dict.custom_file_number4,
            'the_seniority_number': item_dict.the_seniority_number,
            'first_name': item_dict.first_name,
            'policemen_rank': item_dict.policemen_rank,
            'sup_department': item_dict.sup_department,
            'main_department23': item_dict.main_department23,
            'reason': item_dict.reason,
            "cur_user":frappe.session.user

        }
        result.append(data)

    return result