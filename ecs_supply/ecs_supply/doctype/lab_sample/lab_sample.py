# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LabSample(Document):
	@frappe.whitelist()
	def validate(doc, method=None):
		pass

	@frappe.whitelist()
	def on_update_after_submit(doc, method=None):
		pass
	
	@frappe.whitelist()
	def after_insert(doc, method=None):
		pass