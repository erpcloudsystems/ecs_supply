// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Recording Work Assigned To Officer Report"] = {
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
			fieldname: "officers",
			label: __("رقم الضابط"),
			fieldtype: "Link",
			options: "Employee",
		},
        {
			fieldname: "rank",
			label: __("الرتبة"),
			fieldtype: "Link",
			options: "Officer Rank",
		},

	]
};