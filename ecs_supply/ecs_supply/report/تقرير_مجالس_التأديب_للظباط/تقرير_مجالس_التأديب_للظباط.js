// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.query_reports["تقرير مجالس التأديب للظباط"] = {
	"filters": [
        {
			fieldname: "policemen",
			label: __("أسم الظابط"),
			fieldtype: "Link",
			options: "Officers Affairs",
		}
	]
};