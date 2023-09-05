# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MergeLettersinNames(Document):
	def merge_phrases_civ_clothes(self,doctype, people_name):
		civ = frappe.db.sql("""
		SELECT *
		FROM `tabPhrases to Merge` civ
		""",as_dict=1)
		for phrase in civ:
			update_civ = frappe.db.sql("""
			UPDATE `{doctype}` civ
			set civ.{people_name} = replace(civ.{people_name},"{old_phrase}", "{new_phrase}")
			""".format(old_phrase=phrase.old_phrase, new_phrase=phrase.new_phrase,doctype=doctype, people_name=people_name))
			frappe.db.commit()
	def validate(self):
		self.merge_phrases_civ_clothes("tabCivilian Clothing For People","people_name")
		self.merge_phrases_civ_clothes("tabCivilian Clothing For Officers", "officer_name")
