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
    statistics = "<b><div style='text-align:center; background-color:lightblue; color:darkblue; display:flex; justify-content:space-around;'><div>عدد الافراد : {0}</div>".format(data[0]["total_officers"])
    statistics += "<div>عدد الافراد المدرجين : {0}</div>".format(data[0]["listed_officers"])
    statistics += "<div> عدد الافراد الغير مدرجين : {0}</div>".format(data[0]["unlisted_officers"])
    statistics += "<div> عدد الافراد المدرجين وتم طباعتهم : {0}</div>".format(data[0]["printed_officers"])
    statistics += "<div> عدد الافراد المدرجين ولم يتم طباعتهم : {0}</div></div></b>".format(data[0]["unprinted_officers"])
    total_count = "<br><b><div style='text-align:center; background-color:black; color:white; display:flex; justify-content:space-around;'> عدد الافراد في التقرير : {0}</div></b>".format(data[0]["total_count"])
    header = " "  + statistics + total_count

    message = [header]
    return columns, data, message

def get_columns():
    return [
                {
            "label": _("<b><p style='text-align:center; background-color:#005393; color:white'>رقــم الأقــدمــيــة</p></b>"),
            "fieldname": "id_number",
            "fieldtype": "Data",
            "width": 240
        },
        {
            "label": _("<b><p style='text-align:center; background-color:#005393; color:white'>الرتبـــــــة</p></b>"),
            "fieldname": "rank",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": _("<b><p style='text-align:center; background-color:#005393; color:white'>اســـــم الفــرد</p></b>"),
            "fieldname": "name",
            "fieldtype": "Data",
            "width": 250
        },
        {
            "label": _("<b><p style='text-align:center; background-color:#005393; color:white'>الجهـــــــــة</p></b>"),
            "fieldname": "entities",
            "fieldtype": "Data",
            "width": 240
        },
		{
            "label": _("<b><p style='text-align:center; background-color:#005393; color:white'>سبــب الاستحقــاق</p></b>"),
            "fieldname": "reason_for_entitlement",
            "fieldtype": "Data",
            "width": 130
        },
        {
            "label": _("<b><p style='text-align:center; background-color:#005393; color:white'>العمل المسند إليه</p></b>"),
            "fieldname": "assigned_work",
            "fieldtype": "Data",
            "width": 240
        },     
        {
            "label": _("<b><p style='text-align:center; background-color:#005393; color:white'>حالة الطباعـة</p></b>"),
            "fieldname": "print",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": _("<b><p style='text-align:center; background-color:#005393; color:white'>تاريخ الطباعـة</p></b>"),
            "fieldname": "print_date",
            "fieldtype": "Date",
            "width": 110
        },
        {
            "label": _("<b><p style='text-align:center; background-color:#005393; color:white'>السنـة الماليـة</p></b>"),
            "fieldname": "fiscal_year",
            "fieldtype": "Data",
            "width": 110
        },
    ]


def get_data(filters, columns):
    item_price_qty_data = []
    item_price_qty_data = get_item_price_qty_data(filters)
    return item_price_qty_data


