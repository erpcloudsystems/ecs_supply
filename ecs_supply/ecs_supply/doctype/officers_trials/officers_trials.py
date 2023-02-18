# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class OfficersTrials(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.officers)
		log = employee.append("officers_trials_logs", {})
		log.trial_type = self.trial_type
		log.trial_reason = self.trial_reason
		log.trial_date = self.trial_date
		log.resumption_date = self.resumption_date
		log.save()
