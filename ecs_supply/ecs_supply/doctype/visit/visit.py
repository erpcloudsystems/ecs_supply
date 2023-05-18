# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Visit(Document):
	pass


def updatedate2():
    import datetime
    veh_license = frappe.db.sql("""
    SELECT visitdate as visitdate, name
    FROM `tabDaily Visit`

    """, as_dict=1)
    counter = 0
    for row in veh_license:
        try:
            # print(row)
            # day = row.date.split("-")[0][2:]
            # date = datetime.datetime.strptime(str(day) +"-"+ str(row.date.split("-")[1]) +"-"+ str(row.date.split("-")[2]), '%d-%m-%y').date()
            visitdate = datetime.datetime.strptime(row.visitdate, '%d-%b-%y').date()
            veh_license_date = frappe.db.sql("""
                UPDATE `tabDaily Visit` SET visitdate="{visitdate}" where name="{name}"
                """.format(visitdate=visitdate.strftime("%Y-%m-%d"), name=row.name))
            # print(visitdate)
        except Exception as e:
            print(e)