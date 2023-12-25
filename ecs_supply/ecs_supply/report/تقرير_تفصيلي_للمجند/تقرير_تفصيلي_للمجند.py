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
            "label": _("رقم الملف"),
            "fieldname": "custom_file_number4",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": _("رقم الشرطة"),
            "fieldname": "employee_number",
            "fieldtype": "Link",
            "options": "Employee",
            "width": 100
        },
        {
            "label": _("تاريخ التجنيد"),
            "fieldname": "date_of_conscription",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("المؤهل الدراسي"),
            "fieldname": "the_academic_qualification",
            "fieldtype": "Data",
            "width": 250
        },
        {
            "label": _("أسم"),
            "fieldname": "first_name",
            "fieldtype": "Data",
            "width": 250
        },
        {
            "label": _("محل الإقامة"),
            "fieldname": "current_address",
            "fieldtype": "Data",
            "width": 250
        },
        {
            "label": _("تاريخ الالتحاق بالإدارة"),
            "fieldname": "date_of_joining",
            "fieldtype": "Data",
            "width": 250
        },
        {
            "label": _("العمل المسند له"),
            "fieldname": "sup_department",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("موقفه من حمل السلاح"),
            "fieldname": "gun_carrying_case",
            "fieldtype": "Data",
            "width": 110
        },
        {
            "label": _("السبب"),
            "fieldname": "reason",
            "fieldtype": "Long Text",
            "width": 150,
    
        },
        {
            "label": _("الحالة النفسية"),
            "fieldname": "health_details3",
            "fieldtype": "Data",
            "width": 110
        },
        {
            "label": _("تفاصيل الحالة"),
            "fieldname": "health_details2",
            "fieldtype": "Long Text ", 
            "width": 200,
    
        },
        # الكشف الجنائي والسياسي
        # {
        #     "label": _(" تاريخ الوارد الأمن الوطني"),
        #     "fieldname": "receipt_the_result_of_political_investigation_date",
        #     "fieldtype": "Date",
        #     "width": 200
        # },
        # {
        #     "label": _("النتيجة"),
        #     "fieldname": "political_investigation_result",
        #     "fieldtype": "Data",
        #     "width": 200
        # },
        # {
        #     "label": _("نتيجة الفرد (احكام)" ),
        #     "fieldname": "custom_criminal_investigation_result3",
        #     "fieldtype": "Data",
        #     "width": 200
        # },
        # {
        #     "label": _("نتيجة الفرد (معلومات)"),
        #     "fieldname": "criminal_investigation_result",
        #     "fieldtype": "Data",
        #     "width": 200
        # },
        # {
        #     "label": _("نتيجة اقاربه (احكام)"),
        #     "fieldname": "result_of_the_investions",
        #     "fieldtype": "Data",
        #     "width": 200
        # },
        # {
        #     "label": _("نتيجة اقاربه (معلومات)"),
        #     "fieldname": "result_of_the_investions_of_his_relatives",
        #     "fieldtype": "Data",
        #     "width": 200
        # },
        # {
        #     "label": _("قرار الوضع"),
        #     "fieldname": "position_decision",
        #     "fieldtype": "Data",
        #     "width": 150
        # },
        # {
        #     "label": _("تاريخ الوضع"),
        #     "fieldname": "position_date",
        #     "fieldtype": "Date",
        #     "width": 120
        # },
        # {
        #     "label": _("قرار الرفع"),
        #     "fieldname": "lifting_decision",
        #     "fieldtype": "Data",
        #     "width": 150
        # },
        # {
        #     "label": _("تاريخ الرفع"),
        #     "fieldname": "lifting_date",
        #     "fieldtype": "Date",
        #     "width": 120
        # },
        # {
        #     "label": _("السبب"),
        #     "fieldname": "sn_reason",
        #     "fieldtype": "Data",
        #     "width": 150
        # },
        # {
        #     "label": _("نوع العقوبة"),
        #     "fieldname": "punishment_type",
        #     "fieldtype": "Data",
        #     "width": 150
        # },
        # {
        #     "label": _("رقم قرار الاحالة"),
        #     "fieldname": "referral_decision_number",
        #     "fieldtype": "Data",
        #     "width": 150
        # },
        # {
        #     "label": _("تاريخ الاحالة"),
        #     "fieldname": "referral_date",
        #     "fieldtype": "Date",
        #     "width": 150
        # },
        # {
        #     "label": _("رقم الدعوة"),
        #     "fieldname": "call_number",
        #     "fieldtype": "Data",
        #     "width": 150
        # },
        # {
        #     "label": _("قرار مجلس التاديب النهائي"),
        #     "fieldname": "disciplinary_board_decision",
        #     "fieldtype": "Data",
        #     "width": 150
        # },
        # {
        #     "label": _("رقم القضية"),
        #     "fieldname": "the_case_number",
        #     "fieldtype": "Data",
        #     "width": 100
        # },
        # {
        #     "label": _("التهمة"),
        #     "fieldname": "the_charge",
        #     "fieldtype": "Data",
        #     "width": 100
        # },
        # {
        #     "label": _("قرار النيابة العامة"),
        #     "fieldname": "public_prosecution_decision",
        #     "fieldtype": "Data",
        #     "width": 250
        # },
        # {
        #     "label": _("قرار المحكمة"),
        #     "fieldname": "the_courts_decision",
        #     "fieldtype": "Data",
        #     "width": 130
        # },
        # {
        #     "label": _("تاريخ القرار"),
        #     "fieldname": "date_of_the_decision",
        #     "fieldtype": "Date",
        #     "width": 100
        # },
        # {
        #     "label": _("تاريخ القرار"),
        #     "fieldname": "date_of_the_decision2",
        #     "fieldtype": "Date",
        #     "width": 100
        # },
        # {
        #     "label": _("موقفه من العمل"),
        #     "fieldname": "his_attitude_to_work",
        #     "fieldtype": "Data",
        #     "width": 130
        # },
        # {
        #     "label": _("ملاحظات"),
        #     "fieldname": "notes",
        #     "fieldtype": "Data",
        #     "width": 130
        # },

    ]


