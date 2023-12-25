# Copycenter (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import statistics
import frappe
from frappe import _

def execute(filters=None):
    columns, data = [], []
    columns = get_columns()
    data = get_data(filters, columns)
    header = ""

    total_count = "<br><b><div style='text-align:center; background-color:black; color:white; display:flex; justify-content:space-around;'> عدد الضباط في التقرير : {0}</div></b>".format(data[0]["total_count"])
    header = " "   + total_count

    message = [header]
    return columns, data, message

def get_columns():
    return [
         {
            "label": _("<b><p style='text-align:center; background-color:#005393; color:white'>رقــــم المــلــف</p></b>"),
            "fieldname": "custom_file_number4",
            "fieldtype": "Data",
            "width": 130
        },
        {
            "label": _("<b><p style='text-align:center; background-color:#005393; color:white'>رقــــم الأقدميــــة</p></b>"),
            "fieldname": "the_seniority_number",
            "fieldtype": "Data",
            "width": 130
        },
        {
            "label": _("<b><p style='text-align:center; background-color:#005393; color:white'>الرتبـــــــة</p></b>"),
            "fieldname": "policemen_rank",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": _("<b><p style='text-align:center; background-color:#005393; color:white'>اســـــم الضابــــط</p></b>"),
            "fieldname": "first_name",
            "fieldtype": "Data",
            "width": 250
        },
        {
            "label": _("<b><p style='text-align:center; background-color:#005393; color:white'>العـمـل الــقــائـــم بــه</p></b>"),
            "fieldname": "main_department23",
            "fieldtype": "Data",
            "width": 240
        },
        {
            "label": _("<b><p style='text-align:center; background-color:#005393; color:white'>مـحــل الأقــامــة </p></b>"),
            "fieldname": "current_address",
            "fieldtype": "Data",
            "width": 240
        }
    ]


def get_data(filters, columns):
    item_price_qty_data = []
    item_price_qty_data = get_item_price_qty_data(filters)
    return item_price_qty_data


def get_item_price_qty_data(filters):
    conditions = ""
    if filters.get("officer_name"):
        conditions += """ and EE.name = '{0}' """.format(filters.get("officer_name"))
    
    if filters.get("id_number"):
        conditions += """ and EE.the_seniority_number  like '{0}' """.format(filters.get("id_number"))

    if filters.get("rank"):
        conditions += """ and EE.policemen_rank  like '{0}' """.format(filters.get("rank"))

    result = []
    counter = 0
    data = frappe.db.sql("""
        select     
            EE.name,
            IFNULL(EE.first_name, '') as first_name,
            IFNULL(EE.the_seniority_number, '') as the_seniority_number,
            IFNULL(EE.policemen_rank, '') as policemen_rank,
            IFNULL(EE.main_department23, '') as main_department23,
            IFNULL(EE.custom_file_number4, '') as custom_file_number4,
            IFNULL(EE.current_address, '') as current_address,
            IFNULL(EE.territory_of_birth2, '') as territory_of_birth2,
            IFNULL(EE.governorate_of_birth2, '') as governorate_of_birth2,
            IFNULL(EE.sup_department, '') as sup_department
        from
            `tabOfficers Affairs` EE
        where
            EE.enabled = 1
            {conditions}
            ORDER BY num_order asc
        """.format(conditions=conditions), as_dict=1)
    
    for row in data:
        counter += 1
        first_name = "<p style='text-align:center ; font-weight:bold;'><a href=/app/officers-affairs/{0}>{1}</a></p>".format(row.name,row.first_name)
        the_seniority_number = "<p style='text-align:center ; font-weight:bold;'>{0}</p>".format(row.the_seniority_number)
        policemen_rank = "<p style='text-align:center ; font-weight:bold;'>{0}</p>".format(row.policemen_rank)
        main_department23 = "<p style='text-align:center ; font-weight:bold;'>{0} / {1} </p>".format(row.main_department23,row.sup_department)
        custom_file_number4 = "<p style='text-align:center ; font-weight:bold;'>{0}</p>".format(row.custom_file_number4)
        current_address = "<p style='text-align:center ; font-weight:bold;'>{0} _ {1} _ {2}</p>".format(row.current_address,row.territory_of_birth2,row.governorate_of_birth2)

        data_row = {
            'first_name': first_name,
            'the_seniority_number': the_seniority_number,
            'policemen_rank': policemen_rank,
            'main_department23': main_department23,
            'custom_file_number4': custom_file_number4,
            'current_address':current_address

        }
        result.append(data_row)
        

    try:
        result[0]["cur_user"] = frappe.db.get_value("User", frappe.session.user, ["full_name"])
        result[0]["total_count"] = counter
        
    except:
        result.append({"name": "لا يوجـــد"})
        result[0]["cur_user"] = "0"
        result[0]["total_count"] = "0"

    return result