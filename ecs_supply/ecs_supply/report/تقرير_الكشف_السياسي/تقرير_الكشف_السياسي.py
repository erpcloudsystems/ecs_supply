# Copyright (c) 2023, erpcloud.systems and contributors
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
    if filters.get("recruit") and filters.get("filter") is None:
        columns = [
            {
                "label": _("المستند"),
                "fieldname": "docname",
                "fieldtype": "Link",
                "options":"Criminal And Political Investigation",
                "width": 100
            },
            {
                "label": _("الاسم"),
                "fieldname": "first_name",
                "fieldtype": "Data",
                "width": 200
            },
            {
                "label": _("الرتبة"),
                "fieldname": "policemen_rank",
                "fieldtype": "Data",
                "width": 200
            },                    
            {
                "label": _("رقم الصادر الأمن الوطني" ),
                "fieldname": "send_investigation_number",
                "fieldtype": "Data",
                "width": 200
            },
            {
                "label": _(" تاريخ الصادر الأمن الوطني"),
                "fieldname": "criminal_investigation_date",
                "fieldtype": "Date",
                "width": 200
            },
            {
                "label": _(" رقم الوارد الأمن الوطني"),
                "fieldname": "investigation_entry_number",
                "fieldtype": "Data",
                "width": 200
            },
            {
                "label": _(" تاريخ الوارد الأمن الوطني"),
                "fieldname": "receipt_the_result_of_criminal_investigation_date",
                "fieldtype": "Date",
                "width": 200
            },
            {
                "label": _("النتيجة"),
                "fieldname": "the_result",
                "fieldtype": "Data",
                "width": 200
            }
        ]
        return columns
        
    elif filters.get("filter"):
        filter_option = filters.get("filter")
        if filter_option != "اخرى":
            return [
                {
                "label": _("المستند"),
                "fieldname": "docname",
                "fieldtype": "Link",
                "options":"Criminal And Political Investigation",
                "width": 100
                },
                {
                    "label": _("الاسم"),
                    "fieldname": "first_name",
                    "fieldtype": "Data",
                    "width": 200
                },
				{
                "label": _(" تاريخ الصادر الأمن الوطني"),
                "fieldname": "criminal_investigation_date",
                "fieldtype": "Date",
                "width": 200
				},
            ]
        elif filter_option == "لم يرد":
            return [
                {
                "label": _("المستند"),
                "fieldname": "docname",
                "fieldtype": "Link",
                "options":"Criminal And Political Investigation",
                "width": 100
                },
                {
                    "label": _("الاسم"),
                    "fieldname": "first_name",
                    "fieldtype": "Data",
                    "width": 200
                },
				{
                "label": _(" تاريخ الوارد الأمن الوطني"),
                "fieldname": "receipt_the_result_of_criminal_investigation_date",
                "fieldtype": "Date",
                "width": 200
				}
            ]
        else:
            return [
                {
                "label": _("المستند"),
                "fieldname": "docname",
                "fieldtype": "Link",
                "options":"Criminal And Political Investigation",
                "width": 100
                },
                {
                    "label": _("الاسم"),
                    "fieldname": "first_name",
                    "fieldtype": "Data",
                    "width": 200
                },
				{
                "label": _(" تاريخ الوارد الأمن الوطني"),
                "fieldname": "receipt_the_result_of_criminal_investigation_date",
                "fieldtype": "Date",
                "width": 200
				}
            ]
             
    return []
def get_data(filters, columns):
    emps = []
    emps = get_emps(filters)
    return emps


def get_emps(filters):
    conditions = ""
    values = {}

    if filters.get("recruit"):
        conditions += f" AND CPI.the_one_who_is_looking_for = '{filters['recruit']}'"
        values["recruit"] = filters["recruit"]

    if filters.get("filter"):
        if "لامانع" in filters.get("filter"):
            conditions += " AND TBL.the_result = 'لامانع'  "
        elif "جاري الفحص" in filters.get("filter"):
            conditions += " AND TBL.the_result = 'جاري الفحص'  "
        elif "الاستبعاد من الخدمات الهامة" in filters.get("filter"):
            conditions += " AND TBL.the_result = 'الاستبعاد من الخدمات الهامة'  "
        elif "اخرى" in filters.get("filter"):
            conditions += " AND TBL.the_result = 'اخرى'  "
        elif "لم يرد" in filters.get("filter"):
            conditions += " AND TBL.the_result = 'لم يرد' "
    result = []
    item_results = frappe.db.sql("""
        SELECT
            EMP.first_name,
            EMP.policemen_rank,                                      
            CPI.name as docname,
            CPI.the_one_who_is_looking_for,
            TBL.send_investigation_number,
            TBL.criminal_investigation_date,
            TBL.investigation_entry_number,
            TBL.receipt_the_result_of_criminal_investigation_date,
            TBL.the_result
        FROM
            `tabCriminal And Political Investigation` CPI
        JOIN
            `tabEnvestigation Employee` EMP
        ON EMP.name = CPI.the_one_who_is_looking_for
            
        JOIN 
            `tabNational Security For Employee` TBL 
        ON TBL.parent = CPI.name
        Where EMP.enabled =1 
        {conditions}
        """.format(conditions=conditions), as_dict=1)

    for item_dict in item_results:
        data = {
            'docname': item_dict.docname,
            'policemen_rank':item_dict.policemen_rank,
            'first_name': item_dict.first_name,
            'the_one_who_is_looking_for':item_dict.the_one_who_is_looking_for,
            'send_investigation_number': item_dict.send_investigation_number,
            'criminal_investigation_date': item_dict.criminal_investigation_date,
            'investigation_entry_number': item_dict.investigation_entry_number,
            'receipt_the_result_of_criminal_investigation_date': item_dict.receipt_the_result_of_criminal_investigation_date,
            "cur_user":frappe.session.user,
            'the_result':item_dict.the_result
        }
        result.append(data)
    return result
