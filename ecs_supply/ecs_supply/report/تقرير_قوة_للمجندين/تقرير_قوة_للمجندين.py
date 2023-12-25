# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import statistics
import frappe
from frappe import _

def execute(filters=None):
    columns, data = [], []
    columns = get_columns()
    data = get_data(filters, columns)
    header = ""

    total_count = "<br><b><div style='text-align:center; background-color:black; color:white; display:flex; justify-content:space-around;'> عدد المجندين في التقرير : {0}</div></b>".format(data[0]["total_count"])
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
            "label": _("<b><p style='text-align:center; background-color:#005393; color:white'>رقــــم الشــرطـــة</p></b>"),
            "fieldname": "employee_number",
            "fieldtype": "Data",
            "width": 130
        },
        {
            "label": _("<b><p style='text-align:center; background-color:#005393; color:white'>اســـــم الــمــجــنــد</p></b>"),
            "fieldname": "first_name",
            "fieldtype": "Data",
            "width": 250
        },
		{
            "label": _("<b><p style='text-align:center; background-color:#005393; color:white'>تـاريـخ التـجـنـيـد</p></b>"),
            "fieldname": "date_of_conscription",
            "fieldtype": "Data",
            "width": 250
        },
        {
            "label": _("<b><p style='text-align:center; background-color:#005393; color:white'>العـمـل الــقــائـــم بــه</p></b>"),
            "fieldname": "sup_department",
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
        conditions += """ and EE.employee_number  = '{0}' """.format(filters.get("id_number"))
   
    if filters.get("from_date"):
        conditions += """ and EE.date_of_conscription >= '{0}' """.format(filters.get("from_date"))
    if filters.get("to_date"):
        conditions += """ and EE.date_of_conscription <= '{0}' """.format(filters.get("to_date"))

    result = []
    counter = 0
    data = frappe.db.sql("""
            SELECT 
                EE.name,
                IFNULL(EE.first_name, '') as first_name,
                IFNULL(EE.employee_number, '') as employee_number,
                IFNULL(EE.date_of_conscription, '') as date_of_conscription,
                IFNULL(EE.sup_department, '') as sup_department,
                IFNULL(EE.custom_file_number4, '') as custom_file_number4,
                IFNULL(EE.current_address, '') as current_address,
                IFNULL(EE.territory_of_birth2, '') as territory_of_birth2,
                IFNULL(EE.governorate_of_birth2, '') as governorate_of_birth2,

                CASE
                    WHEN EE.main_department23 = "خارجية (مأموريات)" THEN EE.the_place_of_the_mission
                    WHEN EE.main_department23 = "خارجية (انتدابات)" THEN EE.custom_mandate_authority
                    ELSE EE.main_department23
                END AS main_department23
            FROM
                `tabThe Recruits` EE
            WHERE
                EE.enabled = 1
                {conditions}
            ORDER BY
               EE.date_of_conscription ASC, EE.first_name;

        """.format(conditions=conditions),filters, as_dict=1)
    
    for row in data:
        counter += 1
        first_name = "<p style='text-align:center ; font-weight:bold;'><a href=/app/the-recruits/{0}>{1}</a></p>".format(row.name,row.first_name)
        employee_number = "<p style='text-align:center ; font-weight:bold;'>{0}</p>".format(row.employee_number)
        if row.sup_department is None:
            sup_department = "<p style='text-align:center ; font-weight:bold;'>{0}</p>".format(row.main_department23)
        elif row.sup_department is None and row.main_department23 is None :
            sup_department = "<p style='text-align:center ; font-weight:bold;'>{0}</p>".format(row.main_department23)
        else:
            sup_department = "<p style='text-align:center ; font-weight:bold;'>{1}/{0}</p>".format(row.sup_department, row.main_department23)
        
        custom_file_number4 = "<p style='text-align:center ; font-weight:bold;'>{0}</p>".format(row.custom_file_number4)
        date_of_conscription = "<p style='text-align:center ; font-weight:bold;'>{0}</p>".format(row.date_of_conscription)
        current_address = "<p style='text-align:center ; font-weight:bold;'>{0} _ {1} _ {2}</p>".format(row.current_address,row.territory_of_birth2,row.governorate_of_birth2)

        data_row = {
            'first_name': first_name,
            'employee_number': employee_number,
            'sup_department': sup_department,
            'custom_file_number4': custom_file_number4,
            'current_address':current_address,
            'date_of_conscription':date_of_conscription
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
