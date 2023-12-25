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
            "label": _("الرتبة"),
            "fieldname": "policemen_rank",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("رقم الشرطة"),
            "fieldname": "employee_number",
            "fieldtype": "Link",
            "options": "Employee",
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
            "width": 150
        },
        {
            "label": _("العمل القائم به"),
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
            "fieldname": "health_details",
            "fieldtype": "Long Text ", 
            "width": 200,
    
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
        {
            "label": _("نتيجة الفرد (احكام)" ),
            "fieldname": "custom_criminal_investigation_result3",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("نتيجة الفرد (معلومات)"),
            "fieldname": "criminal_investigation_result",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("نتيجة اقاربه (احكام)"),
            "fieldname": "result_of_the_investions",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("نتيجة اقاربه (معلومات)"),
            "fieldname": "result_of_the_investions_of_his_relatives",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("قرار الوضع"),
            "fieldname": "position_decision",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("تاريخ الوضع"),
            "fieldname": "position_date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": _("قرار الرفع"),
            "fieldname": "lifting_decision",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("تاريخ الرفع"),
            "fieldname": "lifting_date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": _("السبب"),
            "fieldname": "sn_reason",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("نوع العقوبة"),
            "fieldname": "punishment_type",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("رقم قرار الاحالة"),
            "fieldname": "referral_decision_number",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("تاريخ الاحالة"),
            "fieldname": "referral_date",
            "fieldtype": "Date",
            "width": 150
        },
        {
            "label": _("رقم الدعوة"),
            "fieldname": "call_number",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("قرار مجلس التاديب النهائي"),
            "fieldname": "disciplinary_board_decision",
            "fieldtype": "Data",
            "width": 150
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
        },
		{
            "label": _("ملاحظات"),
            "fieldname": "notes",
            "fieldtype": "Data",
            "width": 130
        },

    ]


def get_data(filters, columns):
    emp = []
    emp = get_emps(filters)
    return emp


def get_emps(filters):
    conditions = ""

    if filters.get("policemen"):
        conditions += " WHERE EE.first_name = %(policemen)s or EE.employee_number = %(policemen)s  or EE.name = %(policemen)s "

            
            

    result = []
    item_results = frappe.db.sql(f"""
        SELECT
            EE.date_of_joining AS date_of_joining ,
            EE.employee_number AS employee_number,
            EE.custom_file_number4 AS custom_file_number4 ,
            EE.sup_department AS sup_department,
            EE.policemen_rank,
            EE.first_name,
            EE.gun_carrying_case,
            EE.health_details3,
            CPI.receipt_the_result_of_political_investigation_date,
            CPI.political_investigation_result,
            CPI.custom_criminal_investigation_result3,
            CPI.criminal_investigation_result,
            CPI.result_of_the_investions,
            CPI.result_of_the_investions_of_his_relatives,
            SN.position_decision,
            SN.position_date,
            SN.reason as sn_reason,
            SN.lifting_decision,          
            SN.lifting_date,
            SN.employee_name AS secret_emp_name,
            pp.policeman_name,
            pp.punishment_type,
            pp.referral_decision_number,
            pp.referral_date,
            pp.call_number,
            pp.disciplinary_board_decision,
            CT.employee as ct_employee,
            CT.employee_name,
            CT.the_case_number,
            CT.the_charge,
            CT.public_prosecution_decision,
            CT.the_courts_decision,
            CT.date_of_the_decision,
            CT.date_of_the_decision2,
            CT.his_attitude_to_work,
            CT.notes,
            CASE
                WHEN EE.health_details3 = 'غير طبيعية' THEN EE.health_details2
                ELSE NULL 
            END AS health_details,                    
            
            CASE
                WHEN  EE.gun_carrying_case = 'غير مصرح عضوي'       THEN EE.reason 
                WHEN  EE.gun_carrying_case = 'غير مصرح نفسي'       THEN EE.reason 
                WHEN  EE.gun_carrying_case = 'غير مصرح إحترازي'    THEN EE.reason 
                ELSE NULL
            END AS reason 
        
        FROM
            `tabEnvestigation Employee` EE 
  
        LEFT JOIN 
            `tabCriminal And Political Investigation` CPI
        ON EE.name = CPI.recruit
                                                                  
        LEFT JOIN 
            `tabSecret Notes` SN
        ON SN.employee_name = EE.first_name 
                                 
        LEFT JOIN 
            `tabPolicemen Punishment` pp
        ON pp.policeman_name = EE.employee_number 
       
        LEFT JOIN 
            `tabCriminal Trials` CT
        ON pp.policeman_name = EE.employee_number 
                                 
        {conditions}
        GROUP BY EE.first_name

        """.format(conditions=conditions), filters, as_dict=1)

    for item_dict in item_results:
        if not frappe.db.exists("Secret Notes",{"employee_name":item_dict.first_name}):
            secret_emp_name ="null"
        else:
            secret_emp_name=item_dict.secret_emp_name
        
        if not frappe.db.exists("Policemen Punishment",{"policeman_name":item_dict.employee_number}):
            pp_name ="null"
        else:
            pp_name=item_dict.policeman_name
        
        if not frappe.db.exists("Criminal Trials",{"employee":item_dict.employee_number}):
            ct_employee ="null"
        else:
            ct_employee=item_dict.ct_employee
        
    
        
        data = {
            'date_of_joining':item_dict.date_of_joining,
            'custom_file_number4': item_dict.custom_file_number4,
            'employee_number': item_dict.employee_number,
            'first_name': item_dict.first_name,
            'policemen_rank': item_dict.policemen_rank,
            'sup_department':item_dict.sup_department,
            'gun_carrying_case':item_dict.gun_carrying_case,
            'reason': item_dict.reason,
            'health_details3':item_dict.health_details3,
            'health_details':item_dict.health_details,
            "cur_user":frappe.session.user,
            'political_investigation_result': item_dict.political_investigation_result,
            'receipt_the_result_of_political_investigation_date': item_dict.receipt_the_result_of_political_investigation_date,
            'custom_criminal_investigation_result3': item_dict.custom_criminal_investigation_result3,
            'criminal_investigation_result': item_dict.criminal_investigation_result,
            'result_of_the_investions': item_dict.result_of_the_investions,
            'result_of_the_investions_of_his_relatives': item_dict.result_of_the_investions_of_his_relatives,
            'position_decision': item_dict.position_decision,
            'position_date': item_dict.position_date,
            'lifting_decision': item_dict.lifting_decision,
            'lifting_date': item_dict.lifting_date,
            'sn_reason': item_dict.sn_reason,
            'secret_emp_name':secret_emp_name,
            'disciplinary_board_decision':item_dict.disciplinary_board_decision,
            'call_number':item_dict.call_number,
            'referral_date':item_dict.referral_date,
            'referral_decision_number':item_dict.referral_decision_number,
            'punishment_type':item_dict.punishment_type,
            'policeman_name':pp_name,
            'the_case_number': item_dict.the_case_number,
            'the_charge': item_dict.the_charge,
            'public_prosecution_decision': item_dict.public_prosecution_decision,
            'the_courts_decision': item_dict.the_courts_decision,
            'date_of_the_decision': item_dict.date_of_the_decision,
			'date_of_the_decision2': item_dict.date_of_the_decision2,
			'his_attitude_to_work': item_dict.his_attitude_to_work,
			'notes': item_dict.notes,
            'ct_employee':ct_employee
        }
        result.append(data)

  
    return result

