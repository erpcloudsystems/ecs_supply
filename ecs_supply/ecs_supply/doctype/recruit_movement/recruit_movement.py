# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RecruitMovement(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.recruit)
		log = employee.append("recruit_movement_logs", {})
		log.movement_type = self.movement_type
		log.notes = self.notes
		log.movement_date = self.movement_date
		log.save()
