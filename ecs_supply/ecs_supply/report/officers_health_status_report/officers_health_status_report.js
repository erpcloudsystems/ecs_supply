// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Officers Health Status Report"] = {
	"filters": [
	    {
			fieldname: "from_date",
			label: __("من تاريخ"),
			fieldtype: "Date",
		},
		{
			fieldname:"to_date",
			label: __("إلى تاريخ"),
			fieldtype: "Date",
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
        {
			fieldname: "injury_type",
			label: __("نوع الاصابة"),
			fieldtype: "Link",
			options: "Injury Type",
		},

	]
};