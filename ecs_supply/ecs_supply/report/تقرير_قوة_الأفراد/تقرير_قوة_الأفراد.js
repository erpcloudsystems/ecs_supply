// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.query_reports["تقرير قوة الأفراد"] = {
	"filters": [
		{
			fieldname: "id_number",
			label: __("رقم الشرطة"),
			fieldtype: "Data",
		},
		{
			fieldname: "rank",
			label: __("الرتبة"),
			fieldtype: "Link",
			options: "police rank",
		},
		{
			fieldname: "officer_name",
			label: __("اسم الفرد"),
			fieldtype: "Link",
			options: "Envestigation Employee",
		},
	]
};
