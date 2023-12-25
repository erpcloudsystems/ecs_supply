# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Hesitantcompanies(Document):
	def before_validate(self):
		if self.disabled == 1:
			self.enabled = 0
		else:
			self.enabled = 1
