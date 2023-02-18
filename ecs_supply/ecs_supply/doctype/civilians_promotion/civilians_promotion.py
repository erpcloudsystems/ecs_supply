# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CiviliansPromotion(Document):
	def on_submit(self):
		frappe.db.set_value('Employee', self.civilians, 'designation', self.new_designation)
		frappe.db.set_value('Employee', self.civilians, 'civilians_degree', self.new_civilians_degree)
		frappe.db.set_value('Employee', self.civilians, 'sub_degree', self.new_sub_degree)
		employee = frappe.get_doc("Employee", self.civilians)
		log = employee.append("civilians_promotion_logs", {})
		log.current_designation = self.current_designation
		log.new_designation = self.new_designation
		log.current_civilians_degree = self.current_civilians_degree
		log.new_civilians_degree = self.new_civilians_degree
		log.notes = self.notes
		log.promotion_date = self.promotion_date
		log.save()

