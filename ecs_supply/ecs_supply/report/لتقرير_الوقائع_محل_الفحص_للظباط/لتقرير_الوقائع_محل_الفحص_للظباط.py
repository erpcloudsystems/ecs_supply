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
			"label": _("الأسم"),
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
			"label": _("تاريخ الواقعة"),
			"fieldname": "date_of_incident",
			"fieldtype": "Data",
			"width": 100
		},
        {
            "label": _("موجز الواقعة"),
            "fieldname": "summary_of_the_incident",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": _("الفحص"),
            "fieldname": "examination",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": _("النتيجة"),
            "fieldname": "result",
            "fieldtype": "Data",
            "width": 120
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
            pp.officers_name,
            D.date_of_incident,
            D.summary_of_the_incident,
            D.examination,
            D.result,
            EE.the_seniority_number AS the_seniority_number,
            EE.custom_file_number4 AS custom_file_number4,
            EE.sup_department AS sup_department,
            EE.first_name,
            EE.the_seniority_number,
            EE.name,
            EE.policemen_rank,
            EE.main_department23
        FROM
            `tabExamination_for_officers` pp
        JOIN
            `tabOfficers Affairs` EE  
                                
        ON pp.officers_name = EE.name 
        
        JOIN
            `tabThe facts under examination for individuals data` D
        ON D.parent = pp.name
        Where EE.enabled =1 
        {conditions}

        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        data = {
            'policenumber': item_dict.policenumber,
            'custom_file_number4': item_dict.custom_file_number4,
            'the_seniority_number': item_dict.the_seniority_number,
            'policemen_rank': item_dict.policemen_rank,
            'date_of_incident': item_dict.date_of_incident,
            'summary_of_the_incident': item_dict.summary_of_the_incident,
            'examination': item_dict.examination,
            'result': item_dict.result,
            'sup_department': item_dict.sup_department,
            'first_name':item_dict.first_name,
            'main_department23':item_dict.main_department23
        }
        result.append(data)

    return result
