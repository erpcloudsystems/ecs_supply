# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class OfficerBonus(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.officers)
		log = employee.append("officer_bonus_log", {})
		log.bonus_type = self.bonus_type
		log.notes = self.notes
		log.bonus_date = self.bonus_date
		log.save()