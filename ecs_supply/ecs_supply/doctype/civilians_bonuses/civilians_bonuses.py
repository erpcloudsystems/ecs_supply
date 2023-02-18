# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CiviliansBonuses(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.civilians )
		log = employee.append("civilians_bonuses_logs", {})
		log.bonus_type = self.bonus_type
		log.notes = self.notes
		log.bonus_date = self.bonus_date
		log.save()
