# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PolicemenSecretReport(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.policemen)
		log = employee.append("policemen_secret_report_logs", {})
		log.estimation = self.estimation
		log.policemen_degree = self.policemen_degree
		log.report_date = self.report_date
		log.save()

