// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.query_reports["تقرير الحالات النفسية للظباط"] = {
	"filters": [
		{
			fieldname: "recruit",
			label: __("أسم المتحري عنه"),
			fieldtype: "Link",
			options: "Officers Affairs"
		},
		{
			fieldname: "health_details3",
			label: __("الحالة النفسية"),
			fieldtype: "Select",
			options: ['طبيعية', 'غير طبيعية','']
		},
	]
};
