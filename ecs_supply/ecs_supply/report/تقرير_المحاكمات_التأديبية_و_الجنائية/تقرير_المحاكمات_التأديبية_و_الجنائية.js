// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.query_reports["تقرير المحاكمات التأديبية و الجنائية"] = {
	"filters": [
		{
			fieldname: "recruit",
			label: __("أسم الموظف"),
			fieldtype: "Link",
			options: "Human Resources"
		}
	]
};
