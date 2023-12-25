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
			"label": _("رقم الملف"),
			"fieldname": "custom_file_number4",
			"fieldtype": "Data",
			"width": 100
		},
        {
            "label": _("الرتبة"),
            "fieldname": "policemen_rank",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("رقم الأقدمية"),
            "fieldname": "the_seniority_number",
            "fieldtype": "Link",
			"options": "Employee",
            "width": 100
        },
        {
			"label": _("اسم رباعي"),
			"fieldname": "first_name",
			"fieldtype": "Data",
			"width": 250
		},
        {
            "label": _("العمل القائم به"),
            "fieldname": "sup_department",
            "fieldtype": "Link",
			"options": "Employee",
            "width": 110
        },
		{
			"label": _("بيان المخالفة"),
			"fieldname": "punishment_type",
			"fieldtype": "Data",
			"width": 100
		},
        {
            "label": _("تاريخ المخالفة"),
            "fieldname": "punishment_date",
            "fieldtype": "Date",
            "width": 120
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
            "width": 550
        }
    ]


def get_data(filters, columns):
    emp = []
    emp = get_emps(filters)
    return emp


def get_emps(filters):
    conditions = ""

    if filters.get("policemen"):
        conditions += "AND EE.the_seniority_number = %(policemen)s or EE.first_name = %(policemen)s or EE.name = %(policemen)s  "

    result = []
    item_results = frappe.db.sql(f"""
        SELECT
            pp.policeman_name,
            D.punishment_type,
            D.referral_decision_number,
            D.referral_date,
            D.punishment_date,
            D.call_number, 
            D.disciplinary_board_decision, 
            EE.the_seniority_number AS the_seniority_number,
            EE.custom_file_number4 AS custom_file_number4,
            EE.sup_department AS sup_department,
            EE.first_name,
            EE.the_seniority_number,
            EE.name,
            EE.policemen_rank,
            EE.main_department23
        FROM
            `tabDisciplinary Councils For Officers` pp
        JOIN
            `tabOfficers Affairs` EE  
                                
        ON pp.officers_affairs = EE.name 
        
        JOIN
            `tabData` D
        ON D.parent = pp.name
        Where EE.enabled =1 
        {conditions}

        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'policenumber': item_dict.policenumber,
            'custom_file_number4': item_dict.custom_file_number4,
            'the_seniority_number': item_dict.the_seniority_number,
            'employee_name': item_dict.employee_name,
            'policemen_rank': item_dict.policemen_rank,
            'punishment_type': item_dict.punishment_type,
            'referral_decision_number': item_dict.referral_decision_number,
            'referral_date': item_dict.referral_date,
            'call_number': item_dict.call_number,
            'disciplinary_board_decision': item_dict.disciplinary_board_decision,
            'sup_department': item_dict.sup_department,
            'punishment_date':item_dict.punishment_date,
            'first_name':item_dict.first_name,
            'main_department23':item_dict.main_department23
        }
        result.append(data)

    return result
