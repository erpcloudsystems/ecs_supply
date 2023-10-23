import frappe
import json

@frappe.whitelist()
def check_for_duplicates_insystem(**kwargs):
    return kwargs["data"]

@frappe.whitelist()
def send_officers_data(**kwargs):
    response = []
    if kwargs["data"]:
        for row in json.loads(kwargs["data"]) :
            if not frappe.db.exists("Civilian Clothing For Officers", {"id_number": row["id_number"], "fiscal_year":row["fiscal_year"]}):
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