// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.query_reports["تقرير المحاكمات العسكرية و الجنائية"] = {
	"filters": [
		{
			fieldname: "recruit",
			label: __("أسم المجند"),
			fieldtype: "Link",
			options: "The Recruits"
		}
	]
};
