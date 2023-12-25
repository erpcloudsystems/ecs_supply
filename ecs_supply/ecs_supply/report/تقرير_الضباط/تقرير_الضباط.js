// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.query_reports["تقرير الضباط"] = {
	"filters": [
		{
			fieldname: "officer_name",
			label: __("اسم الضابط"),
			fieldtype: "Link",
			options: "Officers Affairs",
		},
		{
			fieldname: "id_number",
			label: __("رقم الأقدمية"),
			fieldtype: "Data",
		},
		{
			fieldname: "rank",
			label: __("الرتبة"),
			fieldtype: "Link",
			options: "Policemen Rank",
		}
	]
};