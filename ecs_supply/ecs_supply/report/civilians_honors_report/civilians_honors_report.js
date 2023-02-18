// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Civilians Honors Report"] = {
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
			label: __("رقم الفرد"),
			fieldtype: "Link",
			options: "Employee",
		},
        {
			fieldname: "type_of_honor",
			label: __("نوع التكريم"),
			fieldtype: "Link",
			options: "Type of Honor",
		},
	]
};