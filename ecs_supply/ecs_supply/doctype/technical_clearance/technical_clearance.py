# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TechnicalClearance(Document):
	@frappe.whitelist()
	def on_submit(self):
		
		frappe.db.sql(""" update `tabBuying Order` set technical_clearance_status = '{status}' where `tabBuying Order`.name = '{name}'  """.format(status= self.workflow_state, name=self.buying_order))
		frappe.db.sql(""" update `tabBuying Order` set workflow_state = "انتظار الفض المالي" where `tabBuying Order`.name = '{name}'  """.format( name=self.buying_order))
		
  
  
	@frappe.whitelist()
	def on_cancel(self):
		frappe.db.sql(""" update `tabBuying Order` set presentation_note = "" where `tabBuying Order`.name = '{name}'  """.format( name=self.buying_order))
		frappe.db.sql(""" update `tabBuying Order` set workflow_state = "انتظار مذكرة الطرح" where `tabBuying Order`.name = '{name}'  """.format( name=self.buying_order))
		frappe.db.sql(""" update `tabBuying Order` set technical_clearance_status = "" where `tabBuying Order`.name = '{name}'  """.format( name=self.buying_order))
	@frappe.whitelist()
	def after_insert(doc, method=None):
		pass

	@frappe.whitelist()
	def validate(doc, method=None):
		if not doc.table_supplier1:
			is_items = frappe.db.sql(""" select a.item, a.idx, a.item_name, a.description, a.quantity, a.uom, a.rate, a.amount, a.warehouse
																					from `tabBuying Order Items` a join `tabBuying Order` b
																					on a.parent = b.name
																					where b.name = '{name}'
																				""".format(name=doc.buying_order), as_dict=1)
			for c in is_items:
			
				items = doc.append("table_supplier1", {})
				items.idx = c.idx
				items.item_code = c.item
				items.item_name = c.item_name
				items.description = c.description
				items.qty = c.quantity
				items.rate = 0
				items.amount = 0

				items2 = doc.append("table_supplier2", {})
				items2.idx = c.idx
				items2.item_code = c.item
				items2.item_name = c.item_name
				items2.description = c.description
				items2.qty = c.quantity
				items2.rate = 0
				items2.amount = 0

				items3 = doc.append("table_supplier3", {})
				items3.idx = c.idx
				items3.item_code = c.item
				items3.item_name = c.item_name
				items3.description = c.description
				items3.qty = c.quantity
				items3.rate = 0
				items3.amount = 0

				items4 = doc.append("table_supplier4", {})
				items4.idx = c.idx
				items4.item_code = c.item
				items4.item_name = c.item_name
				items4.description = c.description
				items4.qty = c.quantity
				items4.rate = 0
				items4.amount = 0

				items5 = doc.append("table_supplier5", {})
				items5.idx = c.idx
				items5.item_code = c.item
				items5.item_name = c.item_name
				items5.description = c.description
				items5.qty = c.quantity
				items5.rate = 0
				items5.amount = 0

				items6 = doc.append("table_supplier6", {})
				items6.idx = c.idx
				items6.item_code = c.item
				items6.item_name = c.item_name
				items6.description = c.description
				items6.qty = c.quantity
				items6.rate = 0
				items6.amount = 0

				items7 = doc.append("table_supplier7", {})
				items7.idx = c.idx
				items7.item_code = c.item
				items7.item_name = c.item_name
				items7.description = c.description
				items7.qty = c.quantity
				items7.rate = 0
				items7.amount = 0

				items8 = doc.append("table_supplier8", {})
				items8.idx = c.idx
				items8.item_code = c.item
				items8.item_name = c.item_name
				items8.description = c.description
				items8.qty = c.quantity
				items8.rate = 0
				items8.amount = 0

				items9 = doc.append("table_supplier9", {})
				items9.idx = c.idx
				items9.item_code = c.item
				items9.item_name = c.item_name
				items9.description = c.description
				items9.qty = c.quantity
				items9.rate = 0
				items9.amount = 0

				items10 = doc.append("table_supplier10", {})
				items10.idx = c.idx
				items10.item_code = c.item
				items10.item_name = c.item_name
				items10.description = c.description
				items10.qty = c.quantity
				items10.rate = 0
				items10.amount = 0

				items11 = doc.append("table_supplier11", {})
				items11.idx = c.idx
				items11.item_code = c.item
				items11.item_name = c.item_name
				items11.description = c.description
				items11.qty = c.quantity
				items11.rate = 0
				items11.amount = 0

				items12 = doc.append("table_supplier12", {})
				items12.idx = c.idx
				items12.item_code = c.item
				items12.item_name = c.item_name
				items12.description = c.description
				items12.qty = c.quantity
				items12.rate = 0
				items12.amount = 0

				items13 = doc.append("table_supplier13", {})
				items13.idx = c.idx
				items13.item_code = c.item
				items13.item_name = c.item_name
				items13.description = c.description
				items13.qty = c.quantity
				items13.rate = 0
				items13.amount = 0

				items14 = doc.append("table_supplier14", {})
				items14.idx = c.idx
				items14.item_code = c.item
				items14.item_name = c.item_name
				items14.description = c.description
				items14.qty = c.quantity
				items14.rate = 0
				items14.amount = 0

				items15 = doc.append("table_supplier15", {})
				items15.idx = c.idx
				items15.item_code = c.item
				items15.item_name = c.item_name
				items15.description = c.description
				items15.qty = c.quantity
				items15.rate = 0
				items15.amount = 0

		if doc.table_supplier1:
			total =0
			for x in doc.table_supplier1:
				total = x.qty * x.rate
				x.total = total

		if doc.table_supplier2:
			total =0
			for x in doc.table_supplier2:
				total = x.qty * x.rate
				x.total = total

		if doc.table_supplier3:
			total =0
			for x in doc.table_supplier3:
				total = x.qty * x.rate
				x.total = total

		if doc.table_supplier4:
			total =0
			for x in doc.table_supplier4:
				total = x.qty * x.rate
				x.total = total
		if doc.table_supplier5:
			total =0
			for x in doc.table_supplier5:
				total = x.qty * x.rate
				x.total = total

		if doc.table_supplier6:
			total =0
			for x in doc.table_supplier6:
				total = x.qty * x.rate
				x.total = total

		if doc.table_supplier7:
			total =0
			for x in doc.table_supplier7:
				total = x.qty * x.rate
				x.total = total

		if doc.table_supplier8:
			total =0
			for x in doc.table_supplier8:
				total = x.qty * x.rate
				x.total = total

		if doc.table_supplier9:
			total =0
			for x in doc.table_supplier9:
				total = x.qty * x.rate
				x.total = total

		if doc.table_supplier10:
			total =0
			for x in doc.table_supplier10:
				total = x.qty * x.rate
				x.total = total

		if doc.table_supplier11:
			total =0
			for x in doc.table_supplier11:
				total = x.qty * x.rate
				x.total = total
		if doc.table_supplier12:
			total =0
			for x in doc.table_supplier12:
				total = x.qty * x.rate
				x.total = total
		if doc.table_supplier13:
			total =0
			for x in doc.table_supplier13:
				total = x.qty * x.rate
				x.total = total
		if doc.table_supplier14:
			total =0
			for x in doc.table_supplier14:
				total = x.qty * x.rate
				x.total = total
		if doc.table_supplier15:
			total =0
			for x in doc.table_supplier15:
				total = x.qty * x.rate
				x.total = total
		