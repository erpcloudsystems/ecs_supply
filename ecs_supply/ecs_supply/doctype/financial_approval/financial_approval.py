# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import in_words

class FinancialApproval(Document):
	@frappe.whitelist()
	def validate(self):
		total = 0
		self.total_table = 0
		for d in self.buying_order_items:
			d.amount = d.rate * d.quantity
			total +=d.amount
		self.total_table = total
		self.in_word = in_words(self.total_table)
	@frappe.whitelist()
	def on_submit(self):
		frappe.db.sql(""" update `tabBuying Order` set financial_approval_status = '{status}' where `tabBuying Order`.name = '{name}'  """.format(status= self.workflow_state, name=self.buying_order))
		frappe.db.sql(""" update `tabBuying Order` set workflow_state = "انتظار مذكرة الطرح" where `tabBuying Order`.name = '{name}'  """.format( name=self.buying_order))
		
	@frappe.whitelist()
	def on_cancel(self):
		frappe.db.sql(""" update `tabBuying Order` set financial_approval = "" where `tabBuying Order`.name = '{name}'  """.format( name=self.buying_order))
		frappe.db.sql(""" update `tabBuying Order` set workflow_state = "انتظار الارتباط" where `tabBuying Order`.name = '{name}'  """.format( name=self.buying_order))
		frappe.db.sql(""" update `tabBuying Order` set financial_approval_status = "" where `tabBuying Order`.name = '{name}'  """.format( name=self.buying_order))