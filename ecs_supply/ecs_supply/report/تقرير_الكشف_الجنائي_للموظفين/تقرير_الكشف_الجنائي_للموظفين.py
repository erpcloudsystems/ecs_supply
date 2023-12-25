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
                "options":"Criminal And Political Disclosure Of Human Resources",
                "width": 100
            },
            {
                "label": _("الاسم"),
                "fieldname": "first_name",
                "fieldtype": "Data",
                "width": 200
            },
            {
                "label": _("رقم الصادر"),
                "fieldname": "send_investigation_number",
                "fieldtype": "Data",
                "width": 200
            },  
            {
                "label": _("تاريخ الصادر"),
                "fieldname": "criminal_investigation_date",
                "fieldtype": "Date",
                "width": 200
            },  
            {
                "label": _("رقم الوارد"),
                "fieldname": "investigation_entry_number",
                "fieldtype": "Data",
                "width": 200
            },  
            {
                "label": _("تاريخ الوارد"),
                "fieldname": "receipt_the_result_of_criminal_investigation_date",
                "fieldtype": "Date",
                "width": 200
            }          
        ]
        return columns
        
    elif filters.get("filter"):
        filter_option = filters.get("filter")
        if "احكام موظفين" in filter_option:
            return [
                {
                "label": _("المستند"),
                "fieldname": "docname",
                "fieldtype": "Link",
                "options":"Criminal And Political Disclosure Of Human Resources",
                "width": 100
                },
                {
                "label": _("الاسم"),
                "fieldname": "first_name",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("رقم القضية"),
                "fieldname": "case_number_1",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("رقم الحصر"),
                "fieldname": "limited_number_1",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("كلي مستأنف"),
                "fieldname": "im_all_resumed_1",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("التهمة"),
                "fieldname": "the_charge_1",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("الحكم"),
                "fieldname": "the_ruling_1",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("تاريخ الجلسة"),
                "fieldname": "date_of_the_session_1",
                "fieldtype": "Date",
                "width": 200
                },
                {
                "label": _("العقوبة"),
                "fieldname": "the_punishment_1",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("التصرفات"),
                "fieldname": "acts_1",
                "fieldtype": "Data",
                "width": 200
                },  
            ]

        elif "احكام الاقارب" in filter_option:
            return [
                {
                "label": _("المستند"),
                "fieldname": "docname",
                "fieldtype": "Link",
                "options":"Criminal And Political Disclosure Of Human Resources",
                "width": 100
                },
                {
                "label": _("الاسم"),
                "fieldname": "first_name",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("المحكوم عليه"),
                "fieldname": "the_convict",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("صله القرابة"),
                "fieldname": "the_connection_of_the_kinah_1",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("رقم القضية"),
                "fieldname": "case_number_2",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("رقم الحصر"),
                "fieldname": "limited_number_2",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("كلي مستأنف"),
                "fieldname": "im_all_resumed_2",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("التهمة"),
                "fieldname": "the_charge_2",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("الحكم"),
                "fieldname": "the_ruling_2",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("تاريخ الجلسة"),
                "fieldname": "date_of_the_session_2",
                "fieldtype": "Date",
                "width": 200
                },
                {
                "label": _("العقوبة"),
                "fieldname": "the_punishment_2",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("التصرفات"),
                "fieldname": "acts_2",
                "fieldtype": "Data",
                "width": 200
                },  
            ]

        elif "معلومات موظفين" in filter_option:
            return [
                {
                "label": _("المستند"),
                "fieldname": "docname",
                "fieldtype": "Link",
                "options":"Criminal And Political Disclosure Of Human Resources",
                "width": 100
                },
                {
                "label": _("الاسم"),
                "fieldname": "first_name",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("رقم القضية"),
                "fieldname": "case_number_4",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("التهمة"),
                "fieldname": "the_charge_4",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("التصرفات"),
                "fieldname": "acts_4",
                "fieldtype": "Data",
                "width": 200
                },    
               
            ]

        elif "معلومات الاقارب" in filter_option:
            return [
                {
                "label": _("المستند"),
                "fieldname": "docname",
                "fieldtype": "Link",
                "options":"Criminal And Political Disclosure Of Human Resources",
                "width": 100
                },
                {
                "label": _("الاسم"),
                "fieldname": "first_name",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("المتهم"),
                "fieldname": "the_accused",
                "fieldtype": "Data",
                "width": 200
                }, 
                {
                "label": _("صلة القرابه"),
                "fieldname": "the_connection_of_the_kinah_2",
                "fieldtype": "Data",
                "width": 200
                },   
                {
                "label": _("رقم القضية"),
                "fieldname": "case_number_5",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("التهمة"),
                "fieldname": "the_charge_5",
                "fieldtype": "Data",
                "width": 200
                },
                {
                "label": _("التصرفات"),
                "fieldname": "acts_5",
                "fieldtype": "Data",
                "width": 200
                },    
               
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
        conditions += f" AND EMP.name = '{filters['recruit']}' "
        values["recruit"] = filters["recruit"]
    result = []
    basic_data = frappe.db.sql("""
        SELECT
            EMP.first_name,
            CPI.name AS docname
        FROM
            `tabCriminal And Political Disclosure Of Human Resources` CPI
        JOIN
            `tabHuman Resources` EMP
                                               
        ON EMP.name = CPI.the_one_who_is_looking_for 
        WHERE EMP.enabled = 1
        {conditions}
            """.format(conditions= conditions),as_dict=1)           
    
    for item_dict in basic_data:
        values["name"] = item_dict.docname 
        if not filters.get("filter"):
            first_table =frappe.db.sql("""
                SELECT 
                    TROR.send_investigation_number,
                    TROR.criminal_investigation_date,
                    TROR.investigation_entry_number,
                    TROR.receipt_the_result_of_criminal_investigation_date
                FROM
                    `tabCriminal Security For Human Resources` TROR
                                            
                WHERE TROR.parent = %(name)s 
            """, values,as_dict=1)  
            
            if first_table:
                for item in first_table:
                    data={
                        'docname': item_dict.docname,
                        'first_name': item_dict.first_name,
                        "cur_user": frappe.session.user,
                        "send_investigation_number": item.send_investigation_number,
                        "criminal_investigation_date": item.criminal_investigation_date,
                        "investigation_entry_number": item.investigation_entry_number,
                        "receipt_the_result_of_criminal_investigation_date": item.receipt_the_result_of_criminal_investigation_date,
                    }
                    result.append(data)

        else:   
            second_table = frappe.db.sql("""
                SELECT
                    TRJT.the_case_number AS case_number_1,
                    TRJT.limited_number AS limited_number_1,
                    TRJT.im_all_resumed AS im_all_resumed_1,
                    TRJT.the_charge AS the_charge_1,
                    TRJT.the_ruling AS the_ruling_1,
                    TRJT.date_of_the_session AS date_of_the_session_1,
                    TRJT.the_punishment AS the_punishment_1,
                    TRJT.acts AS acts_1
                FROM
                    `tabThe Employee Result Is Provisions Table` TRJT
                WHERE
                    TRJT.parent = %(name)s
            """, values,as_dict=1)
            
            if second_table and "احكام موظفين" in filters.get("filter"):
                for item in second_table:
                    data={
                        'docname': item_dict.docname,
                        'first_name': item_dict.first_name,
                        "cur_user": frappe.session.user,
                        "case_number_1": item.case_number_1,
                        "limited_number_1": item.limited_number_1,
                        "im_all_resumed_1": item.im_all_resumed_1,
                        "the_charge_1": item.the_charge_1,
                        "the_ruling_1": item.the_ruling_1,
                        "date_of_the_session_1": item.date_of_the_session_1,
                        "the_punishment_1": item.the_punishment_1,
                        "acts_1": item.acts_1,
                    }
                    result.append(data)
    
            third_table=frappe.db.sql("""
                SELECT
                    RTI.the_convict,
                    RTI.the_connection_of_the_kinah AS the_connection_of_the_kinah_1,
                    RTI.the_case_number AS case_number_2,
                    RTI.limited_number AS  limited_number_2,
                    RTI.im_all_resumed AS  im_all_resumed_2,
                    RTI.the_charge AS  the_charge_2,
                    RTI.the_ruling AS the_ruling_2,
                    RTI.date_of_the_session AS date_of_the_session_2,
                    RTI.the_punishment AS the_punishment_2,
                    RTI.acts AS acts_2
                FROM
                    `tabResult Of His Relatives Is Judgments Table` RTI               
                WHERE
                    RTI.parent = %(name)s
            """, values,as_dict=1)
            
            if third_table and "احكام الاقارب" in filters.get("filter"):
                for item in third_table:
                    data={
                        'docname': item_dict.docname,
                        'first_name': item_dict.first_name,
                        "cur_user": frappe.session.user,
                        "the_convict": item.the_convict,  
                        "the_connection_of_the_kinah_1": item.the_connection_of_the_kinah_1,
                        "case_number_2": item.case_number_2,
                        "limited_number_2": item.limited_number_2,
                        "the_ruling_2": item.the_ruling_2,
                        "im_all_resumed_2": item.im_all_resumed_2,
                        "the_charge_2": item.the_charge_2,
                        "date_of_the_session_2": item.date_of_the_session_2,
                        "the_punishment_2": item.the_punishment_2,
                        "acts_2": item.acts_2
                    }
                    result.append(data)
            
            forth_table=frappe.db.sql("""
                SELECT
                    RIT.the_case_number AS case_number_4 ,
                    RIT.the_charge AS the_charge_4 ,
                    RIT.acts AS acts_4
                FROM
                    `tabThe Result Of The Employee Information Table` RIT
                                        
                WHERE
                    RIT.parent = %(name)s
            """, values,as_dict=1)
            if forth_table and "معلومات موظفين" in filters.get("filter"):
                for item in forth_table:
                    data={
                        'docname': item_dict.docname,
                        'first_name': item_dict.first_name,
                        "cur_user": frappe.session.user,
                        "case_number_4": item.case_number_4,  
                        "the_charge_4": item.the_charge_4,
                        "acts_4": item.acts_4,
                    }
                    result.append(data)

            
            fifth_table=frappe.db.sql("""
                SELECT              
                    RIHT.the_accused,
                    RIHT.the_connection_of_the_kinah AS the_connection_of_the_kinah_2,
                    RIHT.the_case_number AS case_number_5,
                    RIHT.the_charge AS the_charge_5,
                    RIHT.acts AS acts_5
                FROM
                    `tabResult Of The Employee Relatives Is Information` RIHT
                WHERE
                    RIHT.parent = %(name)s
            """, values,as_dict=1)
            
            if fifth_table and "معلومات الاقارب" in filters.get("filter"):
                for item in fifth_table:
                    data={
                        'docname': item_dict.docname,
                        'first_name': item_dict.first_name,
                        "cur_user": frappe.session.user,
                        "the_accused": item.the_accused,  
                        "the_connection_of_the_kinah_2": item.the_connection_of_the_kinah_2,
                        "case_number_5": item.case_number_5,
                        "the_charge_5": item.the_charge_5,
                        "acts_5": item.acts_5,
                    }
                    result.append(data)        

    return result
