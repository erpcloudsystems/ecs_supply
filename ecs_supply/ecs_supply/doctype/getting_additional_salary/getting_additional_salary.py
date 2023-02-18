# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GettingAdditionalSalary(Document):
	def on_submit(self):
		employee = frappe.get_doc("Employee", self.policemen)
		log = employee.append("getting_additional_salary_logs", {})
		log.additional_work_type = self.additional_work_type
		log.additional_salary_value = self.additional_salary_value
		log.notes = self.notes
		log.additional_salary_date = self.additional_salary_date
		log.save()
