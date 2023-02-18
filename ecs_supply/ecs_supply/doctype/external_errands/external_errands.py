# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ExternalErrands(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.recruit)
		log = employee.append("external_errands_logs", {})
		log.errand_date = self.errand_date
		log.notes = self.notes
		log.save()
