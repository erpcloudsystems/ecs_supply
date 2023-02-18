# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SecretNotes(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.policemen)
		log = employee.append("secret_notes_logs", {})
		log.position_decision = self.position_decision
		log.position_date = self.position_date
		log.reason = self.reason
		log.lifting_decision = self.lifting_decision
		log.lifting_date = self.lifting_date
		log.save()
