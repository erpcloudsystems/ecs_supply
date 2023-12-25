// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.query_reports["تقرير الكشف الجنائي للظباط"] = {
	"filters": [
		{
			fieldname: "recruit",
			label: __("أسم الظابط"),
			fieldtype: "Link",
			options: "Officers Affairs"
		}
	]
};
