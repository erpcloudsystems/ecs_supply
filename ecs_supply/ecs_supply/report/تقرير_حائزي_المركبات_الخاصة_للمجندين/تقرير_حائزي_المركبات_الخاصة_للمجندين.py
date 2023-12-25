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
            "label": _("تاريخ التجنيد"),
            "fieldname": "date_of_conscription",
            "fieldtype": "Data",
            "width": 140
        },
        {
            "label": _("العمل القائم به"),
            "fieldname": "sup_department",
            "fieldtype": "Data",
            "width": 200
        },
		{
            "label": _("اسم المالك"),
            "fieldname": "owner_name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("رقم اللوحة"),
            "fieldname": "plate_no",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("لون المركبة"),
            "fieldname": "color_vehicle",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("الماركة"),
            "fieldname": "brand",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("نهاية الترخيص"),
            "fieldname": "end_date",
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
        EE.date_of_conscription,
        EE.date_of_joining AS date_of_joining,
        EE.employee_number AS employee_number,
        EE.custom_file_number4 AS custom_file_number4,
        EE.sup_department AS sup_department,
        EE.policemen_rank AS policemen_rank,
        EE.main_department23 AS main_department23,
		VD.owner_name,
		VD.plate_no,
		VD.color_vehicle,
		VD.brand,
		VD.end_date
      FROM
        `tabThe Recruits` EE
    	Join `tabVehicle Data` VD
    	ON VD.parent = EE.name
      Where EE.enabled =1 
        {conditions}
    """.format( conditions=conditions), as_dict=1)

    for item_dict in item_results:
        data = {
            'date_of_joining': item_dict.date_of_joining,
            'date_of_conscription': item_dict.date_of_conscription,
            'custom_file_number4': item_dict.custom_file_number4,
            'employee_number': item_dict.employee_number,
            'first_name': item_dict.first_name,
            'policemen_rank': item_dict.policemen_rank,
            'sup_department': item_dict.sup_department,
            'main_department23': item_dict.main_department23,
            'owner_name': item_dict.owner_name,
            'plate_no': item_dict.plate_no,
            'color_vehicle': item_dict.color_vehicle,
            'brand': item_dict.brand,
            'end_date': item_dict.end_date,
            'reason': item_dict.reason,
            "cur_user":frappe.session.user,
			

        }
        result.append(data)

    return result