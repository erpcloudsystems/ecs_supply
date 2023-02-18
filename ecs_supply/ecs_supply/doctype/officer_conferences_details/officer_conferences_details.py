# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class OfficerConferencesDetails(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.officers)
		log = employee.append("officer_conferences_details_logs", {})
		log.conference_name = self.conference_name
		log.conference_side = self.conference_side
		log.from_date = self.from_date
		log.to_date = self.to_date
		log.save()
