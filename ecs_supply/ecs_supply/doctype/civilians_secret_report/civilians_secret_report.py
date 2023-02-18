# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CiviliansSecretReport(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.civilians)
		log = employee.append("civilians_secret_report_logs", {})
		log.estimation = self.estimation
		log.civilians_grade = self.civilians_grade
		log.report_date = self.report_date
		log.save()
