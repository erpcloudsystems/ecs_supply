# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import datetime
import frappe
from frappe.model.document import Document
from frappe.utils import nowdate
class BonPrinting(Document):
	@frappe.whitelist()
	def get_entity_data(doc, method=None):
		doc.set("bon_printing_civilians", [])
		conditions = ""
		if doc.reason_for_entitlement:
			conditions += " and reason_for_entitlement = '{reason_for_entitlement}' ".format(reason_for_entitlement=doc.reason_for_entitlement)
		if doc.officer_name:
			conditions += " and officer_name LIKE '%{officer_name}%' ".format(officer_name=doc.officer_name)
		if doc.officer_no:
			conditions += " and id_number LIKE '%{officer_no}%' ".format(officer_no=doc.officer_no)
		conditions += " and print = 'لم يتم الطباعه' "


		if doc.title == "ضباط":
			entity_data = frappe.db.sql(
				""" select
					name, id_number2, officer_name, rank, entities, assigned_work, job,
					reason_for_entitlement, print, print_date, fiscal_year
					from `tabCivilian Clothing For Officers` 
					where entities = '{entity}'
					and fiscal_year = '{fiscal_year}'
					and reason_for_entitlement not in ("غير مدرج", "غير مدرج للتكرار")
					{conditions}
					order by num_order asc
					LIMIT {limit}
				""".format(conditions=conditions,limit=doc.print_count, entity=doc.entity, fiscal_year=doc.fiscal_year), as_dict=1)
			
			for civilian in entity_data:
				table = doc.append("bon_printing_civilians", {})
				table.coupon_no = civilian.name
				table.id_number = civilian.id_number2
				table.officer_name = civilian.officer_name
				table.rank = civilian.rank
				table.entities = civilian.entities
				table.job = civilian.job
				table.assigned_work = civilian.assigned_work
				table.reason_for_entitlement = civilian.reason_for_entitlement
				table.print = civilian.print
				table.print_date = civilian.print_date
				table.fiscal_year = civilian.fiscal_year
			if doc.reason_for_entitlement:
				doc.already_printed = frappe.db.count("Civilian Clothing For Officers", {"print":"تم الطباعه", "entities":doc.entity, "fiscal_year":doc.fiscal_year, "reason_for_entitlement":doc.reason_for_entitlement})
				doc.listed = frappe.db.count("Civilian Clothing For Officers", filters={ "entities":["=",doc.entity], "fiscal_year":["=",doc.fiscal_year], "reason_for_entitlement":["!=","غير مدرج"], "reason_for_entitlement":["=",doc.reason_for_entitlement]})
				doc.unlisted = frappe.db.count("Civilian Clothing For Officers", filters={ "entities":["=",doc.entity], "fiscal_year":["=",doc.fiscal_year], "reason_for_entitlement":["=","غير مدرج"]})
			else:
				doc.already_printed = frappe.db.count("Civilian Clothing For Officers", {"print":"تم الطباعه", "entities":doc.entity, "fiscal_year":doc.fiscal_year})
				doc.listed = frappe.db.count("Civilian Clothing For Officers", filters={ "entities":["=",doc.entity], "fiscal_year":["=",doc.fiscal_year], "reason_for_entitlement":["!=","غير مدرج"]})
				doc.unlisted = frappe.db.count("Civilian Clothing For Officers", filters={ "entities":["=",doc.entity], "fiscal_year":["=",doc.fiscal_year], "reason_for_entitlement":["=","غير مدرج"]})
			
		if doc.title == "أفراد" or doc.title == "مساعدين":

			entity_data = frappe.db.sql(
				""" select
					name, id_number, people_name, rank, entities, assigned_work,
					reason_for_entitlement, print, print_date, fiscal_year
					from `tabCivilian Clothing For People` 
					where entities = '{entity}'
					and fiscal_year = '{fiscal_year}'
					and reason_for_entitlement not in  ("غير مدرج", "غير مدرج للتكرار")
					{conditions}
					LIMIT {limit}

				""".format(conditions=conditions,limit=doc.print_count, entity=doc.entity, fiscal_year=doc.fiscal_year), as_dict=1)
			
			for civilian in entity_data:
				table = doc.append("bon_printing_civilians", {})
				table.coupon_no = civilian.name
				table.id_number = civilian.id_number
				table.officer_name = civilian.people_name
				table.rank = civilian.rank
				table.entities = civilian.entities
				table.assigned_work = civilian.assigned_work
				table.reason_for_entitlement = civilian.reason_for_entitlement
				table.print = civilian.print
				table.print_date = civilian.print_date
				table.fiscal_year = civilian.fiscal_year
			if doc.reason_for_entitlement:
				doc.already_printed = frappe.db.count("Civilian Clothing For People", {"print":"تم الطباعه", "entities":doc.entity, "fiscal_year":doc.fiscal_year, "reason_for_entitlement":doc.reason_for_entitlement})
				doc.listed = frappe.db.count("Civilian Clothing For People", filters={ "entities":["=",doc.entity], "fiscal_year":["=",doc.fiscal_year], "reason_for_entitlement":["!=","غير مدرج"], "reason_for_entitlement":["=",doc.reason_for_entitlement]})
				doc.unlisted = frappe.db.count("Civilian Clothing For People", filters={ "entities":["=",doc.entity], "fiscal_year":["=",doc.fiscal_year], "reason_for_entitlement":["=","غير مدرج"]})
			else:
				doc.already_printed = frappe.db.count("Civilian Clothing For People", {"print":"تم الطباعه", "entities":doc.entity, "fiscal_year":doc.fiscal_year})
				doc.listed = frappe.db.count("Civilian Clothing For People", filters={ "entities":["=",doc.entity], "fiscal_year":["=",doc.fiscal_year], "reason_for_entitlement":["!=","غير مدرج"]})
				doc.unlisted = frappe.db.count("Civilian Clothing For People", filters={ "entities":["=",doc.entity], "fiscal_year":["=",doc.fiscal_year], "reason_for_entitlement":["=","غير مدرج"]})
			
			



	def on_submit(self):
		for row in self.bon_printing_civilians:
			if self.title == "ضباط":
				frappe.db.sql(""" 
							UPDATE `tabCivilian Clothing For Officers` set print = "تم الطباعه",
							print_date='{print_date}'
							WHERE name='{name}'
						""".format(name=row.coupon_no,print_date=nowdate()))
			if self.title == "أفراد" or self.title == "مساعدين":
				frappe.db.sql(""" 
							UPDATE `tabCivilian Clothing For People` set print = "تم الطباعه",
							print_date='{print_date}'
							WHERE name='{name}'
						""".format(name=row.coupon_no,print_date=nowdate()))
				
	def on_cancel(self):
		for row in self.bon_printing_civilians:
			if self.title == "ضباط":
				frappe.db.sql(""" 
							UPDATE `tabCivilian Clothing For Officers` set print = "لم يتم الطباعه",
							print_date= NULL
							WHERE name='{name}'
						""".format(name=row.coupon_no))
				
			if self.title == "أفراد" or self.title == "مساعدين":
				frappe.db.sql(""" 
							UPDATE `tabCivilian Clothing For People` set print = "لم يتم الطباعه",
							print_date=NULL
							WHERE name='{name}'
						""".format(name=row.coupon_no))