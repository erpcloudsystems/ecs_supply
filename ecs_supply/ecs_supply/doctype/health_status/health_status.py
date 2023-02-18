# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HealthStatus(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.officers)
		log = employee.append("health_status_logs", {})
		log.description = self.description
		log.from_date = self.from_date
		log.to_date = self.to_date
		log.save()