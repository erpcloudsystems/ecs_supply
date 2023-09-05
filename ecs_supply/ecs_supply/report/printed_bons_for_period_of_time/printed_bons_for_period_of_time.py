# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    columns, data = [], []
    columns = get_columns()
    data = get_data(filters, columns)
    return columns, data

def get_columns():
    return [
        {
            "label": _("الجهة"),
            "fieldname": "entities",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("الاسم"),
            "fieldname": "personal_name",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("سبب الاستحقاق"),
            "fieldname": "reason_for_entitlement",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("رقم شرطي"),
            "fieldname": "id_number",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("الرتبة"),
            "fieldname": "rank",
            "fieldtype": "Data",
            "width": 150
        },
       
        
        {
            "label": _("نوع"),
            "fieldname": "type",
            "fieldtype": "Data",
            "width": 150
        },
         {
            "label": _("تاريخ الطباعة"),
            "fieldname": "print_date",
            "fieldtype": "Date",
            "width": 150
        },
    ]


def get_data(filters, columns):
    item_price_qty_data = []
    item_price_qty_data = get_item_price_qty_data(filters)
    return item_price_qty_data


def get_item_price_qty_data(filters):
    conditions = ""
    conditions1 = ""
    if filters.get("entities"):
        conditions += " and entities = %(entities)s"
    # if filters.get("reason_for_entitlement"):
    #     conditions += "and reason_for_entitlement = %(reason_for_entitlement)s"
    if filters.get("fiscal_year"):
        conditions += " and fiscal_year = %(fiscal_year)s"
    if filters.get("from_date"):
        conditions += " and print_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and print_date <= %(to_date)s"

    result = []
    data = frappe.db.sql("""
                (
                    select entities as entities, officer_name as personal_name, reason_for_entitlement as reason_for_entitlement,
                id_number as id_number, rank as rank, "ضباط" as type, print_date as print_date
                from
                    `tabCivilian Clothing For Officers`
                where
                    reason_for_entitlement not in  ("غير مدرج", "غير مدرج للتكرار")
                and print = "تم الطباعه"
                    {conditions}
                    ) 
            union
                    (
                    select entities as entities, people_name as personal_name, reason_for_entitlement as reason_for_entitlement,
                id_number as id_number, rank as rank, "افراد" as type, print_date as print_date
                from
                    `tabCivilian Clothing For People` 
                where
                    reason_for_entitlement not in  ("غير مدرج", "غير مدرج للتكرار")
                and print = "تم الطباعه"

                    {conditions}
                    ) 
                    ORDER BY print_date
                """.format(conditions=conditions, entities=filters.get("entities")), filters, as_dict=1)
    for row in data:
        data_row = {
            'entities': row.entities,
            'personal_name': row.personal_name,
            'reason_for_entitlement': row.reason_for_entitlement,
            'id_number': row.id_number,
            'rank': row.rank,
            'type': row.type,
            'print_date': row.print_date,
        }
        result.append(data_row)
        

    try:

        result[0]["cur_user"] = frappe.db.get_value("User", frappe.session.user, ["full_name"])
    except:
        pass
    return result