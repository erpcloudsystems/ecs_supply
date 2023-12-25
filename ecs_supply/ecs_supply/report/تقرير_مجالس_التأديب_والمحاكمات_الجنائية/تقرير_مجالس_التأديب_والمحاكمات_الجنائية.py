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
            "label": _("رقم الشرطة"),
            "fieldname": "employee_number",
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
    conditions = ""

    if filters.get("policemen"):
        conditions += "AND EE.employee_number = %(policemen)s or EE.first_name = %(policemen)s or EE.name = %(policemen)s  "

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
            EE.employee_number AS employee_number,
            EE.custom_file_number4 AS custom_file_number4,
            EE.sup_department AS sup_department,
            EE.first_name,
            EE.employee_number,
            EE.name,
            EE.policemen_rank,
            EE.main_department23
        FROM
            `tabPolicemen Punishment` pp
        JOIN
            `tabEnvestigation Employee` EE  
                                
        ON pp.policeman_name = EE.name 
        
        JOIN
            `tabData` D
        ON D.parent = pp.name
        WHERE EE.enabled = 1
        {conditions}

        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'policenumber': item_dict.policenumber,
            'custom_file_number4': item_dict.custom_file_number4,
            'employee_number': item_dict.employee_number,
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
    conditions =""
    if filters.get("policemen"):
        conditions += "WHERE EE.employee_number = %(policemen)s or EE.first_name = %(policemen)s or EE.name = %(policemen)s  "

    item_results2 = frappe.db.sql(f"""
      SELECT
		CT.employee,
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
        EE.employee_number AS rakm2,
        EE.first_name AS asm,
        EE.main_department23 AS md,
        EE.sup_department AS sd
                                  

      FROM
        `tabCriminal Trials` CT
      JOIN
        `tabStatement Of The Case` SOMI
      ON 
        SOMI.parent = CT.name
     JOIN
        `tabEnvestigation Employee` EE  
                                
        ON CT.employee_name = EE.first_name 
      {conditions}
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
