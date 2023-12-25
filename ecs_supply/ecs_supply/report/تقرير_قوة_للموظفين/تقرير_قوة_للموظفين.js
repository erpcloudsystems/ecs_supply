// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.query_reports["تقرير قوة للموظفين"] = {
	"filters": [
		{
			fieldname: "main_department23",
			label: __("جهة العمل الداخلية"),
			fieldtype: "Data",
		},
		{
			fieldname: "the_academic_qualification",
			label: __("المؤهل الدراسي"),
			fieldtype: "Data",
		},
		{
			fieldname: "hr",
			label: __("اسم الموظف"),
			fieldtype: "Link",
			options:"Human Resources"
		},
	]
};