# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import in_words

class FinanceForm(Document):
	@frappe.whitelist()
	def validate(self):
		total1 = 0
		total2 = 0
		total3 = 0
		total4 = 0
		total5 = 0
		total6 = 0
		total7 = 0
		if self.form_type=="فاتورة":
			for d in self.form_invoices:
				total1 += d.total
			self.total_invoices = total1
		total4 = self.total_invoices

		if self.incloud_imprints:
			for x in self.imprints:
				total2 += x.imprints_amount
		self.total_imprints = total2
		total5 = total2
		if self.incloud_taxes:
			for z in self.taxes:
				z.tax_amount = (z.tax_percent * self.total_invoices) / 100
				total3 += z.tax_amount
		self.total_taxes = total3
		total6 = total3 
		total7 = total4 - ( total5 + total6)
		self.total = total7
		self.in_word = in_words(total7)
