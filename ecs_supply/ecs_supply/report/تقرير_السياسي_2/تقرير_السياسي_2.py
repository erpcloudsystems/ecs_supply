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
                "fieldname": "send_investigation_number2",
                "fieldtype": "Data",
                "width": 200
            },
            {
                "label": _(" تاريخ الصادر الأمن الوطني"),
                "fieldname": "political_investigation_date",
                "fieldtype": "Date",
                "width": 200
            },
            {
                "label": _(" رقم الوارد الأمن الوطني"),
                "fieldname": "investigation_entry_number2",
                "fieldtype": "Data",
                "width": 200
            },
            {
                "label": _(" تاريخ الوارد الأمن الوطني"),
                "fieldname": "receipt_the_result_of_political_investigation_date",
                "fieldtype": "Date",
                "width": 200
            },
            {
                "label": _("النتيجة"),
                "fieldname": "political_investigation_result",
                "fieldtype": "Data",
                "width": 200
            },
           
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
                "label": _(" تاريخ الوارد الأمن الوطني"),
                "fieldname": "receipt_the_result_of_political_investigation_date",
                "fieldtype": "Date",
                "width": 200
				},
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
                "fieldname": "receipt_the_result_of_political_investigation_date",
                "fieldtype": "Date",
                "width": 200
				},
                {
                "label": _("ملاحظات"),
                "fieldname": "result_notes",
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
        conditions += f" AND CPI.recruit = '{filters['recruit']}'"
        values["recruit"] = filters["recruit"]

    if filters.get("filter"):
        if conditions:
            conditions += " AND"
        else:
            conditions += " WHERE"

        if "لامانع" in filters.get("filter"):
            conditions += " AND CPI.political_investigation_result like '%لامانع%'  "
        elif "جاري الفحص" in filters.get("filter"):
            conditions += " AND CPI.political_investigation_result like '%جاري الفحص%'  "
        elif "الاستبعاد من الخدمات الهامة" in filters.get("filter"):
            conditions += " AND CPI.political_investigation_result like '%الاستبعاد من الخدمات الهامة%'  "
        elif "اخرى" in filters.get("filter"):
            conditions += " AND CPI.political_investigation_result like '%اخرى%'  "

    result = []
    item_results = frappe.db.sql("""
        SELECT
            EMP.first_name,
            EMP.policemen_rank,                                      
            CPI.name as docname,
            CPI.recruit,
            CPI.send_investigation_number2,
            CPI.political_investigation_date,
            CPI.investigation_entry_number2,
            CPI.receipt_the_result_of_political_investigation_date,
            CPI.political_investigation_result,
            CPI.result_notes,
            CPI.send_investigation_number,
            CPI.criminal_investigation_date,
            CPI.investigation_entry_number,
            CPI.receipt_the_result_of_criminal_investigation_date,
            CPI.custom_criminal_investigation_result3,
            CPI.criminal_investigation_result,
            CPI.result_of_the_investions,
            CPI.result_of_the_investions_of_his_relatives
        FROM
            `tabCriminal And Political Disclosure` CPI
        JOIN
            `tabThe Recruits ` EMP
        ON EMP.name = CPI.recruit
        WHERE EMP.enabled = 1
        {conditions}
        """.format(conditions=conditions), as_dict=1)

    for item_dict in item_results:
        data = {
            'docname': item_dict.docname,
            'policemen_rank':item_dict.policemen_rank,
            'first_name': item_dict.first_name,
            'send_investigation_number2': item_dict.send_investigation_number2,
            'political_investigation_date': item_dict.political_investigation_date,
            'investigation_entry_number2': item_dict.investigation_entry_number2,
            'receipt_the_result_of_political_investigation_date': item_dict.receipt_the_result_of_political_investigation_date,
            'political_investigation_result': item_dict.political_investigation_result,
            'result_notes': item_dict.result_notes,
            'send_investigation_number': item_dict.send_investigation_number,
            'criminal_investigation_date': item_dict.criminal_investigation_date,
            'investigation_entry_number': item_dict.investigation_entry_number,
            'receipt_the_result_of_criminal_investigation_date': item_dict.receipt_the_result_of_criminal_investigation_date,
            'custom_criminal_investigation_result3': item_dict.custom_criminal_investigation_result3,
            'criminal_investigation_result': item_dict.criminal_investigation_result,
            'result_of_the_investions': item_dict.result_of_the_investions,
            'result_of_the_investions_of_his_relatives': item_dict.result_of_the_investions_of_his_relatives,
            "cur_user":frappe.session.user
        }
        result.append(data)
    return result
