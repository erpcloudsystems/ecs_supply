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
            "width": 90
        },
        {
            "label": _("الرتبة"),
            "fieldname": "policemen_rank",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": _("رقم الشرطة"),
            "fieldname": "the_seniority_number",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": _("اسم رباعي"),
            "fieldname": "first_name",
            "fieldtype": "Data",
            "width": 250
        },
        {
            "label": _("تاريخ الإلتحاق بالإدارة"),
            "fieldname": "date_of_joining",
            "fieldtype": "Data",
            "width": 130
        },
        {
            "label": _("العمل القائم به"),
            "fieldname": "sup_department",
            "fieldtype": "Data",
            "width": 450
        },
        {
			"label": _("رقم القضية"),
			"fieldname": "the_case_number",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("رقم الحصر"),
			"fieldname": "limited_number",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("كلي مستأنف"),
			"fieldname": "im_all_resumed",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("التهمة"),
			"fieldname": "the_charge",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("الحكم"),
			"fieldname": "the_ruling",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("تاريخ الجلسة"),
			"fieldname": "date_of_the_session",
			"fieldtype": "Date",
			"width": 200
		},
		{
			"label": _("العقوبة"),
			"fieldname": "the_punishment",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("التصرفات"),
			"fieldname": "acts",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("رقم القضية"),
			"fieldname": "the_case_number_1",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("التهمة"),
			"fieldname": "the_charge_1",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("التصرفات"),
			"fieldname": "acts_1",
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
    filter_values = {}

    if filters.get("recruit"):
        conditions += " AND EE.name = %(recruit)s"
        filter_values["recruit"] = filters["recruit"]
    

    where_clause = conditions
   
    result = []
    item_results = frappe.db.sql(f"""
      SELECT
        EE.first_name,
        EE.date_of_joining AS date_of_joining,
        EE.the_seniority_number AS the_seniority_number,
        EE.custom_file_number4 AS custom_file_number4,
        EE.sup_department AS sup_department,
        EE.main_department23 AS main_department23,
        EE.policemen_rank AS policemen_rank,
        CDO.the_one_who_is_looking_for,
        SOJ.the_case_number,
        SOJ.limited_number,
        SOJ.im_all_resumed,
        SOJ.the_charge,
        SOJ.the_ruling,
        SOJ.date_of_the_session,
        SOJ.the_punishment,
        SOJ.acts,
        OI.the_case_number AS the_case_number_1,
        OI.the_charge AS the_charge_1,
        OI.acts AS acts_1
      FROM
        `tabCriminal Detection Of Officers` CDO
	  JOIN
        `tabOfficers Affairs` EE
      ON CDO.the_one_who_is_looking_for = EE.name
	  
	  JOIN
        `tabSchedule Of Officers Of Judgments` SOJ
      ON SOJ.parent = CDO.name
	
	  JOIN
        `tabOfficers Information` OI
      ON OI.parent = CDO.name
	  Where EE.enabled =1
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
            'the_case_number': item_dict.the_case_number,
            'limited_number': item_dict.limited_number,
            'im_all_resumed': item_dict.im_all_resumed,
            'the_charge': item_dict.the_charge,
            'the_ruling': item_dict.the_ruling,
            'date_of_the_session': item_dict.date_of_the_session,
            'the_punishment': item_dict.the_punishment,
            'acts': item_dict.acts,
            'the_case_number_1': item_dict.the_case_number_1,
            'the_charge_1': item_dict.the_charge_1,
            'acts_1': item_dict.acts_1,
            "cur_user":frappe.session.user
        }
        result.append(data)

    return result
