# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate ,getdate

class PolicemenPunishment(Document):
    def onload(self):
        pass


    def on_submit(self):
        employee = frappe.get_doc("Envestigation Employee", self.policeman_name)
        self.policemen_rank = employee.policemen_rank
        self.police_number = employee.employee_number
        employee.save()
        # log = employee.append("policemen_punishment", {})
        # employee.first_name =self.employee_name
        # employee.punishment_type = self.punishment_type
        # employee.notes = self.notes
        # employee.punishment_date = self.punishment_date
        # employee.save()
