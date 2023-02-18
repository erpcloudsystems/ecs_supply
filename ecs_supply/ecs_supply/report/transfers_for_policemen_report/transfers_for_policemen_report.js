// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Transfers for Policemen Report"] = {
	"filters": [
	    {
			fieldname: "from_date",
			label: __("من تاريخ"),
			fieldtype: "Date",
			default: frappe.datetime.add_months(frappe.datetime.get_today(), -12),
		},
		{
			fieldname:"to_date",
			label: __("إلى تاريخ"),
			fieldtype: "Date",
			default: frappe.datetime.get_today(),
		},
        {
			fieldname: "policemen",
			label: __("رقم الفرد"),
			fieldtype: "Link",
			options: "Employee",
		},
        {
			fieldname: "policemen_rank",
			label: __("الرتبة"),
			fieldtype: "Link",
			options: "Policemen Rank",
		},
        {
			fieldname: "current_main_department",
			label: __("جهة العمل الرئيسية"),
			fieldtype: "Link",
			options: "Main Department",
		},
        {
			fieldname: "current_sub_department",
			label: __("جهة العمل الداخلية"),
			fieldtype: "Link",
			options: "Sub Department",
		},
	]
};