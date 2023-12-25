// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.query_reports["تقرير الحالة النفسية"] = {
		"filters": [
			{
				fieldname: "recruit",
				label: __("أسم المتحري عنه"),
				fieldtype: "Link",
				options: "Envestigation Employee"
			},
			{
				fieldname: "health_details3",
				label: __("الحالة النفسية"),
				fieldtype: "Select",
				options: ['طبيعية', 'غير طبيعية','']
			},
		]
	};
	