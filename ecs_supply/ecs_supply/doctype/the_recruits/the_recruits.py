# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class TheRecruits(Document):
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
    def before_validate(self):
        if self.disabled == 1:
            self.enabled = 0
            frappe.db.set_value("Criminal And Political Disclosure",{"the_recruits":self.name},"enabled",0)
            frappe.db.set_value("Military Trials",{"the_recruits":self.name},"enabled",0)
            frappe.db.set_value("Criminal Trials Of Recruits",{"the_recruits":self.name},"enabled",0)
            frappe.db.set_value("Examination_for_recruits",{"recruit_name":self.name},"enabled",0)
        else:
            self.enabled = 1
            frappe.db.set_value("Criminal And Political Disclosure",{"the_recruits":self.name},"enabled",1)
            frappe.db.set_value("Military Trials",{"the_recruits":self.name},"enabled",1)
            frappe.db.set_value("Criminal Trials Of Recruits",{"the_recruits":self.name},"enabled",1)
            frappe.db.set_value("Examination_for_recruits",{"recruit_name":self.name},"enabled",1)
        frappe.db.commit()

    @frappe.whitelist()
    def on_trash(self):
        indexing_of_employees(self.name)

def indexing_of_employees(selfname):
    idx = None
    data = frappe.db.sql("""
    select EE.name
    FROM
        `tabThe Recruits` EE
    where
        EE.enabled = 1
    ORDER BY
        EE.date_of_conscription ASC, EE.first_name;
    """,as_dict=1)
    for index, item in enumerate(data, start=1):
        if item.name == selfname:
            idx = index
        frappe.db.set_value("The Recruits",item.name,"custom_file_number4",index)
    frappe.db.commit()
    if idx:
        return idx
    else:
        return 0
def check_duplicate_names(self):
        if frappe.db.exists(self.doctype,{"first_name":self.first_name}):
            frappe.throw("أسم المجند مكرر")  