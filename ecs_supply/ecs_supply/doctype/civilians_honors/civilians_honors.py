# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CiviliansHonors(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.civilians)
		log = employee.append("civilians_honors_logs", {})
		log.type_of_honor = self.type_of_honor
		log.notes = self.notes
		log.date = self.date
		log.save()
