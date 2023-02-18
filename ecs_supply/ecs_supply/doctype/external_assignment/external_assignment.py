# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ExternalAssignment(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.recruit)
		log = employee.append("external_assignment_logs", {})
		log.assignment_date = self.assignment_date
		log.assignment_entities = self.assignment_entities
		log.notes = self.notes
		log.save()