def get_data(filters, columns):
    emp = []
    emp = get_emps(filters)
    return emp


def get_emps(filters):
    conditions = ""

    if filters.get("policemen"):
        conditions += " WHERE TR.first_name = %(policemen)s or TR.employee_number = %(policemen)s  or TR.name = %(policemen)s "

            
            

    result = []
    item_results = frappe.db.sql(f"""
        SELECT
            TR.date_of_joining AS date_of_joining ,
            TR.employee_number AS employee_number,
            TR.custom_file_number4 AS custom_file_number4 ,
            TR.sup_department AS sup_department,
            TR.first_name,
            TR.gun_carrying_case,
            TR.health_details3,
            TR.health_details2,
            TR.the_academic_qualification,
            TR.current_address,
            TR.date_of_conscription,
            CASE
                WHEN TR.health_details3 = 'غير طبيعية' THEN TR.health_details2
                ELSE NULL 
            END AS health_details,                    
            
            CASE
                WHEN  TR.gun_carrying_case = 'غير مصرح عضوي'       THEN TR.reason 
                WHEN  TR.gun_carrying_case = 'غير مصرح نفسي'       THEN TR.reason 
                WHEN  TR.gun_carrying_case = 'غير مصرح إحترازي'    THEN TR.reason 
                ELSE NULL
            END AS reason 
        
        FROM
            `tabThe Recruits` TR 

                                 
        {conditions}
        GROUP BY TR.first_name

        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:

        
        data = {
            'date_of_joining':item_dict.date_of_joining,
            'custom_file_number4': item_dict.custom_file_number4,
            'employee_number': item_dict.employee_number,
            'first_name': item_dict.first_name,
            'sup_department':item_dict.sup_department,
            'gun_carrying_case':item_dict.gun_carrying_case,
            'reason': item_dict.reason,
            'health_details3':item_dict.health_details3,
            'health_details2':item_dict.health_details2,
            'date_of_conscription':item_dict.date_of_conscription,
            'the_academic_qualification':item_dict.the_academic_qualification,
            'current_address':item_dict.current_address,
            "cur_user":frappe.session.user
        }
        result.append(data)
    result.append({"header":frappe.get_value('File','47d71d9839')})
  
    return result

