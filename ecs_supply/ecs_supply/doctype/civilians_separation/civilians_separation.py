# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CiviliansSeparation(Document):
	def on_submit(self):
		frappe.db.set_value('Employee', self.civilians, 'status', "Left")
		frappe.db.set_value('Employee', self.civilians, 'relieving_date', self.separation_begins_on)
		frappe.db.set_value('Employee', self.civilians, 'reason_for_leaving', self.reason)