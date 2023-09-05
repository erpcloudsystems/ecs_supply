# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CivilianClothingForPeople(Document):
	def merge_phrases_civ_clothes(self,doctype, people_name):
		civ = frappe.db.sql("""
		SELECT *
		FROM `tabPhrases to Merge` civ
		""",as_dict=1)
		for phrase in civ:
			frappe.db.sql("""
			UPDATE `tabCivilian Clothing For People` 
			set people_name = replace(people_name,"{old_phrase}", "{new_phrase}")
			WHERE name = "{name}"
			""".format(old_phrase=phrase.old_phrase, new_phrase=phrase.new_phrase,name=self.name))
			frappe.db.commit()
		self.reload()
	def after_insert(self):
		self.merge_phrases_civ_clothes("tabCivilian Clothing For People","people_name")
		# self.merge_phrases_civ_clothes("tabCivilian Clothing For Officers", "officer_name")
