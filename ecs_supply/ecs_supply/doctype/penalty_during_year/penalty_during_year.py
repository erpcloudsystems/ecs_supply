# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PenaltyDuringYear(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.policemen)
		log = employee.append("penalty_during_year_logs", {})
		# log.absent_days_during_year = self.absent_days_during_year
		# log.violation_during_year = self.violation_during_year
		# log.delays_during_year = self.delays_during_year
		# log.penalty_during_year = self.penalty_during_year
		log.erase_penalty = self.erase_penalty
		log.year = self.year
		log.save()