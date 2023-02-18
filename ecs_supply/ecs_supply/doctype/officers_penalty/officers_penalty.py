# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class OfficersPenalty(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.officers)
		log = employee.append("officers_penalty_logs", {})
		log.penalty_type = self.penalty_type
		log.reason = self.reason
		log.penalty_date = self.penalty_date
		log.save()
