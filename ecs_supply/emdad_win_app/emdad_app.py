import frappe
import json
from frappe.model.naming import getseries
from frappe.utils import now

@frappe.whitelist()
def check_for_duplicates_insystem(**kwargs):
    return kwargs["data"]

@frappe.whitelist()
def send_officers_data(**kwargs):
    now_datetime = now()
    response = []
    if kwargs["data"]:
        for row in json.loads(kwargs["data"]):
            if not frappe.db.exists("Officer Rank", {"name": row["rank"]}):
                frappe.db.sql(f"""
                            Insert INTO `tabOfficer Rank` (name, officer_rank, code , creation, modified, owner)  
                               VALUES  ('{row["rank"]}','{row["rank"]}' , '{row["rank_code"] or None }', '{now_datetime}', '{now_datetime}', 'Administrator')
                                """)
                frappe.db.commit()
                
            if not frappe.db.exists("Clothing Entity", {"name": row["entities"]}):
                frappe.db.sql(f"""
                            Insert INTO `tabClothing Entity` (name, entity_name, code , creation, modified, owner) 
                            Values ('{row["entities"]}','{row["entities"]}' , '{row["entities_code"] or None }', '{now_datetime}', '{now_datetime}', 'Administrator')
                                """)
                frappe.db.commit()
            if not frappe.db.exists("Civilian Clothing For Officers", {"id_number": row["id_number"], "fiscal_year":row["fiscal_year"]}):

                prefix = 'O-'
                name = getseries(prefix, 5)
                
                frappe.db.sql(f"""
                            Insert INTO `tabCivilian Clothing For Officers` (name, id_number, id_number2, num_order,job, officer_name, rank, rank_code,
                              entities, entities_code, assigned_work, fiscal_year, reason_for_entitlement, creation, modified, owner) 
                            Values ('O-{name}','{row["id_number"]}', '{row["id_number2"]}', '{int(row["num_order"])}', '{row["job"]}', 
                            '{row["officer_name"]}', '{row["rank"]}', '{row["rank_code"]}',
                             '{row["entities"]}' , '{row["entities_code"]}', '{row["assigned_work"]}',
                             '{row["fiscal_year"]}', '{row["reason_for_entitlement"]}', '{now_datetime}', '{now_datetime}', 'Administrator')
                                """)
                frappe.db.commit()
                # doc = frappe.get_doc(row)
                # doc.insert(
                #     ignore_permissions=True, # ignore write permissions during insert
                #     ignore_links=True, # ignore Link validation in the document
                #     ignore_mandatory=True # insert even if mandatory fields are not set
                # )
            else:
                response.append(row)
        return response
            
@frappe.whitelist()
def send_people_data(**kwargs):
    response = []
    if kwargs["data"]:
        for row in json.loads(kwargs["data"]):
            duplicate_people = frappe.db.sql(f"""
                                    SELECT name 
                                    From `tabCivilian Clothing For People`
                                    WHERE id_number = "{str(row["id_number"])}"
                                    and fiscal_year = "{row["fiscal_year"]}"
                    """, as_dict=1)
            if not duplicate_people:
                doc = frappe.get_doc(row)
                doc.insert(
                    ignore_permissions=True, # ignore write permissions during insert
                    ignore_links=True, # ignore Link validation in the document
                    ignore_mandatory=True # insert even if mandatory fields are not set
                )
            else:
                response.append(row)
        return response
            

@frappe.whitelist()
def get_default_fiscalyear():
    return frappe.get_doc('System Defaults').default_fiscal_year