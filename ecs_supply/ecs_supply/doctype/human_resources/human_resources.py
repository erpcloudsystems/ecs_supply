# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class HumanResources(Document):
    @frappe.whitelist()
    def after_insert(self):
        idx = indexing_of_employees(self.name)
        self.custom_file_number4 = idx
    @frappe.whitelist()
    def validate(self):
        idx = indexing_of_employees(self.name)
        self.custom_file_number4 = idx
    
    def before_insert(self):
        check_duplicate_names(self)
    @frappe.whitelist()
    def before_validate(self):
        if self.disabled == 1:
            self.enabled = 0
            frappe.db.set_value("Criminal And Political Disclosure Of Human Resources",{"the_one_who_is_looking_for":self.name},"enabled",0)
            frappe.db.set_value("examination_of_civilian_employees",{"employee_name":self.name},"enabled",0)
            frappe.db.set_value("Disciplinary and Criminal Trials",{"human_resources":self.name},"enabled",0)
        else:
            self.enabled = 1
            frappe.db.set_value("Criminal And Political Disclosure Of Human Resources",{"the_one_who_is_looking_for":self.name},"enabled",1)
            frappe.db.set_value("examination_of_civilian_employees",{"employee_name":self.name},"enabled",1)
            frappe.db.set_value("Disciplinary and Criminal Trials",{"human_resources":self.name},"enabled",1)
        frappe.db.commit()
    @frappe.whitelist()
    def on_trash(self):
        indexing_of_employees(self.name)

def indexing_of_employees(selfname):
    idx = None
    data = frappe.db.sql("""
    select EE.name
    FROM
        `tabHuman Resources` EE
    where
        EE.enabled = 1
    ORDER BY
        EE.custom_date_of_appointment ASC, EE.first_name;
    """,as_dict=1)
    for index, item in enumerate(data, start=1):
        if item.name == selfname:
            idx = index
        frappe.db.set_value("Human Resources",item.name,"custom_file_number4",index)
    frappe.db.commit()
    if idx:
        return idx
def check_duplicate_names(self):
        if frappe.db.exists(self.doctype,{"first_name":self.first_name}):
            frappe.throw("أسم الموظف مكرر")  