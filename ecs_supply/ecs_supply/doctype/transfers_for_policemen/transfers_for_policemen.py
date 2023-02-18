# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TransfersforPolicemen(Document):
	def on_submit(self):
		frappe.db.set_value('Employee', self.policemen, 'main_department', self.new_main_department)
		frappe.db.set_value('Employee', self.policemen, 'sup_department', self.new_sub_department)
		employee = frappe.get_doc("Employee", self.policemen)
		log = employee.append("transfers_for_policemen_logs", {})
		log.current_main_department = self.current_main_department
		log.new_main_department = self.new_main_department
		log.current_sub_department = self.current_sub_department
		log.new_sub_department = self.new_sub_department
		log.transfer_reason = self.transfer_reason
		log.transfer_date = self.transfer_date
		log.save()
