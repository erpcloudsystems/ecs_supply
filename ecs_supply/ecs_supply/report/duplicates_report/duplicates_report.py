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
                    select name as name, entities as entities, officer_name as personal_name, reason_for_entitlement as reason_for_entitlement,
                id_number as id_number, rank as rank, "ضباط" as type, print_date as print_date, fiscal_year as fiscal_year
                from
                    `tabCivilian Clothing For Officers`
                where  fiscal_year = "{fiscal_year}"
               
                    ) 
            union
                    (
                    select name as name, entities as entities, people_name as personal_name, reason_for_entitlement as reason_for_entitlement,
                id_number as id_number, rank as rank, "افراد" as type, print_date as print_date, fiscal_year as fiscal_year
                from
                    `tabCivilian Clothing For People` 
               where  fiscal_year = "{fiscal_year}"
                    ) 
                     
                    ORDER BY {filter_value}
                """.format(conditions=conditions, entities=filters.get("entities"),
                            filter_value=filters.get("filter_value"),
                            fiscal_year=filters.get("fiscal_year")), filters, as_dict=1)
    ids = []
    names = []
    if filters.get("filter_value") == "personal_name":
        for row in data:
            names.append(row.personal_name)
            ids.append(row.name)
        for idx in range(len(names)-1, -1, -1):
            if names.count(names[idx]) == 1:
                del names[idx]
                del ids[idx]
    else:
        for row in data:
            names.append(row.id_number)
            ids.append(row.name)
        for idx in range(len(names)-1, -1, -1):
            if names.count(names[idx]) == 1:
                del names[idx]
                del ids[idx]
    ids_conditions = " WHERE name in ('') "
    if len(ids) == 1:
        ids_conditions = " WHERE name in ({ids}) ".format(ids=ids[0])
    elif len(ids) > 1:
        ids_conditions = " WHERE name in {ids}  ".format(ids=tuple(ids))

    get_duplicated = frappe.db.sql("""
              (
                    select name as name, entities as entities, officer_name as personal_name, reason_for_entitlement as reason_for_entitlement,
                id_number as id_number, rank as rank, "ضباط" as type, print_date as print_date
                from
                    `tabCivilian Clothing For Officers`
               {ids_conditions}
                    ) 
            union
                    (
                    select name as name, entities as entities, people_name as personal_name, reason_for_entitlement as reason_for_entitlement,
                id_number as id_number, rank as rank, "افراد" as type, print_date as print_date
                from
                    `tabCivilian Clothing For People` 
                    {ids_conditions}
                    )
                
                    ORDER BY {filter_value} 

                """.format(conditions=conditions, entities=filters.get("entities"),
                            filter_value=filters.get("filter_value"),
                            ids_conditions=ids_conditions),filters, as_dict=1)
    if filters.get("entities"):
        accepted_names = []
        for row in get_duplicated:
            if row.entities == filters.get("entities"):
                accepted_names.append(row.personal_name)
        for idx in range(len(get_duplicated)-1, -1, -1):
            if get_duplicated[idx].personal_name not in accepted_names:
                del get_duplicated[idx]

    for row in get_duplicated:
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