// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.query_reports["Daily Visitors"] = {
	"filters": [
	    {
			fieldname: "from_date",
			label: __("من تاريخ"),
			fieldtype: "Date",
			default: frappe.datetime.get_today(),
		},
		{
			fieldname:"to_date",
			label: __("إلى تاريخ"),
			fieldtype: "Date",
			default: frappe.datetime.get_today(),
		},
        {
			fieldname: "genral_visit",
			label: __("جهة الزيارة الرئيسية"),
			fieldtype: "Select",
			options: ["","الإدارة العامة للمركبات","الإدارة العامة للإمداد"],
		},
	]
};