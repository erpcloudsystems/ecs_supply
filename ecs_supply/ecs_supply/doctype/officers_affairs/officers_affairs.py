# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class OfficersAffairs(Document):
    @frappe.whitelist()
    def after_insert(self):
        self.validate_enabled()
        self.validate_number_order()
        idx = indexing_of_employees(self.name)
        self.custom_file_number4 = idx
    @frappe.whitelist()
    def validate(self):
        self.validate_enabled()
        self.validate_number_order()
        idx = indexing_of_employees(self.name)
        self.custom_file_number4 = idx
    @frappe.whitelist()
    def before_validate(self):
        self.validate_number_order()

    @frappe.whitelist()
    def on_trash(self):
        indexing_of_employees(self.name)

    def validate_enabled(self):
        if self.disabled == 1:
            self.enabled = 0
            frappe.db.set_value("Criminal Detection Of Officers",{"the_one_who_is_looking_for":self.name},"enabled",0)
            frappe.db.set_value("Secret Notes Officers",{"officers_affairs":self.name},"enabled",0)
            frappe.db.set_value("Disciplinary Councils For Officers",{"officers_affairs":self.name},"enabled",0)
            frappe.db.set_value("Criminal Trials Of Officers",{"officers_affairs":self.name},"enabled",0)
            frappe.db.set_value("Examination_for_officers",{"officers_name":self.name},"enabled",0)
        else:
            self.enabled = 1
            frappe.db.set_value("Criminal Detection Of Officers",{"the_one_who_is_looking_for":self.name},"enabled",1)
            frappe.db.set_value("Secret Notes Officers",{"officers_affairs":self.name},"enabled",1)
            frappe.db.set_value("Disciplinary Councils For Officers",{"officers_affairs":self.name},"enabled",1)
            frappe.db.set_value("Criminal Trials Of Officers",{"officers_affairs":self.name},"enabled",1)
            frappe.db.set_value("Examination_for_officers",{"officers_name":self.name},"enabled",1)
        frappe.db.commit()
    
    def validate_number_order(self):
        self.num_order = "19" + str(self.graduated_year) +("0" * (5-len(str(self.graduation_ranking)))) + str(self.graduation_ranking) if len(str(self.graduated_year)) <= 2 else str(self.graduated_year) +("0" * (5-len(str(self.graduation_ranking)))) + str(self.graduation_ranking) 
        if self.special_no:
            self.the_seniority_number = f"{self.special_no}/{self.graduated_year}/{self.graduation_ranking}"
        else:
            self.the_seniority_number = f"{self.graduated_year}/{self.graduation_ranking}"      
            
    def check_duplicate_names(self):
        if frappe.db.exists(self.doctype,{"the_seniority_number":self.the_seniority_number}):
            frappe.throw("رقم الأقدمية مكرر")
      
        if frappe.db.exists(self.doctype,{"first_name":self.first_name}):
            frappe.throw("أسم الضابط مكرر")  


def indexing_of_employees(selfname):
    idx = None
    data = frappe.db.sql("""
    select EE.name
    from
        `tabOfficers Affairs` EE
    where
        EE.enabled = 1
    ORDER BY num_order asc
    """,as_dict=1)
    for index, item in enumerate(data, start=1):
        if item.name == selfname:
            idx = index

        frappe.db.set_value("Officers Affairs",item.name,"custom_file_number4",index)
    frappe.db.commit()
    if idx:
        return idx
