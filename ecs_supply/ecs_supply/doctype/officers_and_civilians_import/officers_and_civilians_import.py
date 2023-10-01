# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
# import pyodbc

import os

#to get the current working directory


class OfficersandCiviliansImport(Document):
	def validate(self):
		directory = os.getcwd()
	# 	frappe.msgprint(self.attach_file)
	# 	# file_path = directory + self.attach_file
	# 	# frappe.msgprint(file_path)
	# 	# db_driver = '{Microsoft Access Driver (*.mdb, *.accdb)}'
	# 	# db_path = '//10.0.0.5/ex_backup2/frappe/frappe-bench/sites/erp.emdad.local/public/files/افراد (1).mdb'
	# 	import pandas_access as mdb
	# 	os.chdir('/private/files')

	# 	db_filename = 'افراد (1).mdb'
	# 	# Listing the tables.
	# 	for tbl in mdb.list_tables(db_filename):
	# 		frappe.msgprint(tbl)
	# 	# Read a small table.
	# 	df = mdb.read_table(db_filename, "OFF_PER_DATA")
	# 	frappe.msgprint(str(df))

		# frappe.msgprint(self.attach_file)
