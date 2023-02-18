# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RecordingWorkAssignedToOfficer(Document):
    def on_submit(self):
         frappe.db.set_value('Employee', self.officers, 'work_assigned_to_officers', self.work_assigned)