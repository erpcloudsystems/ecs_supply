# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CriminalAndPoliticalInvestigation(Document):
	
	@frappe.whitelist()
	def history_investigation(self):
		return frappe.db.sql(f"""
			SELECT * 
			FROM `tabCriminal And Political Investigation` creminal
			where recruit = '{self.recruit}'
		""",as_dict=True)
