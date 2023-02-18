// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Civilians Promotion Report"] = {
	"filters": [
	    {
			fieldname: "from_date",
			label: __("من تاريخ"),
			fieldtype: "Date",
			default: frappe.datetime.add_months(frappe.datetime.get_today(), -12),
		},
		{
			fieldname:"to_date",
			label: __("إلى تاريخ"),
			fieldtype: "Date",
			default: frappe.datetime.get_today(),
		},
        {
			fieldname: "civilians",
			label: __("رقم الموظف"),
			fieldtype: "Link",
			options: "Employee",
		},
        {
			fieldname: "current_civilians_degree",
			label: __("الدرجة"),
			fieldtype: "Link",
			options: "Civilians Degree",
		},
        {
			fieldname: "current_sub_degree",
			label: __("فئة الدرجة"),
			fieldtype: "Link",
			options: "Sub Degree",
		},
	]
};