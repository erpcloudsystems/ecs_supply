# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RecruitVacation(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.recruit)
		log = employee.append("recruit_vacation_logs", {})
		log.start_date = self.start_date
		log.end_date = self.end_date
		log.notes = self.notes
		log.save()
