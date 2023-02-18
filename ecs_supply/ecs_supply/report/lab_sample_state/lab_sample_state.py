# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe import msgprint, _
from frappe.utils import flt


def execute(filters=None):
    columns, data = [], []
    columns = get_columns()
    data = get_data(filters, columns)
    return columns, data


def get_columns():
    return [
		{
			"label": _(" المعمل   "),
			"fieldname": "lab",
			"fieldtype": "Data",
			"width": 180
		},{
			"label": _("اجمالي العينات المسجلة "),
			"fieldname": "total1",
			"fieldtype": "Float",
			"width": 180
		},
		{
			"label": _("اجمالي العينات تم اصدار تقرير"),
			"fieldname": "total4",
			"fieldtype": "Float",
			"width": 200
		},
        {
            "label": _("اجمالي التقارير المسلمة  "),
            "fieldname": "total3",
            "fieldtype": "Float",
            "width": 200
        },
       
    ]


def get_data(filters, columns):
    item_price_qty_data = []
    item_price_qty_data = get_item_price_qty_data(filters)
    return item_price_qty_data


def get_item_price_qty_data(filters):
    conditions = ""
    conditions1 = ""

    if filters.get("from_date"):
        conditions1 += " and `tabLab Sample`.report_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions1 += " and `tabLab Sample`.report_date <= %(to_date)s"
    if filters.get("from_date"):
        conditions += " and `tabSample`.sample_receipt_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " and `tabSample`.sample_receipt_date <= %(to_date)s"



    lab = frappe.db.sql("""
        Select
			name as lab,
			name1 as lab_name
		from `tabLab`
        """, as_dict=1)

    result = []
    if lab:
        for x in lab:
            data = {
                'lab': x.lab + "-" + str(x.lab_name),
            }
            item_results = frappe.db.sql("""
               select
					`tabSample`.lab as lab, 
					ifnull(count(`tabSample`.name),0)  as total12,
                    (select ifnull(count(`tabLab Sample`.name),0) from `tabLab Sample`  where  `tabLab Sample`.workflow_state = "Delivered" and `tabLab Sample`.lab = '{lab}'  {conditions1} ) as total3,
			 		(select ifnull(count(`tabLab Sample`.name),0) from `tabLab Sample`  where  `tabLab Sample`.workflow_state = "Report Created" and  `tabLab Sample`.lab = '{lab}'  {conditions1} ) as total4
				from
					`tabSample`	
                where
                   `tabSample`.lab = '{lab}'
                   and `tabSample`.workflow_state = "تم تسديد الرسوم"
                   {conditions}
                 """.format(lab=x.lab, conditions=conditions, conditions1=conditions1), filters, as_dict=1)
           
            for item_dict in item_results:
                data['total1'] = item_dict.total12
                data['total3'] = item_dict.total3
                data['total4'] = item_dict.total4

               

            result.append(data)
    return result























