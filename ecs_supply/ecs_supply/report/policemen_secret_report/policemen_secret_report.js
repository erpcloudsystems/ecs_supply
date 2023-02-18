// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Policemen Secret Report"] = {
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
			fieldname: "estimation",
			label: __("التقدير"),
			fieldtype: "Link",
			options: "Estimation",
		},

	]
};