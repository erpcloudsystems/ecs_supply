# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CiviliansTrainingEvent(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.civilians)
		log = employee.append("civilians_training_event_logs", {})
		log.course_type = self.course_type
		log.location = self.location
		log.start_date = self.start_date
		log.end_date = self.end_date
		log.save()