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
            "label": _("الأسم"),
            "fieldname": "first_name",
            "fieldtype": "Data",
            "width": 200
        },
		{
            "label": _("جهة العمل"),
            "fieldname": "main_department23",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("تاريخ وجهة الانتداب"),
            "fieldname": "mandate_authority",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("تاريخ وجهة المأمورية"),
            "fieldname": "the_place_of_the_mission",
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



    result = []
    item_results = frappe.db.sql(f"""
      SELECT
        EE.first_name,
        EE.custom_file_number4 AS custom_file_number4,
        EE.policemen_rank AS policemen_rank,
		EE.main_department23,
        EE.mandate_authority,
        EE.the_place_of_the_mission
      FROM
        `tabHuman Resources` EE
		WHERE EE.enabled = 1 AND EE.main_department23 = "خارجية (مأموريات)" or EE.main_department23 = "خارجية (انتدابات)" 
	ORDER BY
    CASE
        WHEN EE.main_department23 = "خارجية (مأموريات)" THEN 1
        ELSE 0
    END;
	""".format( conditions=conditions), as_dict=1)

    for item_dict in item_results:
        data = {
            'date_of_joining': item_dict.date_of_joining,
            'custom_file_number4': item_dict.custom_file_number4,
            'first_name': item_dict.first_name,
            'policemen_rank': item_dict.policemen_rank,
            'mandate_authority': item_dict.mandate_authority,
            'the_place_of_the_mission': item_dict.the_place_of_the_mission,
            'main_department23': item_dict.main_department23,

            "cur_user":frappe.session.user,
			

        }
        result.append(data)

    return result