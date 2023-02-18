# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class OfficersSecretReport(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.officers)
		log = employee.append("officers_secret_report_logs", {})
		log.estimation = self.estimation
		log.degree = self.degree
		log.report_date = self.report_date
		log.save()