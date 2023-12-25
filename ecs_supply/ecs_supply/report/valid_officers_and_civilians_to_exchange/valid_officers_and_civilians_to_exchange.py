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
            "label": _("الأقدمية"),
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
            "label": _("الجهة"),
            "fieldname": "entities",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("الاسم"),
            "fieldname": "officer_name",
            "fieldtype": "Integer",
            "width": 150
        },
        {
            "label": _("استحقاق الصرف"),
            "fieldname": "reason_for_entitlement",
            "fieldtype": "Integer",
            "width": 150
        },
        {
            "label": _("العمل المسند"),
            "fieldname": "assigned_work",
            "fieldtype": "Data",
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
    # if filters.get("from_date"):
    #     conditions += " and print_date >= %(from_date)s"
    # if filters.get("to_date"):
    #     conditions += " and print_date <= %(to_date)s"

    result = []
    if filters.get("title") == "ضباط":
        data = frappe.db.sql("""
                    select *
                    from
                        `tabCivilian Clothing For Officers` 
                    where
                        `tabCivilian Clothing For Officers`.reason_for_entitlement not in  ("غير مدرج", "غير مدرج للتكرار")
                    and `tabCivilian Clothing For Officers`.print = "لم يتم الطباعه"
                        {conditions}
                    order by num_order 
                    """.format(conditions=conditions, entities=filters.get("entities")), filters, as_dict=1)
        for row in data:
            data_row = {
                'id_number': row.id_number2,
                'rank': row.rank,
                'entities': row.entities,
                'officer_name': row.officer_name,
                'reason_for_entitlement': row.reason_for_entitlement,
                'assigned_work': row.assigned_work,
            }
            result.append(data_row)
            
    else:

        data = frappe.db.sql("""
                    select *
                    from
                        `tabCivilian Clothing For People` 
                    where
                        `tabCivilian Clothing For People`.reason_for_entitlement not in  ("غير مدرج", "غير مدرج للتكرار")
                    and `tabCivilian Clothing For People`.print = "لم يتم الطباعه"

                        {conditions}
                    """.format(conditions=conditions, entity=filters.get("entities")), filters, as_dict=1)
        for row in data:
            data_row = {
                'id_number': row.id_number,
                'rank': row.rank,
                'entities': row.entities,
                'officer_name': row.officer_name,
                'reason_for_entitlement': row.reason_for_entitlement,
                'assigned_work': row.assigned_work,
            }
            result.append(data_row)
    try:

        result[0]["cur_user"] = frappe.db.get_value("User", frappe.session.user, ["full_name"])
    except:
        pass
    return result