# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import fractions
import frappe
from frappe.model.document import Document

class CivilianClothingForOfficers(Document):
	def merge_phrases_civ_clothes(self,doctype, people_name):
		civ = frappe.db.sql("""
		SELECT *
		FROM `tabPhrases to Merge` civ
		""",as_dict=1)
		for phrase in civ:
			self.officer_name = self.officer_name.replace(phrase.old_phrase, phrase.new_phrase)
		# 	frappe.db.sql("""
		# 	UPDATE `tabCivilian Clothing For Officers` 
		# 	set officer_name = replace(officer_name,"{old_phrase}", "{new_phrase}")
		# 	WHERE name = "{name}"
		# 	""".format(old_phrase=phrase.old_phrase, new_phrase=phrase.new_phrase,name=self.name))
		# 	frappe.db.commit()
		# self.reload()

	def get_id_number(self):
		id_number = ""
		id_number += str(self.no1) if self.no1 else ""
		id_number += str(self.no2) if self.no2 else ""
		id_number += str(self.no3) if self.no3 else ""
		id_number += str(self.no4) if self.no4 else ""

		return id_number
	
	def get_id_number2(self):
		id_number = []
		id_number.append(str(self.no1) if self.no1 else "")
		id_number.append(str(self.no2) if self.no2 else "")
		id_number.append(str(self.no3) if self.no3 else "")
		id_number.append(str(self.no4) if self.no4 else "")
		return id_number
	def check_duplicate_name(self):

		officers = frappe.db.get_all("Civilian Clothing For Officers", {"officer_name": self.officer_name})
		officers_list = []
		
		for row in officers:
			if self.name != row["name"]:
				officers_list.append(row)
		if officers_list:
			frappe.msgprint(f"ضابط {self.officer_name} موجود بالفعل ")

		officers = frappe.db.get_all("Civilian Clothing For Officers", {"id_number": str(self.id_number)})
		officers_list = []
		for row in officers:
			if self.name != row["name"]:
				officers_list.append(row)
		if officers_list:
			frappe.throw(f"   رقم أقدمية   {self.id_number} موجود بالفعل")


	def validate_officers_data(self):
		#validate duplicate officer name
		if self.no1 or self.no2 or self.no3 or self.no4:
			self.num_order = "19" + str(self.no2) +("0" * (5-len(str(self.no1)))) + str(self.no1) if len(str(self.no2)) <= 2 else str(self.no2) +("0" * (5-len(str(self.no1)))) + str(self.no1) 
			self.id_number = self.get_id_number()
			self.id_number2 = "/".join(self.get_id_number2())
		
		if self.is_new():
			self.check_duplicate_name()
	def validate(self):
		self.validate_officers_data()
		# self.merge_phrases_civ_clothes("tabCivilian Clothing For People","people_name")
		# self.merge_phrases_civ_clothes("tabCivilian Clothing For Officers", "officer_name")

