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
            "label": _("أسم الشركة"),
            "fieldname": "company_name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("الأسم"),
            "fieldname": "vis_name",
            "fieldtype": "Data",
            "width": 250
        },
        {
            "label": _("تاريخ الميلاد"),
            "fieldname": "vis_birthday",
            "fieldtype": "Link",
            "options": "Employee",
            "width": 110
        },
        {
            "label": _("محل الأقامة"),
            "fieldname": "vis_address",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": _("تاريخ العمل بالإدارة"),
            "fieldname":"working_date",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": _("طبيعة العمل"),
            "fieldname": "working_type",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": _("الكشف الجنائي"),
            "fieldname": "vis_crime",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": _("الكشف السياسي"),
            "fieldname": "vis_poli",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": _("ملاحظات"),
            "fieldname": "vis_notes",
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
    result = []
    if filters.get("name"):
        conditions += """ AND HCD.vis_name like '%{0}%' """.format(filters.get("name"))

    if filters.get("company_name"):
        conditions += """ AND HC.company_name like '%{0}%' """.format(filters.get("company_name"))

    item_results = frappe.db.sql(f"""
        SELECT
            HC.company_name,
            HCD.vis_name,
            HCD.vis_birthday,
            HCD.vis_address,
            HCD.working_date,
            HCD.working_type,
            HCD.vis_crime,
            HCD.vis_poli,
            HCD.vis_notes
                                 
        FROM
            `tabHesitant companies` HC
        JOIN
            `tabHesitant companies data` HCD          
        ON HCD.parent = HC.name
        WHERE HC.enabled = 1
        {conditions}

        ORDER BY  HC.company_name
     """.format(conditions=conditions), as_dict=1)
    for item_dict in item_results:
        data = {
            'company_name': item_dict.company_name,
            'vis_name': item_dict.vis_name,
            'vis_birthday': item_dict.vis_birthday,
            'vis_address': item_dict.vis_address,
            'working_date': item_dict.working_date,
            'working_type': item_dict.working_type,
            'vis_crime': item_dict.vis_crime,
            'vis_poli': item_dict.vis_poli,
            'vis_notes':item_dict.vis_notes,
            'cur_user':frappe.db.get_value("User", frappe.session.user, ["full_name"])
        }
        result.append(data)

    return result
