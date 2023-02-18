// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Officer Conferences Details Report"] = {
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
			fieldname: "conference_name",
			label: __("اسم المؤتمر"),
			fieldtype: "Link",
			options: "Conference Name",
		},
        {
			fieldname: "conference_side",
			label: __("جهة المؤتمر"),
			fieldtype: "Link",
			options: "Conference Side",
		},

	]
};