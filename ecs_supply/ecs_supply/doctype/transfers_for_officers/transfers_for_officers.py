# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TransfersforOfficers(Document):
	def on_submit(self):
		frappe.db.set_value('Officers Affairs', self.employee_name, 'sup_department', self.new_sub_department)
		frappe.db.set_value('Officers Affairs', self.employee_name, 'main_department23', self.new_main_department)
		employee = frappe.get_doc("Officers Affairs", self.employee_name)
		employee.main_department = self.main_department
		employee.new_main_department = self.new_main_department
		employee.sub_department = self.sub_department
		employee.new_sub_department = self.new_sub_department
		employee.transfer_reason = self.transfer_reason
		employee.transfer_date = self.transfer_date
		employee.save()
