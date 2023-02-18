# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PolicemenPromotion(Document):
	def on_submit(self):
		frappe.db.set_value('Employee', self.policemen, 'policemen_rank', self.new_policemen_rank)
		employee = frappe.get_doc("Employee", self.policemen)
		log = employee.append("policemen_promotion_logs", {})
		log.current_policemen_rank = self.current_policemen_rank
		log.new_policemen_rank = self.new_policemen_rank
		log.notes = self.notes
		log.promotion_date = self.promotion_date
		log.save()
