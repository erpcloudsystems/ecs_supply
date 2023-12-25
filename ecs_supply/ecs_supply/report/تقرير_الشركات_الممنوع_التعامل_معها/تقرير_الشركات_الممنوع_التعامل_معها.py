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
            "label": _("السنة المالية"),
            "fieldname": "fiscal_year",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": _("أسم الشركة"),
            "fieldname": "the_company_name",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": _("مالك الشركة/رئيس مجلس الادارة"),
            "fieldname": "the_owner_of_the_company",
            "fieldtype": "Data",
            "width": 250
        },
        {
            "label": _("السمة التجارية"),
            "fieldname": "the_commercial_charactristic",
            "fieldtype": "Link",
            "options": "Employee",
            "width": 110
        },
        {
            "label": _("السجل التجاري"),
            "fieldname": "commercial_register",
            "fieldtype": "Data",
            "width": 100
        }
    ]


def get_data(filters, columns):
    emp = []
    emp = get_emps(filters)
    return emp


def get_emps(filters):
    conditions = ""
    result = []
    if filters.get("year"):
        conditions+= """ AND HC.fiscal_year = '{0}'""".format(filters.get("year"))

    if filters.get("the_company_name"):
        conditions += """ AND HCD.the_company_name like '%{0}%' """.format(filters.get("the_company_name"))

    if filters.get("the_owner_of_the_company"):
        conditions += """ AND HCD.the_owner_of_the_company like '%{0}%' """.format(filters.get("the_owner_of_the_company"))

    item_results = frappe.db.sql(f"""
        SELECT
            HC.fiscal_year,
            FY.year_end_date,
            HCD.commercial_register,
            HCD.the_owner_of_the_company,
            HCD.the_commercial_charactristic,
            HCD.the_company_name

                                 
        FROM
            `tabCompanies That Are Forbidden To Deal With` HC
        JOIN
            `tabTable Of Companies Prohibited To Deal With` HCD          
        ON HCD.parent = HC.name
        JOIN `tabFiscal Year` FY
        ON FY.name = HC.fiscal_year
        Where 1=1
        {conditions}

		ORDER BY FY.year_end_date DESC
     """.format(conditions=conditions), as_dict=1)
    for item_dict in item_results:
        data = {
            'fiscal_year': item_dict.fiscal_year,
            'the_company_name': item_dict.the_company_name,
            'the_owner_of_the_company': item_dict.the_owner_of_the_company,
            'the_company_activity': item_dict.the_company_activity,
            'commercial_register': item_dict.commercial_register,
            'the_commercial_charactristic': item_dict.the_commercial_charactristic,
            "cur_user":frappe.session.user,

        }
        result.append(data)

    return result
