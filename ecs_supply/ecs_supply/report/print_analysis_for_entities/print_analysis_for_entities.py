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
            "fieldname": "entity",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("عدد مستحقي الصرف"),
            "fieldname": "valid_exchangers",
            "fieldtype": "Integer",
            "width": 150
        },
        {
            "label": _("عدد ما تم صرفه"),
            "fieldname": "exchanged_amount",
            "fieldtype": "Integer",
            "width": 200
        },
        {
            "label": _("عدد ما لم يتم صرفه"),
            "fieldname": "not_exchanged_amount",
            "fieldtype": "Integer",
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
        conditions1 += "and entities = %(entities)s"

    if filters.get("reason_for_entitlement"):
        conditions += "and reason_for_entitlement = %(reason_for_entitlement)s"
    if filters.get("fiscal_year"):
        conditions += "and fiscal_year = %(fiscal_year)s"
    if filters.get("from_date"):
        conditions += " and print_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and print_date <= %(to_date)s"

    result = []
    
        
    if filters.get("title") == "ضباط":
        entities = frappe.db.sql("""
            SELECT 
             entities as entities
        FROM `tabCivilian Clothing For Officers` 
        where 1=1
        {conditions1}

        GROUP BY entities
            """.format(conditions1=conditions1),filters,as_dict=1)
        if entities:
            for entity in entities:
                count1 = frappe.db.sql("""
                    select
                        COUNT(name) as count
                    from
                        `tabCivilian Clothing For Officers` 
                    where
                        `tabCivilian Clothing For Officers`.reason_for_entitlement not in  ("غير مدرج", "غير مدرج للتكرار")
                    and 
                        `tabCivilian Clothing For Officers`.entities = "{entity}"
                        {conditions}
                    """.format(conditions=conditions, entity=entity.entities), filters, as_dict=1)
                
                count2 = frappe.db.sql("""
                    select
                        COUNT(name) as count
                    from
                        `tabCivilian Clothing For Officers` 
                    where
                        `tabCivilian Clothing For Officers`.reason_for_entitlement not in  ("غير مدرج", "غير مدرج للتكرار")
                    and `tabCivilian Clothing For Officers`.print = "تم الطباعه"
                    and `tabCivilian Clothing For Officers`.entities = "{entity}"

                        {conditions}
                    """.format(conditions=conditions, entity=entity.entities), filters, as_dict=1)
                
                count3 = frappe.db.sql("""
                    select
                        COUNT(name) as count
                    from
                        `tabCivilian Clothing For Officers` 
                    where
                        `tabCivilian Clothing For Officers`.reason_for_entitlement not in  ("غير مدرج", "غير مدرج للتكرار")
                        and `tabCivilian Clothing For Officers`.print = "لم يتم الطباعه"
                        and `tabCivilian Clothing For Officers`.entities = "{entity}"

                        {conditions}
                    """.format(conditions=conditions, entity=entity.entities), filters, as_dict=1)
                data = {
                    'entity': entity.entities,
                    'valid_exchangers': count1[0].count,
                    'exchanged_amount': count2[0].count,
                    'not_exchanged_amount': count3[0].count,
                    
                }
                result.append(data)
            
    else:

        entities = frappe.db.sql("""
            SELECT 
            entities as entities
        FROM `tabCivilian Clothing For People` 
        where 1=1
        {conditions1}

        GROUP BY entities
            """.format(conditions1=conditions1),filters,as_dict=1)
        if entities:
            for entity in entities:
                count1 = frappe.db.sql("""
                    select
                        COUNT(name) as count
                    from
                        `tabCivilian Clothing For People` 
                    where

                    `tabCivilian Clothing For People`.reason_for_entitlement not in  ("غير مدرج", "غير مدرج للتكرار")
                    and 
                        `tabCivilian Clothing For People`.entities = "{entity}"
                        {conditions}
                    """.format(conditions=conditions, entity=entity.entities), filters, as_dict=1)
                
                count2 = frappe.db.sql("""
                    select
                        COUNT(name) as count
                    from
                        `tabCivilian Clothing For People` 
                    where
                    `tabCivilian Clothing For People`.reason_for_entitlement not in  ("غير مدرج", "غير مدرج للتكرار")
                    and `tabCivilian Clothing For People`.print = "تم الطباعه"
                    and `tabCivilian Clothing For People`.entities = "{entity}"

                        {conditions}
                    """.format(conditions=conditions, entity=entity.entities), filters, as_dict=1)
                
                count3 = frappe.db.sql("""
                    select
                        COUNT(name) as count
                    from
                        `tabCivilian Clothing For People` 
                    where
                            `tabCivilian Clothing For People`.reason_for_entitlement not in  ("غير مدرج", "غير مدرج للتكرار")
                        and `tabCivilian Clothing For People`.print = "لم يتم الطباعه"
                        and `tabCivilian Clothing For People`.entities = "{entity}"

                        {conditions}
                    """.format(conditions=conditions, entity=entity.entities), filters, as_dict=1)
                data = {
                    'entity': entity.entities,
                    'valid_exchangers': str(count1[0].count),
                    'exchanged_amount': str(count2[0].count),
                    'not_exchanged_amount': str(count3[0].count),
                    
                }
                result.append(data)
    try:

        result[0]["cur_user"] = frappe.db.get_value("User", frappe.session.user, ["full_name"])
    except:
        pass
    return result