// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Policemen Punishment Report"] = {
	"filters": [
        {
			fieldname: "policemen",
			label: __("أسم الفرد"),
			fieldtype: "Link",
			options: "Envestigation Employee",
		}
	]
};