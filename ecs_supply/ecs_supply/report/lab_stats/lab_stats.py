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
			"label": _("اجمالي العينات المسددةللرسوم"),
			"fieldname": "total2",
			"fieldtype": "Float",
			"width": 200
		},
        {
            "label": _("اجمالي العينات منتظره التسديد "),
            "fieldname": "total3",
            "fieldtype": "Float",
            "width": 200
        },
        {
            "label": _(" اجمالي الدخل للمعمل"),
            "fieldname": "total4",
            "fieldtype": "Float",
            "width": 160
        },
		{
			"label": _("اجمالي المنتظر تسديدة "),
			"fieldname": "total5",
			"fieldtype": "Float",
			"width": 160
		},
        {
            "label": _("ايراد المعمل الكلي"),
            "fieldname": "total6",
            "fieldtype": "Float",
            "width": 160
        },
    ]


def get_data(filters, columns):
    item_price_qty_data = []
    item_price_qty_data = get_item_price_qty_data(filters)
    return item_price_qty_data


def get_item_price_qty_data(filters):
    conditions = ""
    if filters.get("sample_receipt"):
        conditions += " and `tabSample`.sample_receipt >= %(sample_receipt)s"
    
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
					`tabSample`.lab as lab, `tabSample`.lab_name as lab_name, ifnull(count(`tabSample`.name),0) as total1, ifnull(sum(`tabSample`.price),0) as total6,
					(select ifnull(sum(`tabSample`.price),0) from `tabSample` where  `tabSample`.workflow_state = "انتظار تسديد الرسوم" and  `tabSample`.lab = '{lab}'  {conditions}) as total5,
					(select ifnull(count(`tabSample`.name),0) from `tabSample` where  `tabSample`.workflow_state = "انتظار تسديد الرسوم" and  `tabSample`.lab = '{lab}'  {conditions} ) as total3,
					(select ifnull(sum(`tabSample`.price),0) from `tabSample` where  `tabSample`.workflow_state = "تم تسديد الرسوم" and  `tabSample`.lab = '{lab}'  {conditions} ) as total4,
					(select ifnull(count(`tabSample`.name),0) from `tabSample` where  `tabSample`.workflow_state = "تم تسديد الرسوم" and  `tabSample`.lab = '{lab}'  {conditions} ) as total2
				from
					`tabSample`	
                where
                   `tabSample`.lab = '{lab}'
                   {conditions}
                """.format(lab=x.lab, conditions=conditions), filters, as_dict=1)
            for item_dict in item_results:
                data['total1'] = float(item_dict.total2) + float(item_dict.total3)
                data['total2'] = item_dict.total2
                data['total3'] = item_dict.total3
                data['total4'] = item_dict.total4
                data['total5'] = item_dict.total5
                data['total6'] = float(item_dict.total4) + float(item_dict.total5)
               

            result.append(data)
    return result




























    # result = []
    # item_results1 = frappe.db.sql("""
    #     select
    #         `tabSample`.lab as lab, `tabSample`.lab_name as lab_name, count(`tabSample`.name) as total1, sum(`tabSample`.price) as total6,
    #         (select sum(`tabSample`.price) from `tabSample` where  `tabSample`.workflow_state = "انتظار تسديد الرسوم" ) as total5,
    #         (select count(`tabSample`.name) from `tabSample` where  `tabSample`.workflow_state = "انتظار تسديد الرسوم" ) as total3,
    #         (select sum(`tabSample`.price) from `tabSample` where  `tabSample`.workflow_state = "تم تسديد الرسوم" ) as total4,
    #         (select count(`tabSample`.name) from `tabSample` where  `tabSample`.workflow_state = "تم تسديد الرسوم" ) as total2
    #     from
    #         `tabSample`
       
    #         {conditions}
    #         GROUP BY `tabSample`.lab
    #     """.format(conditions=conditions), filters, as_dict=1)

    # for item_dict in item_results1:
    #     data = {
    #         'lab': item_dict.lab + "-" + str(item_dict.lab_name),
    #         'total1': item_dict.total1,
    #         'total2': item_dict.total2,
    #         'total3': item_dict.total3,
    #         'total4': item_dict.total4,
    #         'total5': item_dict.total5,
    #         'total6': item_dict.total6,
    #     }
    #     result.append(data)
    # return result