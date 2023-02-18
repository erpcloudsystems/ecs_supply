# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ActingPoliceOfficers(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.policemen)
		log = employee.append("acting_police_officers_logs", {})
		log.notes = self.notes
		log.proxy_decision_number = self.proxy_decision_number
		log.proxy_decision_date = self.proxy_decision_date
		log.save()