def get_item_price_qty_data(filters):
    conditions = ""
    if filters.get("people_name"):
        conditions += """ and people_name like '%{0}%' """.format(filters.get("people_name"))
    if filters.get("id_number"):
        conditions += """ and id_number  = '{0}' """.format(filters.get("id_number"))
    if filters.get("name"):
        conditions += """ and name  = '{0}' """.format(filters.get("name"))

    if filters.get("entities"):
        conditions += """ and entities  = '{0}' """.format(filters.get("entities"))

    if filters.get("rank"):
        conditions += """ and rank  = '{0}' """.format(filters.get("rank"))

    if filters.get("fiscal_year"):
        conditions += """ and fiscal_year  = '{0}' """.format(filters.get("fiscal_year"))

    if filters.get("listed_unlisted") == "مدرج":
        conditions += " and reason_for_entitlement not in ('غير مدرج','غير مدرج للتكرار') "

    if filters.get("listed_unlisted") == "غير مدرج":
        conditions += " and reason_for_entitlement in ('غير مدرج','غير مدرج للتكرار') "
        
    if filters.get("reason_for_entitlement"):
        conditions += """ and reason_for_entitlement  = '{0}' """.format(filters.get("reason_for_entitlement"))

    if filters.get("assigned_work"):
        conditions += """ and assigned_work  = '{0}' """.format(filters.get("assigned_work"))

    if filters.get("print"):
        conditions += """ and print  = '{0}' """.format(filters.get("print"))
    if conditions != "" :        
        result = []
        counter = 0
        data = frappe.db.sql("""
            select EE.name,EE.people_name,EE.rank,EE.entities,EE.reason_for_entitlement,EE.assigned_work,EE.print,EE.print_date,EE.fiscal_year,EE.assigned_work,EE.id_number
            from
                `tabCivilian Clothing For People` EE
            Join `tabPolicemen Rank` R
            ON R.name = EE.rank
            where
                1=1
                {conditions}
        ORDER BY CAST(R.code AS SIGNED) DESC;
            """.format(conditions=conditions), as_dict=1)
    else:
        result = []
        data ={}

    total_officers = frappe.db.sql("""
		select count(*) as count
        from
			`tabCivilian Clothing For People`
		where
			fiscal_year = '{fiscal_year}'
		""".format(fiscal_year=filters.get("fiscal_year")), filters, as_dict=1)
    
    listed_officers = frappe.db.sql("""
		select count(*) as count
        from
			`tabCivilian Clothing For People`
		where
			fiscal_year = '{fiscal_year}'
            and reason_for_entitlement not in ('غير مدرج','غير مدرج للتكرار')
		""".format(fiscal_year=filters.get("fiscal_year")), filters, as_dict=1)
    
    unlisted_officers = frappe.db.sql("""
		select count(*) as count
        from
			`tabCivilian Clothing For People`
		where
			fiscal_year = '{fiscal_year}'
            and reason_for_entitlement in ('غير مدرج','غير مدرج للتكرار')
		""".format(fiscal_year=filters.get("fiscal_year")), filters, as_dict=1)
    
    printed_officers = frappe.db.sql("""
		select count(*) as count
        from
			`tabCivilian Clothing For People`
		where
			fiscal_year = '{fiscal_year}'
            and reason_for_entitlement not in ('غير مدرج','غير مدرج للتكرار')
            and print = "تم الطباعه"
		""".format(fiscal_year=filters.get("fiscal_year")), filters, as_dict=1)
    
    unprinted_officers = frappe.db.sql("""
		select count(*) as count
        from
			`tabCivilian Clothing For People`
		where
			fiscal_year = '{fiscal_year}'
            and reason_for_entitlement not in ('غير مدرج','غير مدرج للتكرار')
            and (print = "لم يتم الطباعه" or print is null)
		""".format(fiscal_year=filters.get("fiscal_year")), filters, as_dict=1)
    
    for row in data:
        counter += 1
        name = "<p style='text-align:right'><a href=/app/civilian-clothing-for-people/{0}>{1}</a></p>".format(row.name,row.people_name)
        rank = "<p style='text-align:right'>{0}</p>".format(row.rank)
        entities = "<p style='text-align:right'>{0}</p>".format(row.entities)
        reason_for_entitlement = "<p style='text-align:right'>{0}</p>".format(row.reason_for_entitlement)
        assigned_work = "<p style='text-align:right'>{0}</p>".format(row.assigned_work)
        print = "<p style='text-align:right'>{0}</p>".format(row.print)
        print_date = "<p style='text-align:right'>{0}</p>".format(row.print_date)
        fiscal_year = "<p style='text-align:right'>{0}</p>".format(row.fiscal_year)
        assigned_work = "<p style='text-align:right'>{0}</p>".format(row.assigned_work)
        id_number = "<p style='text-align:right'>{0}</p>".format(row.id_number)
        data_row = {
            'name': name,
            'rank': rank,
            'entities': entities,
            'reason_for_entitlement': reason_for_entitlement,
            'assigned_work': assigned_work,
            'print': print,
            'print_date': print_date,
            'fiscal_year': fiscal_year,
            'assigned_work': assigned_work,
            'id_number': id_number,
        }
        result.append(data_row)
        

    try:
        result[0]["cur_user"] = frappe.db.get_value("User", frappe.session.user, ["full_name"])
        result[0]["total_count"] = counter
        if filters.get("fiscal_year"):
            result[0]["total_officers"] = str(total_officers[0]['count']) 
            result[0]["listed_officers"] = str(listed_officers[0]['count']) 
            result[0]["unlisted_officers"] = str(unlisted_officers[0]['count']) 
            result[0]["printed_officers"] = str(printed_officers[0]['count'])
            result[0]["unprinted_officers"] = str(unprinted_officers[0]['count']) 
        else:
            result[0]["total_officers"] = "0"
            result[0]["listed_officers"] = "0"
            result[0]["unlisted_officers"] = "0"
            result[0]["printed_officers"] = "0"
            result[0]["unprinted_officers"] = "0"

    except:
        result.append({"name": "لا يوجـــد"})
        result[0]["cur_user"] = "0"
        result[0]["total_count"] = "0"
        result[0]["total_officers"] = "0"
        result[0]["listed_officers"] = "0"
        result[0]["unlisted_officers"] = "0"
        result[0]["printed_officers"] = "0"
        result[0]["unprinted_officers"] = "0"
    return result