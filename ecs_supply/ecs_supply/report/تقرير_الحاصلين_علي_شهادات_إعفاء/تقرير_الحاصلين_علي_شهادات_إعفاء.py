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
            "label": _("أسم الموظف"),
            "fieldname": "first_name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("العمل القائم به"),
            "fieldname": "sup_department",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("رقم الكود"),
            "fieldname": "code_number",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("تاريخ الاصدار"),
            "fieldname": "release_date",
            "fieldtype": "Data",
            "width": 200
        },
		{
            "label": _("رقم السلاح"),
            "fieldname": "gun_number",
            "fieldtype": "Data",
            "width": 200
        },
		{
            "label": _("نوع السلاح"),
            "fieldname": "gun_type",
            "fieldtype": "Data",
            "width": 200
        },
		{
            "label": _("ماركة السلاح"),
            "fieldname": "gun_model",
            "fieldtype": "Data",
            "width": 200
        },        
		{
            "label": _("الغرض منه"),
            "fieldname": "its_purpose",
            "fieldtype": "Data",
            "width": 200
        }, 
    ]

    return columns


def get_data(filters, columns):
    emp = []
    emp = get_emps(filters)
    return emp


def get_emps(filters):
    conditions = ""

    if filters.get("recruit"):
        conditions += " AND EE.employee_number = %(recruit)s"

    result = []
    item_results = frappe.db.sql(f"""
      SELECT
        EE.first_name,
        EE.custom_date_of_appointment,
        EE.date_of_joining AS date_of_joining,
        EE.employee_number AS employee_number,
        EE.custom_file_number4 AS custom_file_number4,
        EE.sup_department AS sup_department,
        EE.policemen_rank AS policemen_rank,
        EE.main_department23 AS main_department23,
		WS.code_number,
		WS.release_date,
		WS.gun_number,
		WS.gun_type,
		WS.gun_model,
		WS.its_purpose

      FROM
        `tabOfficers Affairs` EE
    	Join `tabWeapon Spreadsheet` WS
      ON WS.parent = EE.name
    WHERE EE.enabled = 1   
    {conditions}
    """.format( conditions=conditions), as_dict=1)

    for item_dict in item_results:
        data = {
            'date_of_joining': item_dict.date_of_joining,
            'custom_file_number4': item_dict.custom_file_number4,
            'employee_number': item_dict.employee_number,
            'first_name': item_dict.first_name,
            'policemen_rank': item_dict.policemen_rank,
            'sup_department': item_dict.sup_department,
            'main_department23': item_dict.main_department23,
            'code_number': item_dict.code_number,
            'release_date': item_dict.release_date,
            'gun_number': item_dict.gun_number,
            'gun_type': item_dict.gun_type,
            'gun_model': item_dict.gun_model,
            'its_purpose': item_dict.its_purpose,
            "cur_user":frappe.session.user,
			

        }
        result.append(data)

    return result