// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.query_reports["تقرير حائزي المركبات الخاصة"] = {
	"filters": [
		{
			fieldname: "recruit",
			label: __("أسم المتحري عنه"),
			fieldtype: "Link",
			options: "Envestigation Employee"
		}
	]
};
