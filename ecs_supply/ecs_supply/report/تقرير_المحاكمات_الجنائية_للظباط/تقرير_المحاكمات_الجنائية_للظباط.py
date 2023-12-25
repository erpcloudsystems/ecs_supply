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
            "fieldname": "rakm1",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": _("الرتبة"),
            "fieldname": "ratba",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("رقم الأقدمية"),
            "fieldname": "rakm2",
            "fieldtype": "Link",
			"options": "Employee",
            "width": 100
        },
        {
            "label": _("اسم رباعي"),
            "fieldname": "asm",
            "fieldtype": "Data",
            "width": 250
        },
        {
            "label": _("العمل القائم به"),
            "fieldname": "sd",
            "fieldtype": "Link",
            "options": "Employee",
            "width": 110
        },
        {
            "label": _("التهمة"),
            "fieldname": "the_charge",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": _("قرار النيابة العامة"),
            "fieldname": "public_prosecution_decision",
            "fieldtype": "Data",
            "width": 250
        },
        {
            "label": _("قرار المحكمة"),
            "fieldname": "the_courts_decision",
            "fieldtype": "Data",
            "width": 130
        },
        {
            "label": _("تاريخ القرار"),
            "fieldname": "date_of_the_decision",
            "fieldtype": "Date",
            "width": 100
        },
        {
            "label": _("تاريخ القرار"),
            "fieldname": "date_of_the_decision2",
            "fieldtype": "Date",
            "width": 100
        },
        {
            "label": _("موقفه من العمل"),
            "fieldname": "his_attitude_to_work",
            "fieldtype": "Data",
            "width": 130
        }
    ]


def get_data(filters, columns):
    emp = []
    emp = get_emps(filters)
    return emp


def get_emps(filters):
    result =[]
    conditions =""
    if filters.get("policemen"):
        conditions += " AND CT.employee = %(policemen)s or CT.name = %(policemen)s  "

    item_results2 = frappe.db.sql(f"""
      SELECT
        CT.officers_affairs,
        CT.employee_name,
        SOMI.the_case_number,
        SOMI.the_charge,
        SOMI.public_prosecution_decision,
        SOMI.the_courts_decision,
        SOMI.date_of_the_decision,
        SOMI.date_of_the_decision2,
        SOMI.his_attitude_to_work,
        EE.custom_file_number4 AS rakm1,
        EE.policemen_rank AS ratba,
        EE.the_seniority_number AS rakm2,
        EE.first_name AS asm,
        EE.main_department23 AS md,
        EE.sup_department AS sd
                                  

      FROM
        `tabCriminal Trials Of Officers` CT
      JOIN
        `tabStatement Of The Case` SOMI
      ON 
        SOMI.parent = CT.name
     JOIN
        `tabOfficers Affairs` EE  
                                
        ON CT.officers_affairs = EE.name 
      {conditions}
    Where EE.enabled =1    
    """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results2:
        data = {
            'rakm1': item_dict.rakm1,
            'ratba': item_dict.ratba,
            'rakm2': item_dict.rakm2,
            'asm': item_dict.asm,
            'the_case_number': item_dict.the_case_number,
            'the_charge': item_dict.the_charge,
            'public_prosecution_decision': item_dict.public_prosecution_decision,
            'the_courts_decision': item_dict.the_courts_decision,
            'date_of_the_decision': item_dict.date_of_the_decision,
            'date_of_the_decision2': item_dict.date_of_the_decision2,
            'his_attitude_to_work': item_dict.his_attitude_to_work,
            "cur_user":frappe.session.user,
            'md':item_dict.md,
            'sd':item_dict.sd
        }
        result.append(data)
    return result
