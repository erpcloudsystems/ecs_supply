# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TransfersforOfficers(Document):
	def on_submit(self):
		frappe.db.set_value('Employee', self.officers, 'sup_department', self.new_sub_department)
		frappe.db.set_value('Employee', self.officers, 'main_department', self.new_main_department)
		employee = frappe.get_doc("Employee", self.officers)
		log = employee.append("transfers_for_officers_logs", {})
		log.main_department = self.main_department
		log.new_main_department = self.new_main_department
		log.sub_department = self.sub_department
		log.new_sub_department = self.new_sub_department
		log.transfer_reason = self.transfer_reason
		log.transfer_date = self.transfer_date
		log.save()
