// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.query_reports["تقرير قوة للمجندين"] = {
	"filters": [
		{
			fieldname: "id_number",
			label: __("رقم الشرطة"),
			fieldtype: "Data",
		},
		{
			fieldname: "officer_name",
			label: __("اسم المجند"),
			fieldtype: "Link",
			options:"The Recruits"
		},
		{
			fieldname: "from_date",
			label: __("من تاريخ"),
			fieldtype: "Date",
		},
		{
			fieldname:"to_date",
			label: __("إلى تاريخ"),
			fieldtype: "Date",
		},
	]
};
