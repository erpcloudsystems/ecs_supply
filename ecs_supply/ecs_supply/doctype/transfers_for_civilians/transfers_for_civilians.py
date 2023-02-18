# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TransfersforCivilians(Document):
	def on_submit(self):
		frappe.db.set_value('Employee', self.civilians, 'main_department', self.new_main_department)
		frappe.db.set_value('Employee', self.civilians, 'department_new', self.new_department_new)
		frappe.db.set_value('Employee', self.civilians, 'department_sec', self.new_department_sec)
		frappe.db.set_value('Employee', self.civilians, 'department', self.new_department)
		frappe.db.set_value('Employee', self.civilians, 'designation_feiled', self.new_designation_filed)
		employee = frappe.get_doc("Employee", self.civilians)
		log = employee.append("transfers_for_civilians_logs", {})
		log.main_department = self.main_department
		log.new_main_department = self.new_main_department
		log.current_department_new = self.current_department_new
		log.new_department_new = self.new_department_new
		log.current_department_sec = self.current_department_sec
		log.new_department_sec = self.new_department_sec
		log.current_department = self.current_department
		log.new_department = self.new_department
		log.current_designation_filed = self.current_designation_filed
		log.new_designation_filed = self.new_designation_filed
		log.transfer_reason = self.transfer_reason
		log.transfer_date = self.transfer_date
		log.save()
