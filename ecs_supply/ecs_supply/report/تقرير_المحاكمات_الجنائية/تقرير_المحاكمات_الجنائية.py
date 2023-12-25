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
            "label": _("الفرد"),
            "fieldname": "employee_name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("رقم القضية"),
            "fieldname": "the_case_number",
            "fieldtype": "Data",
            "width": 100
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

    return columns


def get_data(filters, columns):
    emp = []
    emp = get_emps(filters)
    return emp


def get_emps(filters):
    conditions = ""
    filter_values = {}

    if filters.get("recruit"):
        conditions += "AND CT.employee = %(recruit)s"
        filter_values["recruit"] = filters["recruit"]

    where_clause = conditions
    if where_clause:
        where_clause = " Where EE.enabled =1 " + where_clause

    result = []
    item_results = frappe.db.sql(f"""
      SELECT
		CT.employee,
        CT.employee_name,
		SOMI.the_case_number,
		SOMI.the_charge,
		SOMI.public_prosecution_decision,
		SOMI.the_courts_decision,
		SOMI.date_of_the_decision,
		SOMI.date_of_the_decision2,
		SOMI.his_attitude_to_work

      FROM
        `tabCriminal Trials` CT
      JOIN
        `tabStatement Of The Case` SOMI
      ON 
        SOMI.parent = CT.name
      {where_clause}
    """, filter_values, as_dict=1)

    for item_dict in item_results:
        data = {
            'employee_name': item_dict.employee_name,
            'the_case_number': item_dict.the_case_number,
            'the_charge': item_dict.the_charge,
            'public_prosecution_decision': item_dict.public_prosecution_decision,
            'the_courts_decision': item_dict.the_courts_decision,
            'date_of_the_decision': item_dict.date_of_the_decision,
			'date_of_the_decision2': item_dict.date_of_the_decision2,
			'his_attitude_to_work': item_dict.his_attitude_to_work,
            "cur_user":frappe.session.user

        }
        result.append(data)

    return result
