# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime



class DailyVisit(Document):
	@frappe.whitelist()
	def before_insert(doc, method=None):
		pass
