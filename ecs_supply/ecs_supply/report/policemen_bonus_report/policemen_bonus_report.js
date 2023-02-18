// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Policemen Bonus Report"] = {
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
			fieldname: "policemen",
			label: __("رقم الفرد"),
			fieldtype: "Link",
			options: "Employee",
		},
		{
			fieldname: "bonus_type",
			label: __("نوع العلاوة"),
			fieldtype: "Link",
			options: "Bonus Type",
		},
        {
			fieldname: "year",
			label: __("السنة"),
			fieldtype: "Data",
		},
	]
};