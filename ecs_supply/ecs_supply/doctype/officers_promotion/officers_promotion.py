# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class OfficersPromotion(Document):
	def on_submit(self):
		frappe.db.set_value('Employee', self.officers, 'rank', self.new_rank)
		employee = frappe.get_doc("Employee", self.officers)
		log = employee.append("officers_promotion_logs", {})
		log.current_rank = self.current_rank
		log.new_rank = self.new_rank
		log.promotion_date = self.promotion_date
		log.save()
