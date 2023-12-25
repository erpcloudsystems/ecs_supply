// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Civilians Secret Report"] = {
	"filters": [
	    // {
		// 	fieldname: "from_date",
		// 	label: __("من تاريخ"),
		// 	fieldtype: "Date",
		// 	default: frappe.datetime.add_months(frappe.datetime.get_today(), -12),
		// },
		// {
		// 	fieldname:"to_date",
		// 	label: __("إلى تاريخ"),
		// 	fieldtype: "Date",
		// 	default: frappe.datetime.get_today(),
		// },
        {
			fieldname: "civilians",
			label: __("رقم الموظف"),
			fieldtype: "Link",
			options: "Employee",
		},
        {
			fieldname: "civilians_degree",
			label: __("الدرجة الوظيفية"),
			fieldtype: "Link",
			options: "Civilians Degree",
		},
        {
			fieldname: "estimation",
			label: __("التقدير"),
			fieldtype: "Link",
			options: "Estimation",
		},
        {
			fieldname: "year",
			label: __("السنة"),
			fieldtype: "Data",
		},

	]
};