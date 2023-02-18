# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PolicemenPunishment(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.policemen)
		log = employee.append("policemen_punishment_logs", {})
		log.punishment_type = self.punishment_type
		log.notes = self.notes
		log.punishment_date = self.punishment_date
		log.save()
