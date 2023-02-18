# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class NeedsList(Document):
	@frappe.whitelist()
	def validate(doc, method=None):
		items = frappe.db.sql(""" select a.item,
										a.item_name,
										a.uom,
										sum(a.qty) as qty,
										b.fiscal_year
										
								from `tabClothing Needs Items` a join `tabClothing Needs` b
								on a.parent = b.name
								where b.fiscal_year = '{fiscal_year}' and b.docstatus =1
								GROUP BY a.item,a.uom
							""".format(fiscal_year=doc.fiscal_year), as_dict=1)
		doc.clothing_needs_items = []
		for x in items:
			table = doc.append("clothing_needs_items", {})
			table.item = x.item
			table.item_name = x.item_name
			table.uom = x.uom
			table.qty = x.qty
			
			

	