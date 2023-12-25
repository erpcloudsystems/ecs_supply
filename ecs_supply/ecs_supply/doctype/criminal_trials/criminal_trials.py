# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CriminalTrials(Document):
	def validate(self):
		self.employee_name = frappe.db.get_value("Envestigation Employee",self.employee,"first_name")
		