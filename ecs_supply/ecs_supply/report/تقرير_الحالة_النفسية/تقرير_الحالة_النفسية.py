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
            "fieldname": "employee_number",
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
    ]

    if filters.get("health_details3") == 'غير طبيعية':
        columns.append({
            "label": _("تفاصيل الحالة"),
            "fieldname": "health_details",
            "fieldtype": "Long Text ", #make this field bigger as text box
            "width": 1000,
    
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
    
    if filters.get("health_details3"):
        conditions += " AND EE.health_details3 = %(health_details3)s"
        filter_values["health_details3"] = filters["health_details3"]

    where_clause = conditions
  
    result = []
    item_results = frappe.db.sql(f"""
      SELECT
        EE.first_name,
        EE.date_of_joining AS date_of_joining,
        EE.employee_number AS employee_number,
        EE.custom_file_number4 AS custom_file_number4,
        EE.sup_department AS sup_department,
        EE.main_department23 AS main_department23,
        EE.policemen_rank AS policemen_rank,
        CASE
            WHEN EE.health_details3 = 'غير طبيعية' THEN EE.health_details2
            ELSE NULL -- or provide a default value if necessary
        END AS health_details
      FROM
        `tabEnvestigation Employee` EE
    Where EE.enabled =1
      {where_clause}
    """, filter_values, as_dict=1)

    for item_dict in item_results:
        data = {
            'date_of_joining': item_dict.date_of_joining,
            'custom_file_number4': item_dict.custom_file_number4,
            'employee_number': item_dict.employee_number,
            'first_name': item_dict.first_name,
            'policemen_rank': item_dict.policemen_rank,
            'sup_department': item_dict.sup_department,
            'main_department23': item_dict.main_department23,
            'health_details': item_dict.health_details,
            "cur_user":frappe.session.user

        }
        result.append(data)

    return result
