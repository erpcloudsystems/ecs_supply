// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Penalty During Year Report"] = {
	"filters": [
        {
			fieldname: "policemen",
			label: __("رقم الموظف"),
			fieldtype: "Link",
			options: "Employee",
		},
		{
			fieldname: "policemen_rank",
			label: __("الرتبة"),
			fieldtype: "Link",
			options: "Policemen Rank",
		},
	]
};