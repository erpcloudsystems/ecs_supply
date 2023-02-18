# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class OfficersBonusAndDecorations(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.officers)
		log = employee.append("officers_bonus_and_decorations_logs", {})
		log.bonus_type = self.bonus_type
		log.reason = self.reason
		log.date = self.date
		log.save()
