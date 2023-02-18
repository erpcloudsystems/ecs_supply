# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PolicemenPenalty(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.policemen)
		log = employee.append("policemen_penalty_logs", {})
		log.penalty_type = self.penalty_type
		log.reason = self.reason
		log.penalty_date = self.penalty_date
		log.save()
