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
                            Insert INTO `tabOfficer Rank` (name, officer_rank, code , creation, modified)  
                               VALUES  ('{row["rank"]}','{row["rank"]}' , '{row["rank_code"] or None }', '{now_datetime}', '{now_datetime}')
                                """)
                frappe.db.commit()
                
            if not frappe.db.exists("Entities", {"name": row["entities"]}):
                frappe.db.sql(f"""
                            Insert INTO `tabEntities` (name, entity_name, code , creation, modified) 
                            Values ('{row["entities"]}','{row["entities"]}' , '{row["entities_code"] or None }', '{now_datetime}', '{now_datetime}')
                                """)
                frappe.db.commit()
            if not frappe.db.exists("Civilian Clothing For Officers", {"id_number": row["id_number"], "fiscal_year":row["fiscal_year"]}):

                prefix = 'O-'
                name = getseries(prefix, 5)
                print(name)
                frappe.db.sql(f"""
                            Insert INTO `tabCivilian Clothing For Officers` (name, id_number, officer_name, rank, rank_code,
                              entities, entities_code, assigned_work, fiscal_year, reason_for_entitlement, creation, modified) 
                            Values ('O-{name}','{row["id_number"]}', '{row["officer_name"]}', '{row["rank"]}', '{row["rank_code"]}',
                             '{row["entities"]}' , '{row["entities_code"]}', '{row["assigned_work"]}',
                             '{row["fiscal_year"]}', '{row["reason_for_entitlement"]}', '{now_datetime}', '{now_datetime}')
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
    now_datetime = now()
    response = []
    if kwargs["data"]:
        for row in json.loads(kwargs["data"]):
            duplicate_people = frappe.db.sql(f"""
                                    SELECT name 
                                    From `tabCivilian Clothing For People`
                                    WHERE id_number = "{str(row["id_number"])}"
                                    and fiscal_year = "{row["fiscal_year"]}"
                    """, as_dict=1)
            if not frappe.db.exists("Job Code", {"name": row["assigned_work"]}):
                frappe.db.sql(f"""
                            Insert INTO `tabJob Code` (name, job, code , creation, modified)  
                               VALUES  ('{row["assigned_work"]}','{row["assigned_work"]}' , '{row["assigned_work"] or None }', '{now_datetime}', '{now_datetime}')
                                """)
                frappe.db.commit()
            if not frappe.db.exists("Reason for Entitlement", {"name": row["reason_for_entitlement"]}):
                frappe.db.sql(f"""
                            Insert INTO `tabReason for Entitlement` (name, reason, creation, modified)  
                               VALUES  ('{row["reason_for_entitlement"]}','{row["reason_for_entitlement"]}' , '{now_datetime}', '{now_datetime}')
                                """)
                frappe.db.commit()
            if not frappe.db.exists("Policemen Rank", {"name": row["rank"]}):
                frappe.db.sql(f"""
                            Insert INTO `tabPolicemen Rank` (name, policemen_rank , creation, modified)  
                               VALUES  ('{row["rank"]}','{row["rank"]}' , '{now_datetime}', '{now_datetime}')
                                """)
                frappe.db.commit()
                
            if not frappe.db.exists("Clothing Entity", {"name": row["entities"]}):
                frappe.db.sql(f"""
                            Insert INTO `tabClothing Entity` (name, entity_name , creation, modified) 
                            Values ('{row["entities"]}','{row["entities"]}' ,  '{now_datetime}', '{now_datetime}')
                                """)
                frappe.db.commit()
            CE_name = frappe.db.get_value("Clothing Entity",{"code":row["entities"]},"name")

            if not frappe.db.exists("Civilian Clothing For People", {"id_number": row["id_number"], "entities":CE_name, "people_name": row["people_name"],"fiscal_year":row["fiscal_year"]}):
                prefix = 'C-'
                name = getseries(prefix, 5)
                print(name)
                frappe.db.sql(f"""
                            Insert INTO `tabCivilian Clothing For People` (name, id_number, people_name, rank,
                              entities, assigned_work, fiscal_year, reason_for_entitlement,
                              reason_for_entitlement_lastyear, non_reason_for_entitlement_lastyear, creation, modified) 
                            Values ('O-{name}','{row["id_number"]}', '{row["people_name"]}', '{row["rank"]}',
                             '{CE_name}' , '{row["assigned_work"]}',
                             '{row["fiscal_year"]}', '{row["reason_for_entitlement"]}',
                              '{row["reason_for_entitlement_lastyear"]}','{row["non_reason_for_entitlement_lastyear"]}',
                              '{now_datetime}', '{now_datetime}')
                                """)
                frappe.db.commit()
            else:
                response.append(row)
        return response
            

@frappe.whitelist()
def get_default_fiscalyear():
    return frappe.get_doc('System Defaults').default_fiscal_year