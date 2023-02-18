# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PolicemenAttendanceRequest(Document):
	def on_submit(doc):
		employee = frappe.get_doc("Employee", doc.policemen)
		log = employee.append("policemen_attendance_request_logs", {})
		log.type = doc.type
		log.country = doc.country
		log.from_date = doc.from_date
		log.to_date = doc.to_date
		log.notes = doc.notes
		log.save()