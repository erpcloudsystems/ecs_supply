# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Sample(Document):
	@frappe.whitelist()
	def before_insert(doc, method=None):
		max_code = 0
		last_code = frappe.db.sql(""" select code as max from `tabSample` """, as_dict=1)
		for x in last_code:
			if max_code < int(x.max):
				max_code = int(x.max)

		doc.code = max_code + 1
